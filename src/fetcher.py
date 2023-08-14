import time
import requests
from .settings import ERROR_SLEEP_TIME
import json


def fetch(body, URL, headers):
    while True:
        try:
            body = json.dumps(body)
            start = time.perf_counter()
            post = requests.post(URL, data=body, headers=headers)
            end = time.perf_counter()
            response_time = (end - start) * 1000
            break
        except requests.RequestException as error:
            print(f"[{time.strftime('%d %b %Y %H:%M:%S', time.localtime())}] {error}")
            time.sleep(ERROR_SLEEP_TIME)

    return format(response_time, '.3f').replace('.', ',')
