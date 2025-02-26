import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger, UnigramTagger
from nltk.corpus import treebank
from nltk.parse import ViterbiParser
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('treebank')
nltk.download('averaged_perceptron_tagger')

patterns = [
    (r'^[A-Z][a-z]+$', 'NNP'),  
    (r'^[a-z]+ing$', 'VBG'),  
    (r'^[a-z]+ed$', 'VBD'),  
    (r'^[a-z]+ly$', 'RB'),  
    (r'^[a-z]+s$', 'NNS'),  
    (r'^[0-9]+$', 'CD'),  
    (r'.*', 'NN')  
]

regex_tagger = RegexpTagger(patterns)

train_sents = treebank.tagged_sents()[:2000]
unigram_tagger = UnigramTagger(train_sents, backoff=regex_tagger)

def transformation_based_tagging(text):
    words = word_tokenize(text)
    return unigram_tagger.tag(words)

grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> DT NN [0.5] | PRP [0.5]
    VP -> VB NP [0.7] | VB [0.3]
    DT -> 'the' [1.0]
    NN -> 'dog' [0.5] | 'cat' [0.5]
    PRP -> 'he' [0.5] | 'she' [0.5]
    VB -> 'chased' [0.6] | 'slept' [0.4]
""")

parser = ViterbiParser(grammar)

def parse_sentence(sentence):
    words = word_tokenize(sentence)
    print("Parsing Tree:")
    for tree in parser.parse(words):
        print(tree)
        tree.pretty_print()
        tree.draw()

def check_agreement(sentence):
    words = word_tokenize(sentence)
    tagged_words = unigram_tagger.tag(words)
    
    for i in range(len(tagged_words) - 1):
        word, tag = tagged_words[i]
        next_word, next_tag = tagged_words[i + 1]
        
        if tag == 'DT' and next_tag == 'NNS':
            print(f"Agreement error: '{word} {next_word}' should match in number.")
        elif tag == 'PRP' and next_tag == 'VB':
            print(f"Agreement error: Pronoun '{word}' may require verb conjugation.")

if __name__ == "__main__":
    text = "NLTK is a powerful library for text processing."
    tagged_text = transformation_based_tagging(text)
    
    print("Transformation-Based POS Tagged Text:")
    for word, tag in tagged_text:
        print(f"{word}: {tag}")
    
    sentence = "the dog chased the cat"
    parse_sentence(sentence)
    check_agreement(sentence)
