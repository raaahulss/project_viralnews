import os

# premium key set
CONSUMER_KEY=os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET=os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN_KEY=os.environ.get("ACCESS_TOKEN_KEY")
ACCESS_TOKEN_SECRET=os.environ.get("ACCESS_TOKEN_SECRET")
SEARCH_ENV = 'viralnews1' # Search environment name


# 100 for standard twitter api and 500 for premium
SEARCH_PER_REQUEST=500
# Max number of replies returned by the system
MAX_REPLY=SEARCH_PER_REQUEST * 2

# Upperlimit on the number of seconds the system utlizes to fetch replues
MAX_TIME_REPLY_SEARCH=5

# max number of days allowed to be searched in past
# 7 for standard and 30 for premium
MAX_TWEET_CREATION_RANGE=30


MIN_CONTENT_LEN = 50

REQUEST_TIME_OUT = 3

VIRALNESS_FIXED_LENGTH = 500
VIRALNESS_VOCAB_SIZE = 104313
VIRALNESS_RETURN_VAL_LIST = [0.05, 0.2, 0.45, 0.8]
VIRALNESS_TOKENIZER = 'en_core_web_sm'
VIRALNESS_STOPWORDS_LANG = 'english'
VIRALNESS_GLOVE_WEIGHT_PATH = "./src/models/pretrained_weights_80.npy"
VIRALNESS_VOCAB2INDEX_PATH = "./src/models/vocab2index_80.npy"
VIRALNESS_STATE_DICT = "./src/models/bilstm_content.pt"
