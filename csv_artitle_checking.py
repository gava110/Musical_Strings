import pandas

#Create a pandas dataframe from  Top 500 Songs.csv and select just artist and song title
top500 = pandas.read_csv("Top 500 Songs.csv", encoding= 'Latin 1')
top500 = top500[["artist", "title"]]

#Turn all vlaues in the newly created top500 dataframe lowercase
for i in range (len(top500)):
    top500["artist"][i]=top500["artist"][i].lower()
    top500["title"][i]=top500["title"][i].lower()

def artitle_check(artist, title):
    #Makes sure any input from user is turned lowercase
    artist= str(artist).lower()
    title=str(title).lower()
    
    #Search for inputted artist and return True if it is inside top500
    if artist in top500["artist"].tolist():
        return True
    return False
    
    #Search for inputted song title and return True if it is inside top500
    if title in top500["title"].tolist():
        return True
    return False