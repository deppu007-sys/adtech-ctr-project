import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Ad": ["Ad_A", "Ad_B", "Ad_C", "Ad_D"],
    "Impressions": [1000, 1500, 1200, 900],
    "Clicks": [50, 90, 40, 30]
}

df = pd.DataFrame(data)

# Calculate CTR
df["CTR"] = df["Clicks"] / df["Impressions"]

print(df)

# Best performing ad
best_ad = df.loc[df["CTR"].idxmax()]
print("\nBest Performing Ad:")
print(best_ad)

# Ranking ads
ranking = df.sort_values(by="CTR", ascending=False)
print("\nAd Ranking:")
print(ranking)

# Plot
plt.bar(df["Ad"], df["CTR"])
plt.xlabel("Ads")
plt.ylabel("CTR")
plt.title("Ad CTR Comparison")
plt.show()

# Function
def calculate_ctr(impressions, clicks):
    return clicks / impressions

print("\nCTR for custom input:", calculate_ctr(2000, 120))
