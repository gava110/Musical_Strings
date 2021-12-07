#per fare la prova: "the Beatles" "Yesterday" "John Lennon" "Imagine"
#per fare la prova: "Beatles" "Yesterday" "Vasco rossi" "vivere"
import nltk
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
from removal_code import stopremoval
from stemlem import stemming
from stemlem import lemmatization
from jaccard_code import jsimilarity
from intersection_code import intersection

parser = ap.ArgumentParser()
parser.add_argument("artist1", help="First artist", type= str)
parser.add_argument("song1", help="Song of the first artist", type= str)
parser.add_argument("artist2", help="Second artist", type= str)
parser.add_argument("song2", help="Song of the Second artist", type= str)
parser.add_argument("-p", "--preference", help="enter similarity method preference",
					default="jaccard",choices= ["jaccard","intersection"],type=str)
args = parser.parse_args()


artist1=args.artist1
song1=args.song1
artist2=args.artist2
song2=args.song2
preference= args.preference

try:
	text1= get_lyric(artist1, song1)
except KeyError:
	print ("{} - {} not found".format(artist1,song1))
try :
	text2= get_lyric(artist2, song2)
except KeyError:
	print ("{} - {} not found".format(artist2,song2))

#control that artist and song is within top 500

top500 = pandas.read_csv("Top 500 Songs.csv", encoding= 'Latin 1')
top500 = top500[["artist", "title"]]



if artitle_check(artist1,song1,top500) == False:
	print ("your FIST artist is not on Top 500 songs")
if artitle_check(artist2,song2,top500) == False:
	print ("your SECOND artist is not on Top 500 songs")

#remove stopwords



filtered1 = stopremoval(text1)
filtered2 = stopremoval(text2)

#stemmisation of the two songs



stem1 = stemming (filtered1)
stem2 = stemming ( filtered2)

#lemmatization of the two songs



lem1 = lemmatization(filtered1)
lem2 = lemmatization(filtered2)



if preference== "jaccard":
#jaccard similarity for stemmisation

	similarity_s= jsimilarity(stem1,stem2)

	#jaccard similarity for lemmatisation

	similarity_l= jsimilarity(lem1,lem2)

	print ("{} by {} and {} by {} are similar according to stemmatisation by {}% and according to lemmatisation by {}%".format(song1,artist1,song2,artist2 ,round (similarity_s*100,2),round( similarity_l*100,2)))

#intersection similarity



if preference=="intersection":
#by stemmisation
	inter_s= intersection(stem1, stem2)
	print ( "number of intersection by lemmatisation is {}".format(inter_l) )
	#by lemmatisation
	inter_l= intersection(lem1, lem2)
	print ( "number of intersection by lemmatisation is {}".format(inter_l) )













