import json
import redis
import os

if __name__ == "__main__":

    r = redis.StrictRedis(host="165.22.234.253", port=6379, db=0,
        password=os.environ['REDIS_PASS'])

    BASEDIR = os.path.dirname(os.path.realpath(__file__))

    with open('{}/init_cache_values.json'.format(BASEDIR)) as f:
        categories = json.load(f)
        for seller, category in categories.get("seller_category").items():
            r.set(seller, category['default'])
    r.close()