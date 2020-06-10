# Twitter Viral News Dataset

## tweet_collector.py
This script uses the Twarc library to log every tweet from specified twitter accounts. It then queries the number of retweets every 24 hours.

In this specific implementation, the script is configured to follow the twitter accounts of various news media outlets such as Wall Street Journal, New York Times, etc.
It only logs the tweet if it contains an embedded URL to an article. 

## Install Requirements
```bash
pip3 install -r requirements.txt

```

## Running Tweet Collector

```bash
python3 tweet_collector.py
```

## Output

The output data is saved to ```data.csv```

Here is the column structure of the output:

| tweet_id  | url  | handle  | count  | created_time  |next_update | 1| 2 | 3| 4| ...| 100|
|---|---|---|---|---|---|---|---|---|---|---|---|

Where the numbered columns represent the offset in days from the ```created_time``` of the tweet and the values are the total number of retweets.


## Logging

By default, the script is configured to write debug information to ```bird_watcher.log``` and ```scheduler.log```

The script also outputs the debug information for both threads to ```stdout```
