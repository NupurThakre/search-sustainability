### **Project Charter**



#### **Project Title: Search Sustainability — Detecting Energy-Intensive Queries**

#### **Owner: Nupur Thakre**



**Problem Statement**
Google's commitment to being carbon-free by 2030 requires understanding and optimizing the energy consumption of its core products. A key challenge is identifying which user query patterns and system behaviors drive disproportionate energy usage and then developing solutions to reduce this carbon footprint without degrading the user experience.



###### **Goals**

• Quantify a baseline for energy consumption per query, categorizing by query type (e.g., text, image, video).
• Identify top 3 query cohorts driving the majority (>70–80%) of potential savings.
• Propose 3 feasible, data-backed strategic fixes (e.g., improved caching, bot traffic throttling, autocomplete optimization).



###### **Scope**

**In Scope:** Analyzing publicly available datasets related to search trends (Google Trends, Wikipedia logs, Kaggle data) to simulate and model energy consumption per query. The project will include data cleaning, SQL modeling, exploratory data analysis, and the creation of a dashboard to visualize insights and potential savings.
**Out of Scope:** Accessing or using any internal Google proprietary data, live user data, or production code. The project will not involve implementing or deploying any proposed fixes within a live system.



###### **Success Metrics (KPIs)**

• **Energy Model Accuracy:** Model approximates relative energy cost of query types within ±10% of benchmark assumptions.
• **Top Cohort Identification:** The clear identification of at least 3 distinct, high-impact query cohorts.
• **Savings Quantification:** The ability to quantify the estimated annual energy savings in kilowatt-hours (kWh) and corresponding carbon reduction (CO₂) for each proposed fix.
• **Dashboard Completion:** A fully functional dashboard that visualizes key insights and allows for interactive analysis of potential optimizations.
• **Delivery:** Final recommendations and dashboard will be delivered within 4 weeks



###### **Data Sources**

• Google Trends: Publicly accessible search interest data (via website).
• Wikipedia Traffic Statistics: Open-source logs for pageview data (available via API or public dataset).
• Kaggle Datasets: Various search-related datasets available on the Kaggle platform (downloadable).
• Open Energy Benchmarks: Public reports from data center organizations or research papers on server power usage and PUE (Power Usage Effectiveness) values (research via Google Scholar or industry reports).



###### **Assumptions**

• **Server Power:** Baseline per-query consumption assumed at 0.0003 kWh (per published research).
• **PUE (Power Usage Effectiveness):** An assumed PUE value for a typical data center, such as 1.1, to account for overhead power consumption.
• **Carbon Intensity:** Regional average of 0.3 kg CO₂/kWh for converting energy savings into carbon reductions.
• **Data Proxies:** Wikipedia traffic and other public datasets are valid proxies for search interest and behavior.



###### **Timeline / Milestones**

• **Part 1:** Project Charter + Cleaned Dataset + Initial Hypotheses. This includes drafting and committing the charter, collecting and cleaning initial datasets, and performing initial analysis to form hypotheses.
• **Part 2:** SQL Models + Clustering/Forecasts + Interactive Dashboard (prototype). This involves building the SQL models, running advanced analyses (clustering, forecasting), and developing the interactive dashboard.
• **Part 3:** Final Analysis Report + Business Impact Summary + Presentation Deck. This milestone focuses on finalizing the analysis, quantifying the business impact, and preparing the final presentation and report.

