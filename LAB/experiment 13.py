# Experiment 13: Word Frequency Distribution in Text Document
# Description: Read sample text document, clean and tokenize words, 
#              and calculate the frequency distribution of words using collections.Counter.

import string
from collections import Counter

# Read text from file
with open("sample_text.txt", "r") as file:
    text = file.read()

# Preprocess text: lowercase and remove punctuation
cleaned_text = text.lower().translate(str.maketrans("", "", string.punctuation))
words = cleaned_text.split()

# Calculate frequency distribution of words
word_freq = Counter(words)

# Display results
print("Word Frequency Distribution:")
print("-" * 35)
print(f"{'Word':<18} {'Frequency':<10}")
print("-" * 35)
for word, freq in word_freq.most_common():
    print(f"{word:<18} {freq:<10}")

print(f"\nTotal words: {len(words)}")
print(f"Unique words: {len(word_freq)}")
