"""
In this part of the code we create two functions to apply stemming and lemmatization methods to the
two songs chosen by the user. Stemming is the process of producing morphological variants of a root/
base word. Lemmatization is the process of grouping together the different inflected forms of a word
so they can be analyzed as a single item. This is necessary to then apply jaccard similarity, which
will return to the user the similarity percentage between two songs.

"""
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer


def stemming(songs):
    """
    This function removes the morphological affixes from words, leaving only the word stem.
    The implementation uses NLTK (the Natural Language Toolkit -- a suite of open source
    Python module).
    """
    porter_stemmer = PorterStemmer()
    # creating a list for stemmed words
    stemmed_songs = []
    # applying the algorithm
    for words in songs:
        stemmed_songs.append(porter_stemmer.stem(words))
    return stemmed_songs


def lemmatization(songs):
    """
    This function aims to remove inflectional endings from the texts of the songs.
    Also here NLTK was used.
    """
    lemmatizer = WordNetLemmatizer()
    #creating lists of lemmatized words
    lemmatized_songs = []
    for words in songs:
        lemmatized_songs.append(lemmatizer.lemmatize(words))
    return lemmatized_songs
  
