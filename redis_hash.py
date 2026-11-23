# Get_commands
# HSET HGET HDEL
# HEXISTS DEL HGETALL
# HINCRYBY HINCRYFLOAT HMSET
# HSETNX HSTRLEN HVALS HKEYS
#
# HSET employee:101 name "Satvir" age 36 department "IT" salary 50000
# HGET employee:101 name
# HGETALL employee:101
# HEXISTS employee:101 name
# HEXISTS employee:101 email
# HKEYS employee:101
# HVALS employee:101
# HSTRLEN employee:101 name
# HINCRBY employee:101 salary 5000
# HINCRBYFLOAT employee:101 salary 100.50
# HDEL employee:101 age
# HGETALL employee:101
# DEL employee:101

import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.hset(
    "user:101",
    mapping={
        "name": "Satvir",
        "age": 36,
        "department": "IT",
        "salary": 50000
    }
)

print(r.hget("user:101", "name"))
print(r.hgetall("user:101"))
print(r.hexists("user:101", "name"))
print(r.hkeys("user:101"))
print(r.hvals("user:101"))
print(r.hincrby("user:101", "salary", 5000))
print(r.hincrbyfloat("user:101", "salary", 100.50))
print(r.hstrlen("user:101", "name"))
r.hdel("user:101", "age")
print(r.hgetall("user:101"))
r.delete("user:101")
