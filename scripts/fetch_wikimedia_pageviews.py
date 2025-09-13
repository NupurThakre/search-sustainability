# scripts/fetch_wikimedia_pageviews.py
import requests, urllib.parse, time, csv
from datetime import datetime, timedelta

# CONFIG: edit these
project = "en.wikipedia"           # e.g., en.wikipedia, es.wikipedia
articles = [
    "Python_(programming_language)",
    "Google",
    "IPhone",
    "Artificial_intelligence",
    "Youtube"
]
# month sample: start_date (YYYY-MM-DD) and end_date (YYYY-MM-DD)
start_date = "2025-08-01"
end_date   = "2025-08-31"

# convert to API format YYYYMMDD00
def to_api_date(d):
    return datetime.strptime(d, "%Y-%m-%d").strftime("%Y%m%d00")

start_api = to_api_date(start_date)
end_api   = to_api_date(end_date)

outrows = []
for article in articles:
    # URL-encode article
    article_enc = urllib.parse.quote(article, safe='')
    url = (
        f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
        f"{project}/all-access/user/{article_enc}/daily/{start_api}/{end_api}"
    )
    headers = {"User-Agent":"search-sustainability-script/1.0 nupurthakre979@gmail.com"}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("WARN: failed for", article, r.status_code, r.text[:200])
        time.sleep(1)
        continue
    data = r.json().get("items", [])
    for item in data:
        outrows.append({
            "project": project,
            "page": article,
            "date": item["timestamp"][:8],   # YYYYMMDD
            "views": item.get("views", 0)
        })
    time.sleep(0.8)  # be polite to API

# write CSV
import os
os.makedirs("data", exist_ok=True)
with open("data/wikimedia_pageviews_1month.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["project","page","date","views"])
    writer.writeheader()
    for r in outrows:
        writer.writerow(r)
print("Saved data/wikimedia_pageviews_1month.csv rows:", len(outrows))
