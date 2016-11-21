from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
       

    def process(self, tup):
        word = tup.values[0]
	
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()

	cur.execute("UPDATE tweetwordcount SET count=(select distinct count+1 from tweetwordcount where word=%s) WHERE word=%s", (word,word))
	conn.commit()

	cur.execute("INSERT INTO tweetwordcount (word,count) SELECT %s,%s WHERE NOT EXISTS (SELECT word FROM tweetwordcount WHERE word=%s)",(word,1,word));
	conn.commit()
	conn.close()
        
	# Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
