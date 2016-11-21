Instructions on running the Twitter wordcount application.

Step 1) Clone the entire mdemaster_w205_exercise2 repository.

Step 2) Install postgres (if not already installed).

Step 3) In the mdemaster_w205_exercise2 directory, run create_tcount_db.py (This creates a postgres database called "tcount" and creates a table called "tweetwordcount").

Step 4) Navigate to the folder EXtweetwordcount.

Step 5) Execute $sparse run. (Let the streaming app run for about a minute).

Step 6) Execute $python finalresults.py the (This shows the number of occurrences of the word, "the").

Step 7) Execute $python finalresults.py (This outputs all words that were parsed from the tweets and their respective counts)

Step 8) Execute $python histogram.py 15,21 (This gives a list of parsed words by a specified range of counts.
