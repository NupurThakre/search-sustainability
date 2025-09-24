# scripts/prepare_raw_ingest.py
import os
import hashlib
import json
from datetime import datetime
import pandas as pd

# ---------- CONFIG ----------
IN = os.environ.get("INGEST_IN", "data/raw_search_events.csv")
OUT = os.environ.get("INGEST_OUT", "data/raw_search_events_ingest.csv")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

# ---------- HELPERS ----------
def sha256_hex(s: str) -> str:
    return hashlib.sha256(str(s).encode("utf-8")).hexdigest()

def device_from_ua(ua: str) -> str:
    """Naive device inference from user agent string"""
    ua = (ua or "").lower()
    if "mobile" in ua:
        return "mobile"
    if "tablet" in ua or "ipad" in ua:
        return "tablet"
    if "windows" in ua or "macintosh" in ua or "linux" in ua:
        return "desktop"
    return "other"

# ---------- MAIN ----------
df = pd.read_csv(IN, dtype=str, na_filter=False)

rows = []
for _, r in df.iterrows():
    # Handle timestamp
    event_ts = r.get("event_ts") or r.get("timestamp") or ""
    try:
        # enforce ISO8601
        event_ts = pd.to_datetime(event_ts).isoformat()
    except Exception:
        event_ts = ""

    # Build base raw payload
    raw_payload_safe = {}
    for k, v in r.items():
        if v not in ("", None):
            raw_payload_safe[k] = v

    # --- SANITIZE PAYLOAD ---
    # remove direct identifiers
    for key in ("user_id", "email", "ip"):
        raw_payload_safe.pop(key, None)

    # add pseudonym (deterministic, based on session_id or query_hash fallback)
    pseudo_source = r.get("session_id") or r.get("user_pseudonym") or r.get("query_hash") or os.urandom(8).hex()
    raw_payload_safe["user_pseudonym"] = sha256_hex(pseudo_source)

    # add ingest metadata
    raw_payload_safe["ingest_schema"] = "v1"
    raw_payload_safe["ingest_ts"] = datetime.utcnow().isoformat()
    raw_payload_safe["ingest_source"] = os.path.basename(IN)

    # --- NORMALIZE FIELDS ---
    # country
    country_val = r.get("country") if r.get("country") else (r.get("region") if r.get("region") else "")

    # user agent (fill missing with placeholder)
    ua_val = r.get("user_agent") if r.get("user_agent") else "unknown-UA"

    # device type
    explicit_device = r.get("device_type") if r.get("device_type") else None
    inferred_device = device_from_ua(ua_val)
    device_type_val = explicit_device or (inferred_device if inferred_device != "other" else None) or "other"

    # query hash (deterministic)
    qh = sha256_hex(r.get("query_text") or r.get("query") or "")

    # append clean row
    rows.append({
        "query_text": r.get("query_text") or r.get("query") or "",
        "query_hash": qh,
        "user_pseudonym": raw_payload_safe["user_pseudonym"],
        "session_id": r.get("session_id", ""),
        "event_ts": event_ts,
        "country": country_val,
        "region": r.get("region", ""),
        "language": r.get("language", "en"),
        "device_type": device_type_val,
        "user_agent": ua_val,
        "result_type": r.get("result_type") or r.get("query_type") or "web",
        "click_count": int(r.get("click_count") or r.get("result_clicks") or 0),
        "raw_payload": json.dumps(raw_payload_safe, ensure_ascii=False)
    })

# ---------- WRITE OUT ----------
out_df = pd.DataFrame(rows)
out_df.to_csv(OUT, index=False)
print(f"Wrote sanitized ingest file: {OUT}")
