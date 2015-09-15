# !/usr/bin/py

import redis

REDIS_HOST = "192.168.83.57"
REDIS_PORT = 6379

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

r.set("resetkey1_11", 'foo');
r.set("resetkey2_5", 'bar');