#!/usr/bin/env python
# coding: utf-8

# ## Stemming 

# In[40]:


#Getting the info about the song chosen
get_song= (get_lyric(artist1, song1))
#print(canzone.split())


# In[42]:


from textblob import TextBlob
#Applying the stemming function 
song_stem = sorted(set(TextBlob(get_song).lower().words.stem()))
#song_stem


# In[43]:


get_song2= (get_lyric(artist2, song2))
#print(canzone.split())


# In[46]:


song_stem2 = sorted(set(TextBlob(get_song2).lower().words.stem()))
#song_stem2


# In[47]:


#Add Jaccard Similarity


# ## Lemmatization

# In[50]:


#Applying the lemmatisation function
song_lemm = sorted(set(TextBlob(get_song).lower().words.lemmatize()))
#song_lemm


# In[53]:


song_lemm2 = sorted(set(TextBlob(get_song2).lower().words.lemmatize()))
#song_lemm2


# In[ ]:




