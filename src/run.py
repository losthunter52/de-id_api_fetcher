import threading
from .settings import *
from .handler import *
from .fetcher import *

class add_row(threading.Thread):
    def __init__(self, dataset, thread, rows):
        threading.Thread.__init__(self)
        self.dataset = dataset
        self.thread = thread
        self.rows = rows

    def fetch_row(self):
        for data in self.dataset:
            body = PAYLOAD_CONFIGURATION
            body.update({'database':[data]})
            row = []
            self.rows.append(row)
            row.append("thread-"+str(self.thread))
            index = len(self.rows)
            row.append(index)
            for t in range(5):
                row.append(fetch(body, URL))
    
    def run(self):
        self.fetch_row()

def Run(archive, threads):
    rows = []
    active_threads = []

    for i in range(int(threads)):
        thread = i + 1
        dataset = read_file(archive)
        t = add_row(dataset, thread, rows)
        t.start()
        active_threads.append(t)

    for t in active_threads:
        t.join()

    write_file(threads, archive, rows)