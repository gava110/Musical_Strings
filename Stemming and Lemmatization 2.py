#!/usr/bin/env python
# coding: utf-8

# ## Stemming 

#Getting the info about the song chosen
get_song= (get_lyric(artist1, song1))
#print(canzone.split())

from textblob import TextBlob
#Applying the stemming function 
song_stem = sorted(set(TextBlob(get_song).lower().words.stem()))
#song_stem

get_song2= (get_lyric(artist2, song2))
#print(canzone.split())

song_stem2 = sorted(set(TextBlob(get_song2).lower().words.stem()))
#song_stem2


# ## Lemmatization

#Applying the lemmatisation function
song_lemm = sorted(set(TextBlob(get_song).lower().words.lemmatize()))
#song_lemm

song_lemm2 = sorted(set(TextBlob(get_song2).lower().words.lemmatize()))
#song_lemm2

#Add Jaccard Similarity here 
