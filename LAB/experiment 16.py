# Experiment 16: Word Frequency Distribution in Customer Reviews
# Description: Load customer reviews dataset using Pandas, clean and tokenize review texts,
#              and compute the overall word frequency distribution across all reviews.

import pandas as pd
import string
from collections import Counter

# Load customer reviews
df = pd.read_csv("customer_reviews.csv")

# Combine all reviews into a single text
all_reviews_text = " ".join(df["Review_Text"])

# Preprocess: lowercase and remove punctuation
cleaned_text = all_reviews_text.lower().translate(str.maketrans("", "", string.punctuation))
words = cleaned_text.split()

# Compute word frequencies
word_freq = Counter(words)

# Display results
print("Word Frequency Distribution in Customer Reviews:")
print("-" * 35)
print(f"{'Word':<18} {'Frequency':<10}")
print("-" * 35)
for word, count in word_freq.most_common():
    print(f"{word:<18} {count:<10}")

print(f"\nTotal Words in Reviews: {len(words)}")
print(f"Unique Words: {len(word_freq)}")
