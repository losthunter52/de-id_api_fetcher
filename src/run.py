import threading
import requests
import json
from .settings import *
from .handler import *
from .fetcher import *

class add_row(threading.Thread):
    def __init__(self, dataset, thread, rows, headers):
        threading.Thread.__init__(self)
        self.dataset = dataset
        self.thread = thread
        self.rows = rows
        self.headers = headers

    def fetch_row(self):
        for data in self.dataset:
            body = PAYLOAD_CONFIGURATION
            body.update({'data':[data]})
            row = []
            self.rows.append(row)
            row.append("thread-"+str(self.thread))
            index = len(self.rows)
            row.append(index)
            for t in range(5):
                row.append(fetch(body, URL, self.headers))
    
    def run(self):
        self.fetch_row()

def Run(archive, threads):
    rows = []
    active_threads = []

    headers = {'Content-type': 'application/json'}
    body = json.dumps({"username": USERNAME, "password": PASSWORD})

    post = requests.post(LOGIN_URL, data=body, headers=headers)

    if post.status_code == 401:
        post = requests.post(REGISTER_URL, data=body, headers=headers)

    response = json.loads(post.text)
    headers.update({'Authorization': 'Token ' + response['token']})


    for i in range(int(threads)):
        thread = i + 1
        dataset = read_file(archive)
        t = add_row(dataset, thread, rows, headers)
        t.start()
        active_threads.append(t)

    for t in active_threads:
        t.join()

    write_file(threads, archive, rows)