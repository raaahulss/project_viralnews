import requests
import threading
import datetime
import numpy as np
import json


class myThread (threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name

    def run(self):
        print("Starting " + self.name)
        print_time(self.name)
        print("Exiting " + self.name)


def print_time(url, latencies, titles):
    start_time = datetime.datetime.now()
    response = requests.post(f'http://localhost:5000/api/url?url={url}')
    end_time = datetime.datetime.now()
    delta_time = end_time - start_time
    latencies.append(delta_time.total_seconds())
    titles.append(response.content)


if __name__ == '__main__':
    # Create new threads
    urls = ['https://twitter.com/nytimes/status/1286401952126042113',
            'https://twitter.com/nytimes/status/1286400957459374088',
            'https://twitter.com/nytimes/status/1286390653581131778',
            'https://twitter.com/CNN/status/1286400952757624835',
            'https://twitter.com/CNN/status/1286386172852342784',
            'https://twitter.com/CNN/status/1286390909953810438',
            'https://twitter.com/CNN/status/1286385860209004544',
            'https://twitter.com/WSJ/status/1286647356788740097',
            'https://twitter.com/WSJ/status/1286620915141312515',
            'https://twitter.com/WSJ/status/1286518814189006848'
            ]

    latencies = []
    titles = []

    for url in urls:
        print_time(url, latencies, titles)

    for i in range(len(latencies)):
        print(f"{latencies[i]} s: {titles[i]}")
    print("Exiting Main Thread")

    print(
        f"Maximum {np.max(latencies)} s\nMinimum {np.min(latencies)} s\nMean {np.mean(latencies)} s\nMedian {np.median(latencies)} s\nStandard deviation {np.std(latencies)} s"
    )
