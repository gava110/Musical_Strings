"""
In this part of the code we created the function that accepts
songs retrived from the API as inputs,recognizes their language,
and removes stopwords accordingly, outputting a list of tokenized
words to be fed to the text similarity analysis processes

"""

# Import modules for lyrics tokenization and stopwords removal
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Import modules for language recognition and iso639 langcode convertion
from langdetect import detect
import iso639


def stopremoval(song):

    # Detect retrieved lyrics' language and convert ISO639 code into text
    language = detect(song)
    lang = iso639.to_name(language)

    # Define extra stopwords that might not be recognized by nltk
    extra_stopwords = ["'m", "'s", "'re", "n't",
                       "'ve", "'d", "'ll", "oh", "ah", "eh", "uh",
                       "paroles", "de", "la", "chanson"]

    # Apply converted iso639 code to define language specific stopwords
    stop_words = set((stopwords.words(lang.lower())) +
                     list(string.punctuation)+extra_stopwords)

    # Turn all words inside lyrics in lowercase and tokenize them
    song = song.lower()
    word_tokens = word_tokenize(song)

    # Eliminate defined stopwords from tokens and add them to a list
    filtered_song = []
    for words in word_tokens:

        if words not in stop_words:

            filtered_song.append(words)

    return filtered_song
