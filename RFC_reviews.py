# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 00:56:00 2021

@author: Immortal
"""

import nltk #for building programs for text analysis(The Natural Language Toolkit)
from nltk.corpus import stopwords #getting the stopwords from nltk corpus function
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re # regular expression, helps us to match or find other strings or sets of strings
nltk.download('punkt')
nltk.download('stopwords')
from nltk import word_tokenize
nltk.download('wordnet')
from nltk.corpus import wordnet
import textblob#perform basic NLP tasks.
from textblob import TextBlob
from textblob import Word
import string 
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report#To get the classification report such as precison,recall(sesitivity),f1 score, support.. 
from sklearn.feature_extraction.text import CountVectorizer#Used to convert collection of text documents to a matrix of token counts.
from sklearn.metrics import f1_score,accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer#term frequencey- inverse document frequncy is a numerical statistic that is intended to reflect how important a word is to document in a collecion or corpus


hotel=pd.read_csv("Downloads//reviews_ratings_hotel.csv")#Loading the dataset

hotel.head()

#Classifiying the rating into positive, Negative, Neutral 
#Rating which is greater than 3 considered as +ve, Less than 3 considered as -ve, And 3 is considered as Neutral.
Sentiment_Rating = [] 
for value in hotel["ratings"]: 
    if value > 3: 
        Sentiment_Rating.append("positive") 
    elif value < 3: 
        Sentiment_Rating.append("negative") 
    else: 
        Sentiment_Rating.append("neutral") 
        
hotel["Sentiment_Rating"] = Sentiment_Rating    #adding the classified column to the dataset
print(hotel)
hotel.head(10)
hotel['Sentiment_Rating'].value_counts()#counting the positve and negative, Neutral reviews
#positive    1769
#neutral      172
#negative      59
hotel['Sentiment_Rating'].value_counts().plot.bar()
#we can say there are 1769 positive reviews and 59 negatives reviews, 172 Neutral reviews.

# library to clean data 
import re 

# Natural Language Tool Kit 
import nltk 

nltk.download('stopwords') 

# to remove stopword 
from nltk.corpus import stopwords 

# for Stemming propose 
from nltk.stem.porter import PorterStemmer 

# Initialize empty array 
# to append clean text 
corpus = [] 

# 2000 (reviews) rows to clean 
for i in range(0, 2000): 
	
	# column : "Review", row ith 
	review = re.sub('[^a-zA-Z]', ' ', hotel['reviews'][i]) 
	
	# convert all cases to lower cases 
	review = review.lower() 
	
	# split to array(default delimiter is " ") 
	review = review.split() 
	
	# creating PorterStemmer object to 
	# take main stem of each word 
	ps = PorterStemmer() 
	
	# loop for stemming each word 
	# in string array at ith row	 
	review = [ps.stem(word) for word in review 
				if not word in set(stopwords.words('english'))] 
				
	# rejoin all string array elements 
	# to create back into a string 
	review = ' '.join(review) 
	
	# append each string to create 
	# array of clean text 
	corpus.append(review) 

from sklearn.feature_extraction.text import CountVectorizer 
# To extract max 2000 feature. 
# "max_features" is attribute to 
# experiment with to get better results 
vect = CountVectorizer().fit(hotel.reviews)
vectorized = vect.transform(hotel.reviews)
cv = CountVectorizer(max_features = 2000) 

# X contains corpus (dependent variable) 
X = cv.fit_transform(corpus).toarray() 

# y contains answers if review is positive or negative 
y = hotel.iloc[:, 1].values 

#Applying SMOTE oversampling technique for removing class imbalance
from imblearn.over_sampling import SMOTE
over_sample =SMOTE (random_state =50,sampling_strategy ="all")
X_oversample,y_oversample =over_sample.fit_sample (vectorized,hotel['Sentiment_Rating'])

#count of sentiments or target classes
import collections,numpy
collections.Counter(y_oversample)
#Counter({'positive': 1769, 'neutral': 1769, 'negative': 1769})

#split data into train & test
def split_into_words(i):
	return (i.split(""))
	seed =7

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test =train_test_split(X_oversample,y_oversample,test_size=0.30)	
# Splitting the dataset into 
# the Training set and Test set 
#from sklearn.cross_validation import train_test_split 
from sklearn.model_selection import cross_val_score

# experiment with "test_size" 
# to get better results 

# Fitting Random Forest Classification 
# to the Training set 
from sklearn.ensemble import RandomForestClassifier 

# n_estimators can be said as number of 
# trees, experiment with n_estimators 
# to get better results 
model = RandomForestClassifier(n_estimators = 501, 
							criterion = 'entropy') 

model.fit(X_train, y_train) 

# Predicting the Test set results 
y_pred = model.predict(X_test) 
y_pred 

print("accuracy_score: ", f1_score(y_test,y_pred ,average='micro'))						

# Making the Confusion Matrix 
from sklearn.metrics import confusion_matrix 

cm = confusion_matrix(y_test, y_pred) 
cm 
#Confusion Matrix 
#array([[516,   0,   2],
 #      [  0, 518,  11],
 #     [  1,   3, 542]], dtype=int64)