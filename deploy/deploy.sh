#!/bin/bash

build_redis=false
deploy_service=false

#######################################################
## IMPORTANT: set environment variables before running
#######################################################

# create directories
mkdir -p /root/dumps

# build latest image of redis
if [ "$build_redis" = true ] ; then
    cd ../cache
    docker build -t mint-redis:latest .
    cd ../deploy
fi

# build latest image of third-party apis
cd ../mint-app
cp  /etc/letsencrypt/live/mint.freeddns.org/fullchain.pem .
cp  /etc/letsencrypt/live/mint.freeddns.org/privkey.pem .
docker build -t mint-app:latest .
cd ../deploy

cd ../third-party/abc_bank_api
#cp  /etc/letsencrypt/live/mint.freeddns.org/fullchain.pem .
#cp  /etc/letsencrypt/live/mint.freeddns.org/privkey.pem .
docker build -t abc_bank_api:latest .
cd ../../deploy

cd ../third-party/xyz_bank_api
#cp  /etc/letsencrypt/live/mint.freeddns.org/fullchain.pem .
#cp  /etc/letsencrypt/live/mint.freeddns.org/privkey.pem .
docker build -t xyz_bank_api:latest .
cd ../../deploy

cd ../third-party/xyz_trade_api
#cp  /etc/letsencrypt/live/mint.freeddns.org/fullchain.pem .
#cp  /etc/letsencrypt/live/mint.freeddns.org/privkey.pem .
docker build -t xyz_trade_api:latest .
cd ../../deploy

# bring down images
docker-compose -f docker-compose.yml down

# detached mode (so command will finish)
docker-compose -f docker-compose.yml up -d

# this is the first time running redis
# we must fill cache with initial values
if [ "$build_redis" = true ] ; then
    cd ../cache
    python3 init_cache.py
    cd ../deploy
fi

# deploy services
cd ../

# backup_redis
if [ "$deploy_service" = true ] ; then
    # REDIS_PASS in service file should be manually edited
    cp services/backup_redis/backup_redis.service /lib/systemd/system/
    cp /lib/systemd/system/backup_redis.service /etc/systemd/backup_redis.service
    chmod 644 /lib/systemd/system/backup_redis.service
    systemctl enable backup_redis
    systemctl start backup_redis
fi
