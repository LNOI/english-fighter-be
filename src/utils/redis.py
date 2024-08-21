from redis import Redis
from redis.exceptions import ConnectionError

r = Redis(host="localhost", port=6379, db=0)
