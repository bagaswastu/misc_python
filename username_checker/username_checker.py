import json
from queue import Queue
import threading
from urllib.error import HTTPError
from urllib.request import urlopen
from urllib.parse import urlparse

url_list = [
    "https://keybase.io/{username}",
    "https://github.com/{username}",
    "https://replit.com/@{username}",
]
queue = Queue()
domain_status = []


def test_url(url: str):
    try:
        urlopen(url)
        return True
    except HTTPError as e:
        if e.status == 404:
            return False
        print(f"Error {e} when accessing", url)


def check_username(username: str):
    while not queue.empty():
        url = queue.get().format(username=username)
        is_available = test_url(url, username)
        domain_status.append(
            {"domain": urlparse(url).netloc, "available": is_available, "url": url}
        )


def run_checker(username: str):
    for domain in url_list:
        queue.put(domain)

    thread_list = []
    for domain in url_list:
        thread = threading.Thread(target=check_username, args=[username])
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()
    print("Please wait...\n")
    for thread in thread_list:
        thread.join()


while True:
    username = input("Input username: ")
    if username:
        run_checker(username.replace(" ", ""))
        break


print(json.dumps(domain_status, indent=2, default=str))
