from __future__ import print_function

import json
from pprint import pprint

data = None
with open('result.json') as data_file:    
    data = json.load(data_file)

titles = []
bodies = []

for k,v in data.iteritems():
	titles.append(v['title'])
	# body = v['body']
	body  = " ".join(v['keywords'])
	bodies.append(body)

import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.externals import joblib



km = joblib.load('doc_cluster.pkl')
clusters = km.labels_.tolist()

news = { 'title': titles, 'body': bodies, 'cluster': clusters}

frame = pd.DataFrame(news, index = [clusters] , columns = ['title', 'cluster'])

print(frame['cluster'].value_counts())



print("Top terms per cluster:")
print()
#sort cluster centers by proximity to centroid
order_centroids = km.cluster_centers_.argsort()[:, ::-1] 

for i in range(num_clusters):
    print("Cluster %d words:" % i, end='')
    
    for ind in order_centroids[i, :6]: #replace 6 with n words per cluster
        print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
    print() #add whitespace
    print() #add whitespace
    
    print("Cluster %d titles:" % i, end='')
    for title in frame.ix[i]['title'].values.tolist():
        print(' %s,' % title, end='')
    print() #add whitespace
    print() #add whitespace
    
print()
print()