import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

stopwords = stopwords.words('english')

def remove_mention(text):
    processed = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", text)
    text = " ".join(processed.split())
    return text


def remove_puncuation(text):
    punc_removed = []
    for char in text:
        if char not in string.punctuation:
            punc_removed.append(char)
        
    return ''.join(punc_removed)


def get_hashtags(text):
    hashtags = []
    for word in text.split(" "):
        if word.startswith("#") and len(word[1:]) > 3:
            hashtags.append(word[1:])
    return hashtags



def remove_stop_words(text):
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if word not in stopwords and len(word) > 2]  
    return ' '.join(tokens_without_sw)


def encode(text):
    return text.encode('ascii',errors='ignore').decode()
