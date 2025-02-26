import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

def perform_morphological_analysis(text):
    """
    Performs morphological analysis on the given text using NLTK.

    Args:
        text (str): The input text to analyze.

    Returns:
        list: A list of tuples, where each tuple contains the original word and its lemma.
    """

    # Tokenize the text into words
    tokens = word_tokenize(text)

    # Initialize the WordNet Lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Perform lemmatization on each token
    lemmas = [(token, lemmatizer.lemmatize(token)) for token in tokens]

    return lemmas

# Example usage:
text = "The runners are running quickly."
analysis_result = perform_morphological_analysis(text)

# Print the results
for word, lemma in analysis_result:
    print(f"Word: {word}, Lemma: {lemma}")
