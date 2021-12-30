## Musical_Strings
LSPD - Project Repository 
Musical_Strings is a project that takes user’s inputs from the machine terminal, checks whether or not the songs are part of the “Top 500 of history” csv file and, if that is the case it retrieves the texts from an API to perform the percentage or absolute value of similarity between the two.

## Installation
Use the command git clone https://github.com/gava110/Musical_Strings.git in the command prompt of your PC to automatically download the whole folder containing the modules. Git should have been previously installed.
The required libraries to run our project on the terminal are: 
- nltk
- langdetect
- iso639
- Pandas
- Numpy
- Request
- json
- Copy

For example:
```bash 
pip install nltk
```

### Nltk
If some particular package not included is required to go forward in the project, you should write this line of code in the terminal:
```bash
Python3 -m nltk.downloader all
```
  
## Usage
The aim of the project is to perform the similarity between two of the best 500 songs in history.
Once two pairs of “Artist” and “Song” are entered, the program performs the similarity between the lyrics. 
The functions Get lyrics, Article_check, Stop removal, Lemmatization, Jsimilarity and Instruction are all stored in their respective modules and recalled in the main code. ArgParse stores the user inputs and then main.py performs the process.

In order to run the program, the command should be written as follows:
```bash
Python3 main.py “artist1” “song1” “artist2” “song2”
```

Remark: program should be run with Python3 to avoid undefined behaviour.

For example:
```bash
Python3 main.py "the Beatles" "Yesterday" "John Lennon" "Imagine"
```

The output:
```bash
Yesterday by the Beatles and Imagine by John Lennon are similar  according to lemmatization by 12.33%
```

The user can also choose the preferred similarity method through -p command
```bash
Python3 main.py "the Beatles" "Yesterday" "John Lennon" "Imagine" -p
```

User can choose among Jaccard Similarity and the Intersection method. By default Jaccard similarity is performed, for its better performance.
``` bash
Python3 main.py "the Beatles" "Yesterday" "John Lennon" "Imagine" -p “intersection”
```

The output:
```bash
Number of intersection by lemmatization is 9
```

The last optional argument is -h, that gives the user some help on the inputs required.
The output:
```bash
positional arguments:
  artist1               First artist
  song1                 Song of the first artist
  artist2               Second artist
  song2                 Song of the Second artist
```

optional arguments:
```bash
  -h, --help: show this help message and exit
  -p {jaccard,intersection}, --preference {jaccard,intersection}: Enter similarity method preference
```

## Running Tests
In the folder Tests the user can find the unit tests. To perform the test on lemmatization, for example, the command should be written as follows: 
```bash
python3 Tests/test_lemmatization.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
GPL
