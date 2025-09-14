import pandas as pd, os
os.makedirs("data", exist_ok=True)

src = "data/wikimedia_pageviews_1month.csv"
out = "data/wikimedia_pageviews_sample.csv"

df = pd.read_csv(src, dtype=str)
df_show = df.head(15)   # just first 15 rows
df_show.to_csv(out, index=False)

print(f"Created {out} with {len(df_show)} rows")
