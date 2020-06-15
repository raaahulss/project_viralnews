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

### Setting up twitter accounts to follow

First specify what twitter accounts you want to follow by adding them to the ```accounts.txt``` file. Add one account per line without the "@" symbol. 


### Running from command line

You can run the python script from the command line with the following script. However, if the script crashes or fails for any reason, it will not restart on its own.

```bash
nohup python3 tweet_collector.py > output.log
```

### Running as systemd service

As a service, the script will continuously run in the background, and if it encounters any errors and crashes, it will restart. 

Move the systemd unit file ```dataset.service``` to ```/etc/systemd/system```

Run the following commands:

```bash
sudo systemctl daemon-reload
sudo systemctl enable dataset
sudo systemctl start dataset
```

This service is configured to restart on failure. 

## Output

The output data is saved to ```retweet_[MON]_[DAY]_[YEAR]_[HOUR]```

Here is the column structure of the output:

| tweet_id  | count  | created_time  |next_update | 1| 2 | 3| 4| ...| 100|
|---|---|---|---|---|---|---|---|---|---|

Where the numbered columns represent the offset in days from the ```created_time``` of the tweet and the values are the total number of retweets.


## Logging

By default, the script is configured to write debug information to ```bird_watcher.log``` and ```scheduler.log```

The script also outputs the debug information for both threads to ```stdout```

## Fault Tolerance

By default, the script is made to be resilient from failures. On every other iteration through the  ```scheduler``` thread, both dataframes are written to disk in the ```../data``` directory. The original tweet IDs from the ```bird_watcher``` thread are written to ```../data/original_df_[MON]_[DAY]_[YEAR]_[HOUR]``` and the retweets from the ```scheduler``` thread are written to ```../data/retweet_[MON]_[DAY]_[YEAR]_[HOUR]```. When the script starts up after a failure, it looks for the newest instances of these two files and regenerates the dataframes to regain state. Every hour, a new version of both of these files is created, which means that the state of both dataframes is exported and saved. 


