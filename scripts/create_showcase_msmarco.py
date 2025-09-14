import pandas as pd, os
os.makedirs("data", exist_ok=True)

src = "data/msmarco_queries_sample_sanitized.csv"
out = "data/msmarco_queries_showcase.csv"

df = pd.read_csv(src, dtype=str)
df_show = df.sample(n=15, random_state=42)  # pick 15 rows
df_show.to_csv(out, index=False)

print(f"Created {out} with {len(df_show)} rows")
