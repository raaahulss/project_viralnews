import pandas as pd
import numpy as np
import time
import threading

def method1():
    global original_df
    while True:
        original_df = original_df.append({'a':1, 'b':2,'c':3}, ignore_index=True)
        print("method 1 : ", len(original_df))
        time.sleep(3)

def method2():
    global original_df
    while True:
        print("method 2 : ", len(original_df))
        time.sleep(4)

def main():
    global original_df
    original_df = pd.DataFrame(columns=['a', 'b', 'c'])
    watcher_t = threading.Thread(target=method1, daemon=True)
    scheduler_t = threading.Thread(target=method2, daemon=True)
    watcher_t.start()
    scheduler_t.start()
    watcher_t.join()
    scheduler_t.join()

if __name__ == "__main__":
    main()