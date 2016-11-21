import sys
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()


if len(sys.argv) == 1:

        cur.execute("SELECT * FROM tweetwordcount ORDER BY word");
	records = cur.fetchall()
	print records
        conn.commit()
        conn.close()
elif len(sys.argv) == 2:
	var=str(sys.argv[1])
	cur.execute("SELECT DISTINCT count FROM tweetwordcount WHERE word='%s'" % var);
	count = cur.fetchall()[0][0]
	print
	print
	print "Total number of occurences of '",var,"':",count
	print
	
