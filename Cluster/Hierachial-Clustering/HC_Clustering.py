import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


rd=pd.read_csv('Mall_Customers.csv')

X=rd.iloc[:,[3,4]].values


# using the dendrogram to find optimal number of clusters
import scipy.cluster.hierarchy as sch

#ward method is used to mininmize varient
dendrogram= sch.dendrogram(sch.linkage(X,method='ward'))
