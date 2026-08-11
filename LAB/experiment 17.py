# Experiment 17: Customer Feedback Word Frequency & Visualization
# Description: Load customer feedback from data.csv, preprocess text (remove punctuation,
#              convert to lowercase, remove stopwords), calculate word frequency distribution,
#              display top N frequent words, and visualize them using a Matplotlib bar graph.

import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

# Define common English stop words
STOP_WORDS = {
    "the", "and", "is", "a", "an", "in", "to", "of", "for", "with", "on", "at", "by", 
    "from", "this", "that", "it", "my", "i", "we", "you", "was", "were", "be", "been", 
    "have", "has", "had", "do", "does", "did", "but", "so", "as", "if", "or", "because", 
    "not", "very", "too", "also", "will", "can"
}

# 1. Load dataset
df = pd.read_csv("data.csv")

# 2. Preprocess text data
all_feedback = " ".join(df["feedback"].astype(str))
cleaned_text = all_feedback.lower().translate(str.maketrans("", "", string.punctuation))
all_words = cleaned_text.split()

# Filter out stop words
filtered_words = [word for word in all_words if word not in STOP_WORDS and len(word) > 1]

# 3. Calculate frequency distribution
word_counts = Counter(filtered_words)

# 4. Display top N most frequent words (N can be configured or input)
N = 10
top_n_words = word_counts.most_common(N)

print(f"Top {N} Most Frequent Words in Customer Feedback:")
print("-" * 35)
print(f"{'Word':<18} {'Frequency':<10}")
print("-" * 35)
for word, freq in top_n_words:
    print(f"{word:<18} {freq:<10}")

# 5. Plot a bar graph
words_list = [item[0] for item in top_n_words]
freqs_list = [item[1] for item in top_n_words]

plt.figure(figsize=(10, 5))
plt.bar(words_list, freqs_list, color='royalblue', edgecolor='black')
plt.title(f"Top {N} Most Frequent Words in Customer Feedback")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("outputs/experiment 17_word_freq_bar.png")
plt.close()

print(f"\nBar graph of top {N} words saved to outputs/experiment 17_word_freq_bar.png")
