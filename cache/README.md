# Cache

running postgres docker for cache:

```bash
docker run -p 6379:6379 --name mint-redis -v /root/dumps:/data -d redis redis-server --requirepass yourpass
```

to connect to image with python:

```python
import redis
r = redis.StrictRedis(host="165.22.234.253", port=6379, db=0, password='yourpass')
```

## additional information



* Update ``categories.json`` periodically using category service
* Category service running as background scheduler (part of mint-app)

New information about categories is obtained using crowdsourcing.

* Users of the mint-app website recommend categories for a service

Possible categories:

* See ``categories.json``.
* Category must be one of the main categories (ex. Shopping) or sub-categories (ex. Books).