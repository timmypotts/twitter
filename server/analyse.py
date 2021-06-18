import pandas as pd
import numpy as np
import re
import nltk
import plotly.express as px

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer


df=pd.read_csv('tweets.csv')




def remove_content(text):
    text = re.sub(r"http\S+", "", text) #remove urls
    text=re.sub(r'\S+\.com\S+','',text) #remove urls
    text=re.sub(r'\@\w+','',text) #remove mentions
    text =re.sub(r'\#\w+','',text) #remove hashtags
    return text
def process_text(text, stem=False): #clean text
    stopwords = nltk.corpus.stopwords.words('english')
    newStopWords = ['like', 'much', 'lol', 'one', 'think', 'would', 'going', 'really', 'yeah', 'go', 'say', ]
    stopwords.extend(newStopWords)
    print(stopwords)
    text=remove_content(text)
    text = re.sub('[^A-Za-z]', ' ', text.lower()) #remove non-alphabets
    tokenized_text = word_tokenize(text) #tokenize
    clean_text = [
         word for word in tokenized_text
         if word not in stopwords
    ]
    if stem:
        clean_text=[stemmer.stem(word) for word in clean_text]
    return ' '.join(clean_text)

df['cleaned_tweets']=df['tweet'].apply(lambda x: process_text(x))
df['tweet']=df['tweet'].apply(lambda x: remove_content(x))

temp=' '.join(df['cleaned_tweets'].tolist())
wordcloud = WordCloud(width = 800, height = 500, 
                background_color ='black', 
                min_font_size = 10).generate(temp)
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0) 
plt.show()


def plot_topn(sentences, ngram_range=(1,3), top=20,firstword=''):
    c=CountVectorizer(ngram_range=ngram_range)
    X=c.fit_transform(sentences)
    words=pd.DataFrame(X.sum(axis=0),columns=c.get_feature_names()).T.sort_values(0,ascending=False).reset_index()
    res=words[words['index'].apply(lambda x: firstword in x)].head(top)
    plt=px.bar(res, x='index',y=0)
    plt.update_layout(yaxis_title='count',xaxis_title='Phrases')
    plt.show()

plot_topn(df['cleaned_tweets'], ngram_range=(1,1))
plot_topn(df['cleaned_tweets'], ngram_range=(2,2))
plot_topn(df['cleaned_tweets'], ngram_range=(3,3))