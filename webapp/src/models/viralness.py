from torch import nn
import torch
import spacy
from collections import Counter
import re
import json
import string
import numpy as np
from nltk.corpus import stopwords
import src.constants as cnst
import boto3
from io import BytesIO
from numpy.lib.npyio import NpzFile
import nltk

from src.collection.news_fetcher import NewsObject

def tokenize(text):
    text = text.replace("[^\w\s]","").lower()
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text.lower())
    return [token.text for token in tok.tokenizer(nopunct) if token not in stop_words]

# def counter(content ):
#     counts = Counter()
#     counts.update(tokenize(content))
#     print("num_words before:", len(counts.keys()))
#     for word in list(counts):
#         if counts[word] < 2:
#             del counts[word]
#     print("num_words after:",len(counts.keys()))
#     return counts

# def create_corpus(counts):
#     vocab2index = {"":0, "UNK":1}
#     words = ["","UNK"]
#     for word in counts:
#         vocab2index[word] = len(words)
#         words.append(word)
#     return vocab2index, words

def preprocess(content):
    # counts = counter(content)
    # vocab2index = np.load("./src/models/vocab2index.npy",allow_pickle='TRUE').item()
    # words = np.load("./src/models/wordlist.npy",allow_pickle='TRUE')
    # print(type(vocab2index), type(words))
    encoded, length = encode_sentence(content)
    return (encoded, length)

# def encode_sentence(text, vocab2index, N=450):
#     tokenized = tokenize(text)
#     encoded = np.zeros(N,dtype=int)
#     enc1 = np.array([vocab2index.get(word,vocab2index["UNK"]) for word in tokenized])
#     length = min(N, len(enc1))
#     encoded[:length] = enc1[:length]
#     return encoded, length

# vocab2index = {"":0, "UNK":1}
# words = ["","UNK"]
# for word in counts:
#     vocab2index[word] = len(words)
#     words.append(word)

def encode_sentence(text, N=cnst.VIRALNESS_FIXED_LENGTH):
    tokenized = tokenize(text)
    encoded = np.zeros(N,dtype=int)
    enc1 = np.array([vocab2index.get(word,vocab2index["UNK"]) for word in tokenized])
    length = min(N, len(enc1))
    encoded[:length] = enc1[:length]
    return encoded, length

# pesudo model functions
# class LSTM_fixed_len(nn.Module):
#     def __init__(self, vocab_size, embedding_dim, hidden_dim):
#         super(LSTM_fixed_len, self).__init__()
#         self.embeddings = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
#         self.dropout = nn.Dropout(0.2)
#         self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True, num_layers=2, bidirectional=True)
#         self.linear = nn.Linear(hidden_dim*2, 4, bias=False)

#     def forward(self, x, l):
#         x = self.embeddings(x)
#         x = self.dropout(x)
#         lstm_out,( ht, ct) = self.lstm(x)
#         return self.linear(torch.cat((ht[-2],ht[-1]), dim=1))

class LSTM_glove_vecs(torch.nn.Module) :
    def __init__(self, vocab_size, embedding_dim, hidden_dim, glove_weights) :
        super().__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        self.embeddings.weight.data.copy_(torch.from_numpy(glove_weights))
        self.embeddings.weight.requires_grad = False ## freeze embeddings
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True, bidirectional=True, num_layers=2)
        self.linear = nn.Linear(hidden_dim, 4)
        self.dropout = nn.Dropout(0.2)
        
    def forward(self, x, l):
        x = self.embeddings(x)
        x = self.dropout(x)
        lstm_out, (ht, ct) = self.lstm(x)
        return self.linear(ht[-1])

def load_model():
    s3 = boto3.resource('s3')
    stream =  BytesIO(s3.Object('project-viralnews-model', 'viralness.npz').get()['Body'].read())
    viralness_files = NpzFile(stream, own_fid=True, allow_pickle=True)
    
    vocab2index = viralness_files['vocab2index'].item()
    tok = spacy.load('en_core_web_sm')
    # stop_words = viralness_files['stop_words']
    pretrained_weights = viralness_files['pretrained_weights']
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    state_dict = torch.load( BytesIO(s3.Object('project-viralnews-model', 'bilstm_content.pt').get()['Body'].read()), map_location=device)
    # tok = spacy.load(cnst.VIRALNESS_TOKENIZER)
    nltk.download('stopwords')
    stop_words = set(stopwords.words(cnst.VIRALNESS_STOPWORDS_LANG))
    viralness_model = LSTM_glove_vecs(cnst.VIRALNESS_VOCAB_SIZE, 100, 100, pretrained_weights)
    viralness_model.load_state_dict(state_dict)
    return vocab2index, tok, stop_words, device, viralness_model


def get_viralness(news: NewsObject) -> float:
    #Load elements
    # tok = spacy.load(cnst.VIRALNESS_TOKENIZER)
    # stop_words = set(stopwords.words(cnst.VIRALNESS_STOPWORDS_LANG))
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # pretrained_weights = np.load(cnst.VIRALNESS_GLOVE_WEIGHT_PATH, allow_pickle=True)
    # vocab2index = np.load(cnst.VIRALNESS_VOCAB2INDEX_PATH, allow_pickle=True)
    # vocab2index = vocab2index.item()
    

    #Process request
    encoded_content, length = preprocess(news.content)
    encoded_content = torch.from_numpy(encoded_content).to(torch.int64)
    encoded_content = encoded_content.unsqueeze(0)
    y_hat = viralness_model(encoded_content, len)
    return cnst.VIRALNESS_RETURN_VAL_LIST[int(torch.max(y_hat, 1)[1])]
    

    # Older model
    # encoded_content, length, vocab_size = preprocess(news.content)
    # encoded_content = torch.from_numpy(encoded_content).to(torch.int64)
    # encoded_content = encoded_content.unsqueeze(0)
    # viralness_model = LSTM_fixed_len(vocab_size, 200, 256)
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # viralness_model.load_state_dict(torch.load("./src/models/viralness.pt", map_location=device))
    # y_hat = viralness_model(encoded_content, len)
    # return int(torch.max(y_hat, 1)[1])

print("Importing viralness model")
vocab2index, tok, stop_words, device, viralness_model = load_model()
print("Viralness model imported",type(vocab2index), type(tok), type(stop_words))
