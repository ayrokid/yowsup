from yowsup.demos import sendclient
import MySQLdb
import MySQLdb.cursors
db = MySQLdb.connect(host="localhost", # your host, usually localhost
user="root", # your username
passwd="root", # your password
db="push",
cursorclass=MySQLdb.cursors.DictCursor) # name of the data base


credentials = ['6281390688955', 'Ga3lQvVTvzt10PlCGC/W5MAJfuE=']

try:
    cur = db.cursor()

    stack = sendclient.YowsupSendStack(
        credentials,
        [(['6285725523023', 'pesan dari ubuntu']), (['6285728825287', 'pesan dari ubuntu 14.04'])]
    )
    stack.start()
except KeyboardInterrupt:
    print('\nYowsdown')
