# SCRAPPING_URL="https://embed.ly/docs/explore/extract?url="
# SCRAPPING_KEY="1934f519a63e142e0d3c893e59cc37fe0172e98a"

# key set 1
# CONSUMER_KEY='RHfPl9J0lOAYxFawj21tBAvgG'
# CONSUMER_SECRET='HfVVnF7fnfSCb3BHSwQ9FyAWyFa73t4wwOAIO0wZO3jhKtaYU0'
# ACCESS_TOKEN_KEY='1242854923261358083-ouJ6KVlpvIrvH0hJYjmyYceIUzuf5E'
# ACCESS_TOKEN_SECRET='AdEh0q4TBTQ4wm9mOU6Uld8HBZGfAvgC32H1YjNelq1Xk'
# SEARCH_ENV = 'projectidk' # Search environment name

#key set 2
# CONSUMER_KEY='fZka0Vfn7Voxt65qmSdc39QVh'
# CONSUMER_SECRET='Xk9eljv3lVJnzkMx3iPEhAGIivs1Yt3QbtFY02aqy29mdTMfsZ'
# ACCESS_TOKEN_KEY='1241834718041079813-expRyPVI6Vvo9FcKDtgovIBPLOgpkv'
# ACCESS_TOKEN_SECRET='Ab89hMnInzQzULrZ8qwsRdodKpO73kTMR7B6CUYCCc2Hh'
# SEARCH_ENV = 'dev' # Search environment name




# key set 2
# CONSUMER_KEY='58wlGpzEOwum6nghvA8tj6nz6'
# CONSUMER_SECRET='b04KqyzRyquIiYGwqv9B12hRqjEj9tvOp53DtoFZJtetaZ7cZE'
# ACCESS_TOKEN_KEY='1243275961824612358-65qxIlXTEhjw0jlbBaK4I0olH9nRP9'
# ACCESS_TOKEN_SECRET='wYdkYaNCakb7sX5PnHjF1u0oJc7Y73iijqbJ4VeB4yyEd'
# SEARCH_ENV = 'dev' # Search environment name

# premium key set
CONSUMER_KEY='PtzUlT4l8yMKPtPHrmGCjF0iF'
CONSUMER_SECRET='sJlUtEwtlylp4witiC2exvU26IlXv6C15iS7B7zlXnWIXmrPa0'
ACCESS_TOKEN_KEY='1242221626256773120-I1w5qsMOQ4RkLJAtr4C0TR092TtXd2'
ACCESS_TOKEN_SECRET='stOnsbz98GwkceoufXAuObBaXzvritHwe3Blc057Kd8Vz'
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
