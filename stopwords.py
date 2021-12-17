"""
In this part of the code we created the function that accepts songs retrived from the API as inputs, 
recognizes their language, and removes stopwords accordingly, outputting a list of tokenized 
words to be fed to the text similarity analysis processes

"""

# Import modules for lyrics tokenization and stopwords removal
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Import modules for automated language recognition and iso639 langcode convertion
from langdetect import detect
import iso639


def stopremoval(song):

    # Detect retrieved lyrics' language and convert ISO639 code into plain text
    language = detect(song)
    lang = iso639.to_name(language)

    
    # Define language specific stopwords + extra ones that might not be properly recognized by nltk
    extra_stopwords = ["'m", "'s", "'re", "n't",
                       "'ve", "'d", "'ll", "oh", "ah", "eh", "uh", "paroles", "de", "la", "chanson"]
    
    # Apply detected languages' converted iso639 code to remove language specific stopwords
    stop_words = set((stopwords.words(lang)) +
                     list(string.punctuation)+extra_stopwords)

    # Turn all words inside lyrics in lowercase and split them into tokens
    song = song.lower()
    word_tokens = word_tokenize(song)

    # Filter song eliminating the defined stopwords from tokens and add them to a list
    filtered_song = []
    for words in word_tokens:

        if words not in stop_words:

            filtered_song.append(words)

    return filtered_song