from torch import nn
import torch
import spacy
from collections import Counter
import re
import string
import numpy as np

from src.collection.news_fetcher import NewsObject
tok = spacy.load('en_core_web_sm')

def tokenize(text):
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text.lower())
    return [token.text for token in tok.tokenizer(nopunct)]

def counter(content ):
    counts = Counter()
    counts.update(tokenize(content))
    print("num_words before:", len(counts.keys()))
    for word in list(counts):
        if counts[word] < 2:
            del counts[word]
    print("num_words after:",len(counts.keys()))
    return counts

def create_corpus(counts):
    vocab2index = {"":0, "UNK":1}
    words = ["","UNK"]
    for word in counts:
        vocab2index[word] = len(words)
        words.append(word)
    return vocab2index, words

def preprocess(content):
    counts = counter(content)
    vocab2index = np.load("./src/models/vocab2index.npy",allow_pickle='TRUE').item()
    words = np.load("./src/models/wordlist.npy",allow_pickle='TRUE')
    print(type(vocab2index), type(words))
    encoded, length = encode_sentence(content, vocab2index)
    return (encoded, length, len(words))

def encode_sentence(text, vocab2index, N=450):
    tokenized = tokenize(text)
    encoded = np.zeros(N,dtype=int)
    enc1 = np.array([vocab2index.get(word,vocab2index["UNK"]) for word in tokenized])
    length = min(N, len(enc1))
    encoded[:length] = enc1[:length]
    return encoded, length

# vocab2index = {"":0, "UNK":1}
# words = ["","UNK"]
# for word in counts:
#     vocab2index[word] = len(words)
#     words.append(word)

def encode_sentence(text, vocab2index, N=450):
    tokenized = tokenize(text)
    encoded = np.zeros(N,dtype=int)
    enc1 = np.array([vocab2index.get(word,vocab2index["UNK"]) for word in tokenized])
    length = min(N, len(enc1))
    encoded[:length] = enc1[:length]
    return encoded, length

# pesudo model functions
class LSTM_fixed_len(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        super(LSTM_fixed_len, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.linear = nn.Linear(hidden_dim, 2)
        self.dropout = nn.Dropout(0.2)

    def forward(self, x, l):
        x = self.embeddings(x)
        x = self.dropout(x)
        lstm_out, (ht, ct) = self.lstm(x)
        return self.linear(ht[-1])

def get_viralness(news: NewsObject) -> float:
    encoded_content, length, vocab_size = preprocess(news.content)
    encoded_content = torch.from_numpy(encoded_content).to(torch.int64)
    encoded_content = encoded_content.unsqueeze(0)
    viralness_model = LSTM_fixed_len(vocab_size, 256, 256)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    viralness_model.load_state_dict(torch.load("./src/models/viralness.pt", map_location=device))
    y_hat = viralness_model(encoded_content, len)
    return int(torch.max(y_hat, 1)[1])

if __name__ == "__main__":
    news = NewsObject("https://www.nytimes.com/2020/07/03/us/politics/trump-coronavirus-mount-rushmore.html")
    news.fetch_from_url()
    print(get_viralness(news))
