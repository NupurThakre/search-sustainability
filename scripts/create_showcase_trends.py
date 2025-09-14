import pandas as pd, os
os.makedirs("data", exist_ok=True)

src = "data/google_trends_top50.csv"  # adjust if you saved with another name
out = "data/google_trends_sample.csv"

df = pd.read_csv(src, dtype=str)
df_show = df.head(15)
df_show.to_csv(out, index=False)

print(f"Created {out} with {len(df_show)} rows")
