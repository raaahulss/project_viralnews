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

    latencies.append((end_time - start_time).microseconds / 1000.0)
    titles.append(response.content)
    # titles.append(json.loads(response.content)['details']['title'])


if __name__ == '__main__':
    # Create new threads
    urls = ['https://twitter.com/nytimes/status/1286401952126042113',
            'https://twitter.com/nytimes/status/1286400957459374088',
            'https://twitter.com/nytimes/status/1286390653581131778',
            'https://twitter.com/CNN/status/1286400952757624835',
            'https://twitter.com/CNN/status/1286386172852342784',
            'https://twitter.com/CNN/status/1286390909953810438',
            'https://twitter.com/CNN/status/1286385860209004544',
            'https://twitter.com/ABC/status/1286404486894944256',
            'https://twitter.com/ABC/status/1286397840596643841',
            'https://twitter.com/ABC/status/1286395172973088771'
            ]
    latencies = []
    titles = []

    for url in urls:
        print_time(url, latencies, titles)

    for i in range(len(latencies)):
        print(f"{latencies[i]} ms: {titles[i]}")
    print("Exiting Main Thread")

    print(
        f"Maximum {np.max(latencies)} ms\nMinimum {np.min(latencies)} ms\nMean {np.mean(latencies)}\nMedian {np.median(latencies)}\nStandard deviation {np.std(latencies)}"
    )
