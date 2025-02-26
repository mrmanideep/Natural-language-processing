import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    words = word_tokenize(text)
    
    tagged_words = pos_tag(words)
    
    return tagged_words

if __name__ == "__main__":
    text = "NLTK is a powerful library for text processing."
    tagged_text = pos_tagging(text)
    
    print("POS Tagged Text:")
    for word, tag in tagged_text:
        print(f"{word}: {tag}")
