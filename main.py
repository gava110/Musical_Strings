import argparse as ap

parser = ap.ArgumentParser()
parser.add_argument("artist1", help="First artist", type= str)
parser.add_argument("song1", help="Song of the first artist", type= str)
parser.add_argument("artist2", help="Second artist", type= str)
parser.add_argument("song2", help="Song of the Second artist", type= str)
args = parser.parse_args()
artist1=args.artist1
song1=args.song1
artist2=args.artist2
song2=args.song2

from lyrics import get_lyric

try:
	text1= get_lyric(artist1, song1)
except KeyError:
	print ("{} - {} not found".format(artist1,song1))
try :
	text2= get_lyric(artist2, song2)
except KeyError:
	print ("{} - {} not found".format(artist2,song2))