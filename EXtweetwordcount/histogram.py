import sys
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()


if len(sys.argv) > 1:
	for i in range(1,len(sys.argv)):
		varlist=[]
		varlist.extend(sys.argv[i].split(","))
	min = min(map(int,varlist))
	max = max(map(int,varlist))
        cur.execute("SELECT * FROM tweetwordcount where count >= %d and count <= %d order by count desc" % (min,max));
        records = cur.fetchall()
        for j in records:
		print j[0],": ",j[1]
        conn.commit()
        conn.close()
