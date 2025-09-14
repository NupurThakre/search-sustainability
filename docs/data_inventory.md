# Data Inventory

- raw_search_events_sample.csv  
  Synthetic mini dataset for local tests.

- wikimedia_pageviews_sample.csv  
  Small 15-row sample of daily pageview counts for selected articles  
  (Python, Google, iPhone, Artificial Intelligence, YouTube).  
  Source: Wikimedia REST API.  
  Period: 2025-08-01 → 2025-08-31.  
  Notes: Full dataset (`data/wikimedia_pageviews_1month.csv`) is excluded from Git for size and governance reasons. Regenerate locally via `scripts/fetch_wikimedia_pageviews.py`.

## Dataset: MS MARCO Queries Dev (Sample)

- **File (working, local):** data/msmarco_queries_sample_sanitized.csv  
- **Showcase (committed):** data/msmarco_queries_showcase.csv  --  Tiny 15-row subset of sanitized MS MARCO queries.
- **Source:** Retrieved using Python script (kaggle/huggingface downloader).  
- **Provenance:** Derived from the "ms-marco-queries-dev" dataset (Kaggle slug: `manupande21111997/ms-marco-queries-dev`).  
- **License:** MIT (see docs/licenses/msmarco_kaggle_license.txt)  
- **SHA256 Checksum (working sample):** DBA7A99764EC589E5A4276F23EADC5C8FA32E1ECEE8ACF80246E281C48F3ED0A

### Notes
- This is a small sampled subset for experimentation.  
- The original MS MARCO dataset is licensed differently (Microsoft Research License, non-commercial).  
- Only non-sensitive, public data was used.

## MS MARCO — dev queries (sanitized sample)
- **Kaggle slug:** manupande21111997/ms-marco-queries-dev  
- **Original filename (not committed):** data/queries.dev.tsv  
- **Sanitized sample (committed):** data/msmarco_queries_showcase.csv  
- **Downloaded on (UTC):** 2025-09-13  
- **Sampling method:** TSV chunk sampling (`scripts/sample_msmarco_queries_tsv.py`), deterministic `seed=42`  
- **Sanitization:** redacted emails/IPs/phone-like sequences; truncated to 200 chars (`scripts/fix_and_sanitize_queries.py`)  
- **SHA256 checksum (showcase):** 2DBA83BAE1CD2E52322D83B2FDAA8A56847DEA9D69424D2DC3AB7F32AB6E0335  
- **License file:** docs/licenses/msmarco_kaggle_license.txt  
- **Notes:** Raw large file retained off-repo. Sanitization applied only to textual query column; numeric IDs retained in `query_id`.

## Wikimedia — Pageviews (1 month)
- **File (local full):** data/wikimedia_pageviews_1month.csv  (DO NOT COMMIT: full raw dataset)
- **Showcase (committed):** data/wikimedia_pageviews_sample.csv    15-row sample of daily pageview counts (Aug 2025). Source: Wikimedia REST API.
- **Source:** Wikimedia Pageviews REST API (script: `scripts/fetch_wikimedia_pageviews.py`)  
- **Period:** 2025-08-01 → 2025-08-31  
- **SHA256 checksum (showcase):** E85ADAF01D0C892CA96C20AAA6AC6B1477043F413413C4A3CD7301D6E24A799A  
- **Notes:** Full file retained locally and excluded from Git. The showcase contains a small subset (≤20 rows) for reviewers.

## Google Trends — Top keywords / timeseries
- **File (local full):** data/google_trends_timeseries.parquet / data/google_trends_top50.csv (local)  
- **Showcase (committed):** data/google_trends_sample.csv     15-row sample of top search queries. Source: Google Trends (via pytrends).
- **Source & script:** `scripts/fetch_google_trends_top50.py` (pytrends)  
- **Period:** 2025-08-01 → 2025-08-31  
- **SHA256 checksum (showcase):** 72D5F99EC1174073C8961C053770BFBFE2193FC55E7C742C1C9CAF9A72D4F5DE  
- **Notes:** Full timeseries stored locally as Parquet; showcase CSV is a small, readable sample for reviewers.

## General notes
- Raw and large datasets are intentionally **excluded** from the repository (see `.gitignore`) to keep the repo lightweight and to avoid exposing sensitive or licensed data.  
- To reproduce any full dataset locally, run the corresponding script in `scripts/` and consult `docs/licenses/` for legal terms.
