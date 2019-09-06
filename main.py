# -*- coding:utf-8 -*-
import json
import time
import redis

def get_comic_from_mysql(comic_id):
    time.sleep(2)
    print(">>>>>从数据库中查所以很慢>>>>>>>")
    return {"id": 3, "name": "七龙珠", "pic": "https://www.pic.jpg", "des": "放松放松分解水浪费时间防守反击"
                                                                         "fsfjsjfjsd胜多负少的浪费结束了"
                                                                         "fsjdfjsfjsfsf发斯蒂芬斯蒂芬"
                                                                         "方式防辐射服"}

def get_comic_from_redis(comic_id):
    r = redis.Redis("39.106.71.25", port=6377, password="wangdongwei@bytedance.com")
    res = r.get(comic_id)
    return res


"""
先去redis查,因为redis快
如果redis没查到就去mysql中查,并且将数据放入redis供下次查询
"""


def get_comic_description(comic_id):
    res = get_comic_from_redis(comic_id)
    # 首次查询redis不一定能查到,所以要去mysql再去查
    if res is None:
        res = get_comic_from_mysql(comic_id)
        # 放到redis中,下次直接可以查redis
        r = redis.Redis("39.106.71.25", port=6377, password="wangdongwei@bytedance.com")
        r.set(comic_id, json.dumps(res))

    return res


if __name__ == "__main__":
    t = time.time()
    print(get_comic_description("2"))

    print(">>>>", time.time() - t)
    t = time.time()
    print(get_comic_description("2"))
    print(get_comic_description("2"))
    print(get_comic_description("2"))
    print(">>>>>>>", time.time() - t)


