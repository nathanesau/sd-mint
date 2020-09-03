from datetime import datetime
import redis
import os
import json
from app.models import Transaction

def update_redis_cache(new_seller_category):
    r = redis.Redis()
    try:
        for seller, smap in new_seller_category.get("seller_category").items():
            if "default" in smap:
                r.set(seller, smap["default"])
            else:
                r.set(seller, smap["crowdsourced"])
        print("updated redis cache at {}".format(datetime.now()))
    except:
        print("unable to connect to redis cache")


def update_categories_file(cachedir, new_seller_category):
    fname = os.path.join(cachedir, 'categories.json')
    with open(fname, 'w') as f:
        json.dump(new_seller_category, f)
    print("updated categories file at {}".format(datetime.now()))


def read_categories_file(cachedir):
    fname = os.path.join(cachedir, 'categories.json')
    data = {}
    with open(fname, 'r') as f:
        data = json.load(f)
    return data


def cs_task():
    """
    calculate crowdsourcing information from transactions table
    update categories.json to use the crowdsourcing information
    update redis cache to use categories.json information
    performed periodically
    """
    print("Performing crowdsourcing task")
    basedir = os.path.abspath(os.path.dirname(__file__))
    cachedir = basedir.replace('mint-app\\app', 'cache')
    current_seller_category = read_categories_file(cachedir)

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

    # add new sellers to map
    # update existing sellers with crowdsource info
    new_seller_category = current_seller_category
    for seller, category in crowdsourced_seller_category.items():
        if seller not in new_seller_category.get("seller_category"):
            new_seller_category.get("seller_category")[seller] = {
                "crowdsourced": category
            }
        else:
            new_seller_category.get("seller_category")[
                seller]["crowdsourced"] = category

    # write new crowdsource info to file
    update_categories_file(cachedir, new_seller_category)

    # update redis cache with new values
    update_redis_cache(new_seller_category)
