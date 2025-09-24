# Ingest verification — Search Sustainability
**Date:** 2025-09-23  
**Operator:** Nupur (pguser)  
**Notes:** ingest path: `data/raw_search_events_ingest.csv` → `public.raw_search_events_stg` → `public.raw_search_events`. Index `ux_raw_qh_user_ts` created by DBA; ingest executed as `pguser`.

---

## 1) Exact SQL executed for verification

-- 1) total rows in canonical table
SELECT 'raw_count' AS metric, COUNT(*) AS cnt FROM raw_search_events;

-- 2) distinct query_hash count
SELECT 'distinct_queries' AS metric, COUNT(DISTINCT query_hash) AS cnt FROM raw_search_events;

-- 3) top 10 queries (by volume)
SELECT query_text, query_hash, COUNT(*) AS cnt
FROM raw_search_events
GROUP BY query_text, query_hash
ORDER BY cnt DESC
LIMIT 10;

-- 4) sample recent rows
SELECT event_id, event_ts, user_pseudonym, substring(query_text for 120) AS q
FROM raw_search_events
ORDER BY event_ts DESC
LIMIT 10;

-- 5) staging rows (should be 0 if we truncated)
SELECT COUNT(*) AS staging_rows FROM raw_search_events_stg;

---

## 2) Captured outputs (run results)

### 2.1 raw_count
metric | cnt
---------+-----
raw_count| 5000


(Verified: `SELECT COUNT(*) FROM public.raw_search_events;` → `5000`)

---

### 2.2 distinct_queries

Command to run (psql):
psql -U pguser -d sustainability -c "SELECT 'distinct_queries' AS metric, COUNT(DISTINCT query_hash) AS cnt FROM public.raw_search_events;"


**Result:** 
      metric      | cnt
------------------+-----
 distinct_queries |  15
(1 row)

---

### 2.3 top 10 queries (by volume)

Command to run (psql):
psql -U pguser -d sustainability -c "SELECT query_text, query_hash, COUNT(*) AS cnt FROM public.raw_search_events GROUP BY query_text, query_hash ORDER BY cnt DESC LIMIT 10;"


**Result:** 
            query_text            |                            query_hash                            | cnt
----------------------------------+------------------------------------------------------------------+-----
 cheapest flights delhi to mumbai | e068b1512f632dd108e9bcf764cebf528805353986b62533e24b72e2abd9f828 | 359
 healthy diet tips                | b2dda823cd37a5e3cdcafa424c62057a564195aa4092113fdf5e889f11571c50 | 357
 weather nagpur                   | 676748130f51f53a45aa53d95a73b4951d98f5696d2b3967ce39b41671905776 | 355
 facebook login                   | 19dbebf66ccf4bc8a7ebbf4ae37583c4a37b09c1eb41ec5152d15a9f02d9366c | 340
 climate change statistics        | 7cfbabee2c50674d24af0bcf27957bc87d51ae817efaf8e76a076cd778e96e69 | 340
 nearest hospital                 | b9cbc67ffc276abb4a30e5d4364728e5c95bf33ed06850fd45cd2b3501272e80 | 335
 download spotify                 | 9213322ceb59e3d2035ba939280eb13d611f9e51937ee5f6aa2ccf61837f087c | 333
 book hotel in goa                | f3fe76c55a740e14431a4985e2208a4d730c86664bc63a0b6b4efec21e981f1f | 332
 buy iphone 15 online             | e3b843560f4abf544d9f3787342bd6365a05070e7b30c4297f579372196478db | 328
 twitter trending                 | 76c698b91084dedbe6cf04b9e3fa61f74918c8119d9b7245aff5c6a01d04e122 | 326
(10 rows)

---

### 2.4 sample recent rows (captured)
event_id | event_ts | user_pseudonym | q
----------+---------------------------+------------------------------------------------------------------+--------------------------------------------
5000 | 2025-09-13 13:28:39+05:30 | 2c5048f353693143c9112db707fae27829c9d4dd680473ce589a113a3dbde934 | how tall is eiffel tower
4999 | 2025-09-10 09:54:20+05:30 | c03101871213d4a2b8fc78d50230d2e4fef115f3d011a99bfc26c69dc1b8d873 | cheapest flights delhi to mumbai
4998 | 2025-09-10 19:31:01+05:30 | f94c7d4cb08da98318056b611f523c47b7d641c025f7b63a1293baff50e517bd | facebook login
4997 | 2025-09-03 07:09:00+05:30 | 436c99c155e588291d7115c889a52ce6d9e18956a7e71374285937af91b8e657 | healthy diet tips
4996 | 2025-09-03 19:12:03+05:30 | 2e6c645705a36efb26ff98d8f5930f70e13635f8afa4beaaac8b20f251adfac6 | order pizza online
4995 | 2025-09-05 12:57:07+05:30 | 3a29aeca58ec4d3faec20ec4181d91ec636b96fac3f34d8f88d1be5a5aac5adb | python pandas tutorial
4994 | 2025-09-12 10:31:11+05:30 | 962ac8bec54d86395fd657ac449a53946ce98f6ebf73509a8ef44eac32064c0d | book hotel in goa
4993 | 2025-09-12 21:14:59+05:30 | dffbc270326a1d5bc7fa206e34bb38b8640cccb9bc0deb2dc21c0b8ce399f6b4 | download spotify
4992 | 2025-09-14 11:46:53+05:30 | 7c24157032d147b0e8f3afd625b0cedea282b8ff8ab71c0248bab606f4cfd300 | download spotify
4991 | 2025-09-06 13:16:38+05:30 | 12731e825e9ae70255efcb6ec22a5f7807bd0ca674c8ee2d913406f9bbce1f26 | book hotel in goa


---

### 2.5 staging_rows
staging_rows
        0


(Verified: `SELECT COUNT(*) FROM public.raw_search_events_stg;` → `0`)

---

## 3) Observations & next steps
- Canonical contains **5000** events. Staging is empty (truncated) — that matches expected behavior for a successful ingest.  
- No exact duplicates were detected (unique index `ux_raw_qh_user_ts` enforced uniqueness).  
- Next: run the `distinct_queries` and `top 10` commands above and paste their outputs into sections 2.2 and 2.3. Commit this doc.

---

## 4) Commands to append outputs automatically (PowerShell)
Run this PowerShell snippet from your project root to run the two missing queries and append results to this file:

```powershell
$env:PGPASSWORD='<your_password>'
$OUT = "docs/ingest_verification.md"

# 1) distinct count (human-friendly)
"### 2.2 distinct_queries (appended)" | Out-File -Append -Encoding utf8 $OUT
psql -U pguser -d sustainability -c "SELECT 'distinct_queries' AS metric, COUNT(DISTINCT query_hash) AS cnt FROM public.raw_search_events;" | Out-File -Append -Encoding utf8 $OUT

# 2) top 10 queries (simple table format)
"### 2.3 top 10 queries (appended)" | Out-File -Append -Encoding utf8 $OUT
psql -U pguser -d sustainability -c "SELECT query_text, query_hash, COUNT(*) AS cnt FROM public.raw_search_events GROUP BY query_text, query_hash ORDER BY cnt DESC LIMIT 10;" | Out-File -Append -Encoding utf8 $OUT
