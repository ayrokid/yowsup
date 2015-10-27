import sys
import MySQLdb
import MySQLdb.cursors
db = MySQLdb.connect(host="localhost", # your host, usually localhost
user="root", # your username
passwd="root", # your password
db="push",
cursorclass=MySQLdb.cursors.DictCursor) # name of the data base

jid = str(sys.argv[1])
message = str(sys.argv[2])

cur = db.cursor()
cur.execute("""
INSERT INTO message (jid, message, stamp) VALUES (%s,%s, NOW())""", (jid, message, ))
cur.execute("COMMIT")
