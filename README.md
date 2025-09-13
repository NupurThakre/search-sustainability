# Search Sustainability — Detecting Energy-Intensive Queries

**Owner:** Nupur Thakre  

**Purpose:** This repository is a scaffold for analyzing energy-intensive query patterns in search systems. It includes data, notebooks, SQL models, and dashboards aimed at quantifying per-query energy consumption, identifying high-impact cohorts, and proposing optimization strategies.  



## Repository Structure

search-sustainability/
├── data/
│ └── wikimedia_pageviews_sample.csv # 15-row sanitized sample
├── docs/
│ ├── assumptions.md 
│ ├── charter.md # project charter
│ └── data_inventory.md # datasets overview
├── notebooks/
│ └── eda_notebook.ipynb # exploratory data analysis
├── scripts/
│ └── fetch_wikimedia_pageviews.py # fetch pageviews from Wikimedia API
└── README.md


## Data Management Policy

- **Raw data** (large/full datasets) is **excluded** from Git for efficiency.  
- **Sample data** (e.g., `data/wikimedia_pageviews_sample.csv`) is committed to help reviewers and recruiters quickly test workflows.  
- To regenerate the full dataset, run:

```bash
python scripts/fetch_wikimedia_pageviews.py



See [/docs](./docs) for detailed project charter and assumptions.