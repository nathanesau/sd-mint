from datetime import datetime
import redis
import os
import json
from app import app
from app.models import Transaction

def update_redis_cache(crowdsourced_seller_category):
    r = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'],
        db=0, password=app.config['REDIS_PASS'])
    try:
        for seller, category in crowdsourced_seller_category.items():
            if r.exists(seller): pass
            # use crowdsourced since default unavailable
            r.set(seller, category)
        print("updated redis cache at {}".format(datetime.now()))
    except:
        print("unable to connect to redis cache")


def cs_task():
    """
    calculate crowdsourcing information from transactions table
    update redis cache to use crowdsourced information
    performed periodically
    """
    print("Performing crowdsourcing task")

    crowdsource_info = {}
    customized_trans = Transaction.query.filter_by(customized=1)
    for trans in customized_trans:
        seller = trans.transaction_seller
        category = trans.category
        if seller in crowdsource_info:
            seller_categories = crowdsource_info[seller]
            if category in seller_categories:
                crowdsource_info[seller][category] = crowdsource_info[seller][category] + 1
            else:  # first crowdsourced entry for seller for category
                crowdsource_info[seller][category] = 1
        else:  # first crowdsourced entry for this seller
            crowdsource_info[seller] = {category: 1}

    # determine crowdsourced category (the one with most recommendations)
    crowdsourced_seller_category = {}
    for seller, ccmap in crowdsource_info.items():
        cs_category = max(ccmap, key=ccmap.get)
        crowdsourced_seller_category[seller] = cs_category

    # update redis cache with new values
    update_redis_cache(crowdsourced_seller_category)
