
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required packages
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Get sentence from user
sentence = input("Enter a sentence: ")

# Tokenization
words = word_tokenize(sentence)

print("\nTokenized Words:")
print(words)

# Part of Speech Tagging
tags = pos_tag(words)

print("\nParts of Speech:")
for word, tag in tags:
    print(word, "->", tag)
