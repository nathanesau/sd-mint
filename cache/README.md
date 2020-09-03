# Cache

running postgres docker for cache:

```bash
docker run -p 6379:6379 --name mint-redis -d redis
```

## Info

Design of cache:

* Populate cache with ``categories.json`` on startup

```python
import json
import redis

if __name__ == "__main__":
    r = redis.Redis("localhost", 6379)
    with open('cache/categories.json') as f:
        categories = json.load(f)
        for seller, category in categories.get("seller_category").items():
            r.set(seller, category)
    r.close()

* Update ``categories.json`` periodically using category service
* Category service running as background scheduler (part of mint-app)

New information about categories is obtained using crowdsourcing.

* Users of the mint-app website recommend categories for a service

Possible categories:

* See ``categories.json``.
* Category must be one of the main categories (ex. Shopping) or sub-categories (ex. Books).