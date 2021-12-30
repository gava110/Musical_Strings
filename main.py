"""
The aim of the project is to performe the similarity between two of the best 500 songs in history.
User should enter one pair of artist and song, and eventually make explicit the similarity method to peform.
This is the main code of the software. In this code we combine all function within different modules
in order to performe the software aim.

"""
import nltk
nltk.download('omw-1.4',quiet=True)
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from langdetect import detect
import iso639
import argparse as ap
import pandas
from lyrics import get_lyric
from check import artitle_check
from stopwords import stopremoval
from stemlem import lemmatization
from jaccard import jsimilarity
from intersection import intersection
import requests
import json
import copy

"""
This part of the main code, get the informations from the user through argparse method.
Two songs and relative artists are positional string arguments, in other words, without
these two entries, the software does not work.
Preference (abbreviate with -p) is optional argument required to the user. It could be
"jaccard" or "intersection", if is not specified, defoult value is "jaccard".

"""


parser = ap.ArgumentParser()
parser.add_argument("artist1", help="First artist", type=str)
parser.add_argument("title1", help="Song of the first artist", type=str)
parser.add_argument("artist2", help="Second artist", type=str)
parser.add_argument("title2", help="Song of the Second artist", type=str)
parser.add_argument(
    "-p",
    "--preference",
    help="Enter similarity method preference",
    default="jaccard",
    choices=[
        "jaccard",
        "intersection"],
    type=str)
args = parser.parse_args()


# rename preference entries
preference = args.preference


"""
Try and expect method allows to return "not found" statement in case of "KeyError".
If the one of the song is not found by the API (inside lyrics module), code retun "KeyError"
and statement is printed. If the process does not produce errors, it store the two lyrics.

"""


try:
    get_lyric(args.artist1, args.title1)
except KeyError:
    print("{} - {} not found".format(args.artist1, args.title1))
try:
    get_lyric(args.artist2, args.title2)
except KeyError:
    print("{} - {} not found".format(args.artist2, args.title2))
"""
We upload "Top 500 Songs.csv" to have list of best 500 songs in history.
Then all columns, exept for "artist" and "title", are dropped as the code does
not use them.

"""

"""
Define the class "Song" with attributes Artist, title and lyric.

"""


class song:
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.lyric = get_lyric(artist, title)


# trasform our inputs into objects
song1 = song(args.artist1, args.title1)
song2 = song(args.artist2, args.title2)


#upload Top500 csv
top500 = pandas.read_csv("Top 500 Songs.csv", encoding='Latin 1')
top500 = top500[["artist", "title"]]


# Check if the two songs are in top 500 dataset through "check" module.
if artitle_check(
        song1.__dict__["artist"],
        song1.__dict__["title"],
        top500) == False:
    print("{} by {} is not in Top 500 songs".format(
        song1.__dict__["title"], song1.__dict__["artist"]))
    exit()
if artitle_check(
        song2.__dict__["artist"],
        song2.__dict__["title"],
        top500) == False:
    print("{} by {} is not in Top 500 songs".format(
        song2.__dict__["title"], song2.__dict__["artist"]))
    exit()


# Remove stopwords and punctuation through "stopwords" module.
filtered1 = stopremoval(song1.__dict__["lyric"])
filtered2 = stopremoval(song2.__dict__["lyric"])


# Store lemmatised list of strings
lem1 = lemmatization(filtered1)
lem2 = lemmatization(filtered2)


if preference == "jaccard":

    # Perform jaccard similarity through "jaccard" module.
    similarity_l = jsimilarity(lem1, lem2)

    print(
        "{} by {} and {} by {} are similar  according to lemmatization by {}%".format(
            song1.__dict__["title"],
            song1.__dict__["artist"],
            song2.__dict__["title"],
            song2.__dict__["artist"],
            round(
                similarity_l * 100,
                2)))


if preference == "intersection":

    # Intersection of set thorough "intersection module"
    inter_l = intersection(lem1, lem2)
    print("Number of intersections by lemmatization is {}".format(inter_l))
