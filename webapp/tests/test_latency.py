import requests
import threading
import datetime
import numpy as np
import json


class MyThread (threading.Thread):
    def __init__(self, thread_id, name, url):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.url = url

    def run(self):
        print("Starting " + self.name)
        record_time(self.url)
        print("Exiting " + self.name)


def parallel_test():
    url_num = len(urls)
    threads = []
    for i in range(url_num):
        threads.append(MyThread(i, f"Thread-{i}", urls[i]))

    # Start new Threads
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    for i in range(len(latencies)):
        print(f"{latencies[i]} s: {responses[i]}")

    print(
        f"Maximum {np.max(latencies)} s\nMinimum {np.min(latencies)} s\nMean {np.mean(latencies)} s\nMedian {np.median(latencies)} s\nStandard deviation {np.std(latencies)} s"
    )


def record_time(url):
    start_time = datetime.datetime.now()
    response = requests.post(f'http://localhost:5000/api/url?url={url}')
    end_time = datetime.datetime.now()
    delta_time = end_time - start_time
    latencies.append(delta_time.total_seconds())
    responses.append(response.content)


def sequential_test():
    for url in urls:
        record_time(url)

    for i in range(len(latencies)):
        print(f"{latencies[i]} s: {responses[i]}")

    print(
        f"Maximum {np.max(latencies)} s\nMinimum {np.min(latencies)} s\nMean {np.mean(latencies)} s\nMedian {np.median(latencies)} s\nStandard deviation {np.std(latencies)} s"
    )


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
    # urls = [
    #     'https://www.nytimes.com/2020/07/25/us/protests-seattle-portland.html',
    #     'https://www.nytimes.com/2020/07/26/nyregion/nyc-coronavirus-time-life-building.html?action=click&module=Top%20Stories&pgtype=Homepage',
    #     'https://www.nytimes.com/2020/07/26/style/functional-fashion.html?action=click&module=Top%20Stories&pgtype=Homepage',
    #     'https://www.cnn.com/2020/07/26/health/us-coronavirus-sunday/index.html',
    #     'https://www.cnn.com/2020/07/26/politics/kudlow-republicans-checks-unemployment-cnntv/index.html',
    #     'https://www.cnn.com/2020/07/26/us/utah-plane-crash-backyard-trnd/index.html',
    #     'https://www.cnn.com/2020/07/26/health/crip-camp-americans-with-disabilities-act-wellness/index.html',
    #     'https://www.nbcnews.com/news/nbcblk/john-lewis-civil-rights-giant-cross-selma-bridge-one-final-n1234941',
    #     'https://www.nbcnews.com/politics/2020-election/pro-trump-super-pac-losing-money-race-democrats-n1234524',
    #     'https://www.nbcnews.com/politics/congress/white-house-pushes-slashing-expanded-jobless-benefits-despite-rises-unemployment-n1234944'
    # ]
    latencies = []
    responses = []
    # sequential_test()
    parallel_test()
