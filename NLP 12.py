import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger, UnigramTagger
from nltk.corpus import treebank
from nltk.parse import EarleyChartParser

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('treebank')
nltk.download('averaged_perceptron_tagger')

# Define regex-based tagging patterns
patterns = [
    (r'^[A-Z][a-z]+$', 'NNP'),  # Proper nouns
    (r'^[a-z]+ing$', 'VBG'),  # Gerunds
    (r'^[a-z]+ed$', 'VBD'),  # Past tense verbs
    (r'^[a-z]+ly$', 'RB'),  # Adverbs
    (r'^[a-z]+s$', 'NNS'),  # Plural nouns
    (r'^[0-9]+$', 'CD'),  # Numbers
    (r'.*', 'NN')  # Default to noun
]

# Create a regex-based tagger
regex_tagger = RegexpTagger(patterns)

# Train a unigram tagger using a portion of the treebank corpus
train_sents = treebank.tagged_sents()[:2000]
unigram_tagger = UnigramTagger(train_sents, backoff=regex_tagger)

def transformation_based_tagging(text):
    words = word_tokenize(text)
    return unigram_tagger.tag(words)

# Define a simple context-free grammar (CFG)
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> DT NN | PRP
    VP -> VB NP | VB
    DT -> 'the'
    NN -> 'dog' | 'cat'
    PRP -> 'he' | 'she'
    VB -> 'chased' | 'slept'
""")

# Create an Earley parser
parser = EarleyChartParser(grammar)

def parse_sentence(sentence):
    words = word_tokenize(sentence)
    print("Parsing Tree:")
    for tree in parser.parse(words):
        print(tree)

if __name__ == "__main__":
    text = "NLTK is a powerful library for text processing."
    tagged_text = transformation_based_tagging(text)
    
    print("Transformation-Based POS Tagged Text:")
    for word, tag in tagged_text:
        print(f"{word}: {tag}")
    
    sentence = "the dog chased the cat"
    parse_sentence(sentence)
