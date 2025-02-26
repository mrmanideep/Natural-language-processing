import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger, UnigramTagger
from nltk.corpus import treebank

nltk.download('punkt')
nltk.download('treebank')

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

if __name__ == "__main__":
    text = "NLTK is a powerful library for text processing."
    tagged_text = transformation_based_tagging(text)
    
    print("Transformation-Based POS Tagged Text:")
    for word, tag in tagged_text:
        print(f"{word}: {tag}")
