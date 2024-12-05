"""
Word Occurrence Counter Program
Estimate:20 minute
Actual:28 minute
"""

text = input("Text: ")

word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

max_length = max(len(word) for word in word_counts)

for word in sorted(word_counts):
    print(f"{word:{max_length}} : {word_counts[word]}")
