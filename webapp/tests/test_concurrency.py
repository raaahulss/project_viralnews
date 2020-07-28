import requests
import threading
import time
import json


class MyThread (threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name

    def run(self):
        print("Starting " + self.name)
        print_time(self.name)
        print("Exiting " + self.name)


def print_time(thread_name):
    counter = 2
    while counter:
        response = requests.post(
            'http://localhost:5000/api/url?url=https://www.nbcnews.com/politics/supreme-court/supreme-court-strikes-down-restrictive-louisiana-abortion-law-n1231392')
        print(time.ctime(time.time()) + " " + thread_name + ': ' + json.loads(response.content)['details']['title'])
        counter -= 1


if __name__ == '__main__':
    # Create new threads
    threads = []
    for i in range(25):
        threads.append(MyThread(i, f"Thread-{i}"))

    # Start new Threads
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Exiting Main Thread")
