import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["running", "jumps", "easily", "studies", "flying", "happiness", "arguing"]

stemmed_words = [stemmer.stem(word) for word in words]

print("Original Words:", words)
print("Stemmed Words:", stemmed_words)
