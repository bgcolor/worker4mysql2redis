# !/usr/bin/py

import MySQLdb
import redis

HOST = "192.168.83.57"
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "redis_sync_test"
connect = MySQLdb.connect(HOST, USERNAME, PASSWORD, DATABASE)

cursor = connect.cursor();
sql = "select * from redis_reset_map"

try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
      resetid = row[0]
      resetkey = row[1]
      print "%s%s" % \
      (resetkey, resetid)

   connect.commit()

except:
    connect.rollback()
    print "Error: unable to fecth data"