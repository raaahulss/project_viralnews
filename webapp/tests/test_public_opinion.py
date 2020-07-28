import pandas as pd
from keras.preprocessing.text import Tokenizer
import pickle


csv = 'clean_tweet_1.csv'
my_df = pd.read_csv(csv, index_col=0)
my_df.head()
my_df.dropna(inplace=True)
my_df.reset_index(drop=True, inplace=True)
my_df.info()
x = my_df.text
tokenizer = Tokenizer(num_words=100000)
tokenizer.fit_on_texts(x)
with open('public_opinion.vocab', 'wb') as f:
    pickle.dump(tokenizer, f)
