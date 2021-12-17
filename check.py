def artitle_check(artist, title,file):
    #Makes sure any input from user is turned lowercase
    #Turn all vlaues in the newly created file dataframe lowercase
    for i in range (len(file)):
        file["artist"][i]=file["artist"][i].lower()
        file["title"][i]=file["title"][i].lower()

    artist= str(artist).lower()
    title=str(title).lower()
    
    #Search for inputted artist and return True if it is inside file
    if artist in file["artist"].tolist():
        return True
    return False
    
    #Search for inputted song title and return True if it is inside file
    if title in file["title"].tolist():
        return True
    return False