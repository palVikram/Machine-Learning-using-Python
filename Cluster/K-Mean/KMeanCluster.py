import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


rd=pd.read_csv('Mall_Customers.csv')

X=rd.iloc[:,[3,4]].values


from sklearn.cluster import KMeans
wcss=[]

#calculating number of cluster by Elbow method.
for i in range(1,11):
    kmean=KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=300,random_state=0)
    kmean.fit(X)
    #compte sum of square in cluster we are suing kmean.inertia_
    wcss.append(kmean.inertia_)

plt.plot(range(1,11), wcss )
plt.title('the elbow method')
plt.xlabel('number of clusters')
plt.ylabel('wcss')
plt.show()

#fitting number of cluster to KMEAN model
kmean=KMeans(n_clusters=5, init='k-means++', n_init=10, max_iter=300,random_state=0)
y_mean=kmean.fit_predict(X)



#visualising the cluster
plt.scatter(X[y_mean==0,0],X[y_mean==0,1],s=100,c='red',label='Careful')
plt.scatter(X[y_mean==1,0],X[y_mean==1,1],s=100,c='blue',label='Standard')
plt.scatter(X[y_mean==2,0],X[y_mean==2,1],s=100,c='green',label='Target')
plt.scatter(X[y_mean==3,0],X[y_mean==3,1],s=100,c='cyan',label='Careful')
plt.scatter(X[y_mean==4,0],X[y_mean==4,1],s=100,c='magenta',label='Sensible')


plt.scatter(kmean.cluster_centers_[:,0],kmean.cluster_centers_[:,1],s=300, c='yellow',label='Centriod')
plt.title('Clusters of Clients')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()










