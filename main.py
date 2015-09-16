# !/usr/bin/py

import MySQLdb
import redis

MYSQL_HOST = "192.168.83.57"
MYSQL_USERNAME = "root"
MYSQL_PASSWORD = "123456"
MYSQL_DATABASE = "redis_sync_test"
REDIS_HOST = "192.168.83.57"
REDIS_PORT = 6379
# REDIS_PASSWORD = "ztolredis"
keyFormat = "%s_%d"
delSql = "DELETE FROM redis_reset_map WHERE itemId = %d AND resetKey = '%s'"
sql = "select * from redis_reset_map"

connect = MySQLdb.connect(MYSQL_HOST, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DATABASE)
r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

cursor = connect.cursor();

try:
    cursor.execute(sql)
    results = cursor.fetchall()

    keys = [];
    for row in results:
        resetId = row[0]
        resetKey = row[1]
        tmp = delSql % (resetId, resetKey)
        keys.append(keyFormat % (resetKey, resetId))
        cursor.execute(tmp)

    if keys.__len__() > 0 :
        r.delete(*tuple(keys))
        print "deleted redis keys."
        connect.commit()
        print "deleted mysql records."
    else :
        print "no data needed to sync."
except:
    connect.rollback()
    print "some error occurs."