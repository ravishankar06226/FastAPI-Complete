# first run this command to make redis database server up : docker run -d -p 6379:6379 redis

import redis

r = redis.Redis(host='localhost', port=6379, db=0)

try:
    if r.ping():
        print('Connected to Redis!')
except redis.ConnectionError:
    print('Redis connection failed!')


r.set('framework', 'FastAPI')

value = r.get('framework')
print(f"Stored value for framework: {value.decode()}")
