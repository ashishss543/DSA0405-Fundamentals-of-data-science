# Experiment 15: Frequency Distribution of Social Media Likes
# Description: Load user interaction dataset using Pandas, calculate frequency distribution of likes,
#              and analyze the distribution of post engagements.

import pandas as pd

# Load social media interaction dataset
df = pd.read_csv("social_media_interactions.csv")

# Calculate frequency distribution of likes
likes_frequency = df["Likes"].value_counts().sort_index()

# Display frequency distribution
print("Frequency Distribution of Likes Among Posts:")
print(likes_frequency)

# Summary of likes distribution
print("\nDetailed Summary:")
print(f"Total Posts Analyzed: {len(df)}")
print(f"Mean Likes per Post: {df['Likes'].mean():.2f}")
print(f"Most Frequent Likes Count (Mode): {df['Likes'].mode().values[0]}")
