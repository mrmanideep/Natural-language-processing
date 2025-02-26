import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from collections import defaultdict
import random

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('treebank')

tagged_sentences = nltk.corpus.treebank.tagged_sents()
word_tag_freq = defaultdict(lambda: defaultdict(int))

def train_pos_tagger():
    for sentence in tagged_sentences:
        for word, tag in sentence:
            word_tag_freq[word.lower()][tag] += 1

def stochastic_pos_tagging(text):
    words = word_tokenize(text)
    tagged_words = []
    
    for word in words:
        tag_freq = word_tag_freq[word.lower()]
        if tag_freq:
            tag = max(tag_freq, key=tag_freq.get)
        else:
            tag = random.choice(list(word_tag_freq[random.choice(list(word_tag_freq.keys()))].keys()))
        tagged_words.append((word, tag))
    
    return tagged_words

if __name__ == "__main__":
    train_pos_tagger()
    text = "NLTK is a powerful library for text processing."
    tagged_text = stochastic_pos_tagging(text)
    
    print("Stochastic POS Tagged Text:")
    for word, tag in tagged_text:
        print(f"{word}: {tag}")
