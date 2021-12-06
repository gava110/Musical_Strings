#!/usr/bin/env python
# coding: utf-8

# In[57]:


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
  
def stemming (songs):
    
    ps = PorterStemmer()
    
    #creating a list for stemmed words
    stemmed_songs = []
    
    #applying the algorithm
    for w in songs:
        stemmed_songs.append(ps.stem(w))
    return stemmed_songs


# In[59]:


from nltk.stem import WordNetLemmatizer

def lemmatization (songs):
    
    lemmatizer = WordNetLemmatizer()
    lemmatized_songs = []
    
    for w in songs:
        lemmatized_songs.append(lemmatizer.lemmatize(w))
    
    return lemmatized_songs

