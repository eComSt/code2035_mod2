import redis
r = redis.Redis("51.250.65.169",port = 6379,db=0)
x = r.get("999999")
print(x)