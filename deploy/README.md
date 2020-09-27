# deploy instructions

## environment variables

environment varaibles should be set manually in server (for security reasons). This can be done in ``~/.bashrc``. Following variables should be set:

```bash
REDIS_HOST=yourip
REDIS_PASS=yourpass
ABC_BANK_API_URL=http://yourip:5001/api/v1
XYZ_BANK_API_URL=http://yourip:5002/api/v1
XYZ_TRADE_API_URL=http://yourip:5003/api/v1
```

## docker containers

redis, mint-app and third-party apis should be running on master server.

redis has a 100M memory limit, which is sufficient since it's only holding category info.

Redis data is backed up by a service so cache data is not lost. Backups are done regularly (every 30 seconds).

## services

backup_redis should be running on master server.
