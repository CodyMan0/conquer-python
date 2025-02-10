import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests


def fetcher(parmas):
    print(parmas)
    session = parmas[0]
    url = parmas[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com"] * 10
    executor = ThreadPoolExecutor(max_workers=3)

    with requests.Session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        params = [(session, url) for url in urls]
        result = list(executor.map(fetcher, params))
    # print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)

# 기존 코드보다 성능이 좋아짐.
