# text-mood
How to measure the “mood” of a text

Objective: find a way to measure the “mood” of a text input, such as Facebook feed, books, news.

Approach: by calculating the ratio between positive and negative words, this script gives a numeric value that allows to compare the “mood” of different texts.

The script uses a great dictionary of English words which contains a sentiment score for each word (Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014).

Results: these are the results of different books passed through the script.
Book 	Total words 	“Scorable” words 	Score
Ulyses 	275,588 	2,327 	0.359
Alice in Wonderland 	30,591 	538 	0.249
Grimms Fairy Tales 	105,324 	875 	0.233
Dracula 	167,897 	1,521 	0.203
Tom Sawyer 	77,625 	1,316 	0.074

Code:
The python code begins by importing the required modules.

Then we create an array with words from the dictionary and their score. Store the file “dictionary.csv” in the same directory of the python script.

Now, prepare the input text. Copy and paste the text into a file called “input.txt”.

Store this file in the same directory. The preparation begins by changing all the words to lowercase and then removing any special character such as: ‘,”,.,-,!,?,(,).

Then sort alphabetically (this last step allows the script to run faster).
The next step is where the magic happens. First create empty arrays to store the data. Then do a loop to check each work against the dictionary. If the word exists in the dictionary, then count the occurrences and then multiply the score by the number of occurrences (a good word that repeats many times would increase the overall score and vice versa). If the word does not exist in the dictionary, discard it.

Find the Github rep here: link

There is a Github rep that does a much better work, but I bet it wasn’t written in a couch 🙂 : link
