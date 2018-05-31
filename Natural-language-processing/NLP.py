# -*- coding: utf-8 -*-
"""
Created on Mon May 28 23:27:49 2018

@author: Vikram
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#ignoring double quote in dataset // delimiter for TSV file.
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)

# steaming for only present form of verb and translating past verb to present.
#Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus=[]
for i in range(0,1000):
    review=re.sub('[^a-zA-Z]',' ', dataset['Review'][i] )
    review=review.lower()
    review=review.split()
    ps=PorterStemmer()
    review=[ ps.stem(word) for word in review if not word in stopwords.words('english')]
    review=' '.join(review)
    corpus.append(review)




# Creating the bag of words model
# taking or refining unique and different words. 
# sparse matric
    
from sklearn.feature_extraction.text import CountVectorizer
cv= CountVectorizer(max_features=1500)
X=cv.fit_transform(corpus).toarray()
y=dataset.iloc[:,1].values



# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)



# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)



#fitting the classifier to the training set
from sklearn.naive_bayes import GaussianNB
classifier= GaussianNB()
classifier.fit(X_train,y_train)


#Predicting the test set results
y_pred=classifier.predict(X_test)


#making the confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test, y_pred)

