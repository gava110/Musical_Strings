#Import module for stopwords removal 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def stopremoval (song, language):
#Define language specific stopwords to remove from retrieved lyrics
    stop_words = set(stopwords.words(language)


    ​#Turn all words inside lyrics in lowercase and split them into tokens
    song=song.lower()
    word_tokens = word_tokenize(song)

    #Filter song eliminating stopwords  
    filtered_song = []
    for words in word_tokens:
    
        if words not in stop_words:
    
            filtered_song.append(words)
        
    return filtered_song
        