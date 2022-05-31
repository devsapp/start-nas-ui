# coding=utf-8

import requests
import os


def handler(event, context):
    url = os.environ['KODBOX_URL']
    # print(url)
    if url.endswith(".fcapp.run"):
        url = url[:-10] + "-vpc.fcapp.run"
    print(url)
    res = requests.head(url)
    print(res.status_code)
