from yowsup.demos import sendclient
#import logging #tampilan log khusus centos os
import MySQLdb
import MySQLdb.cursors
db = MySQLdb.connect(host="localhost", # your host, usually localhost
user="root", # your username
passwd="root", # your password
db="push",
cursorclass=MySQLdb.cursors.DictCursor) # name of the data base


credentials = ['6281390688955', 'Ga3lQvVTvzt10PlCGC/W5MAJfuE=']

data = []

try:
    cur = db.cursor()
    cur.execute("select * from messages")
    results = cur.fetchall()
    i = 0;
    for row in results:
       data.append([ row['sender'], row['content'] ])
       i += 1
    
    #stack = sendclient.YowsupSendStack(credentials, [(['6285725523023', 'pesan dari ubuntu'])])
    stack = sendclient.YowsupSendStack(credentials, data)
    stack.start()
    print('\nKirim Sukses..')
except KeyboardInterrupt:
    print('\nYowsdown')
