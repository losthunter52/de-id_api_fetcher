import time
import requests
from .settings import ERROR_SLEEP_TIME


def fetch(body, URL):
    while True:
        try:
            start = time.perf_counter()
            post = requests.post(URL, body)
            end = time.perf_counter() - start
            end = float(end * 1000)
            break
        except requests.RequestException as error:
            print(f"[{time.strftime('%d %b %Y %H:%M:%S', time.localtime())}] {error}")
            time.sleep(ERROR_SLEEP_TIME)

    return format(end, '.3f').replace('.', ',')
