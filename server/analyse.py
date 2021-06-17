import pandas as pd
import numpy as np
import re
import nltk

nltk.download('stopwords')
from nltk.tokenize import sent_tokenize


df=pd.read_csv('tweets.csv')


print(df['tweet'])

def remove_content(text):
    text = re.sub(r"http\S+", "", text) #remove urls
    text=re.sub(r'\S+\.com\S+','',text) #remove urls
    text=re.sub(r'\@\w+','',text) #remove mentions
    text =re.sub(r'\#\w+','',text) #remove hashtags
    return text
def process_text(text, stem=False): #clean text
    stop_words = set(stopwords.words('english'))
    text=remove_content(text)
    text = re.sub('[^A-Za-z]', ' ', text.lower()) #remove non-alphabets
    tokenized_text = nltk.tokenize.word_tokenize(text) #tokenize
    clean_text = [
         word for word in tokenized_text
         if word not in stop_words
    ]
    if stem:
        clean_text=[stemmer.stem(word) for word in clean_text]
    return ' '.join(clean_text)

df['cleaned_tweets']=df['tweet'].apply(lambda x: process_text(x))
df['tweet']=df['tweet'].apply(lambda x: remove_content(x))