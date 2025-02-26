import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

nltk.download('punkt')

patterns = [
    (r'^[A-Z][a-z]+$', 'NNP'),  
    (r'^[a-z]+ing$', 'VBG'),  
    (r'^[a-z]+ed$', 'VBD'),  
    (r'^[a-z]+ly$', 'RB'),  
    (r'^[a-z]+s$', 'NNS'),  
    (r'^[0-9]+$', 'CD'),  
    (r'.*', 'NN')  
]

tag_regexp = RegexpTagger(patterns)

def regex_pos_tagging(text):
    words = word_tokenize(text)
    return tag_regexp.tag(words)

if __name__ == "__main__":
    text = "NLTK is a powerful library for text processing."
    tagged_text = regex_pos_tagging(text)
    
    print("Rule-Based POS Tagged Text:")
    for word, tag in tagged_text:
        print(f"{word}: {tag}")
