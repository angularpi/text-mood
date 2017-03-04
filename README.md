#text-mood
<strong>Objective:</strong> find a way to measure the "mood" of a text input, such as Facebook feed, books, news.

<strong>Approach:</strong> by calculating the ratio between positive and negative words, this script gives a numeric value that allows to compare the "mood" of different texts.

<!--more-->

The script uses a great dictionary of English words which contains a sentiment score for each word (<span style="color: #999999;"><em>Hutto, C.J. &amp; Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014</em></span>).

<strong>Results:</strong> these are the results of different books passed through the script.
<table style="width: 100%;">
<tbody>
<tr>
<th><strong>Book</strong></th>
<th>Total words</th>
<th>"Scorable" words</th>
<th><strong>Score</strong></th>
</tr>
<tr>
<td>Ulyses</td>
<td>275,588</td>
<td>2,327</td>
<td>0.359</td>
</tr>
<tr>
<td>Alice in Wonderland</td>
<td>30,591</td>
<td>538</td>
<td>0.249</td>
</tr>
<tr>
<td>Grimms Fairy Tales</td>
<td>105,324</td>
<td>875</td>
<td>0.233</td>
</tr>
<tr>
<td>Dracula</td>
<td>167,897</td>
<td>1,521</td>
<td>0.203</td>
</tr>
<tr>
<td>Tom Sawyer</td>
<td>77,625</td>
<td>1,316</td>
<td>0.074</td>
</tr>
</tbody>
</table>
<strong>Code:</strong>

The python code begins by importing the required modules.

Then we create an array with words from the dictionary and their score. Store the file "dictionary.csv" in the same directory of the python script.

Now, prepare the input text. Copy and paste the text into a file called "input.txt".

Store this file in the same directory. The preparation begins by changing all the words to lowercase and then removing any special character such as: ',",.,-,!,?,(,).

Then sort alphabetically (this last step allows the script to run faster).
The next step is where the magic happens. First create empty arrays to store the data. Then do a loop to check each work against the dictionary. If the word exists in the dictionary, then count the occurrences and then multiply the score by the number of occurrences (a good word that repeats many times would increase the overall score and vice versa). If the word does not exist in the dictionary, discard it.

Find the Github rep here: <a href="https://github.com/ospanton/text-mood">link</a>

There is a Github rep that does a much better work, but I bet it wasn't written in a couch :) : <a href="https://github.com/cjhutto/vaderSentiment/tree/master/vaderSentiment">link</a>
