#Import modules for stopwords removal
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Import modules for automated language recognition 
from langdetect import detect
import iso639

def stopremoval (song):

    #Detect lyrics' language and convert language ISO639 code into plain text 
    language = detect(song)
    lang=iso639.to_name(language)
    
    #Define language specific stopwords to be removed from retrieved lyrics
    stop_words = set(stopwords.words(lang))

    #Turn all words inside lyrics in lowercase and split them into tokens
    song=song.lower()
    word_tokens = word_tokenize(song)

    #Filter song eliminating stopwords  
    filtered_song = []
    for words in word_tokens:
    
        if words not in stop_words:
    
            filtered_song.append(words)
        
    return filtered_song
    