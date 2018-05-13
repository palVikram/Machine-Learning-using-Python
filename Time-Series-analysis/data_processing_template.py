# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Data Preprocessing 

import numpy as np  # for mathematical 
import matplotlib as plt # plotting 
import pandas as pd # fetching the dataset


# importing the dataset
df=pd.read_csv('weather_data_cities.csv')

new_df=df.fillna({
        'temperature':0,
        'windspeed':0,
        'event':'no event'
        })

############################################
new_df=df.fillna(method='ffill',limit=1)

new_df=df.interpolate()

new_df=df.dropna()


new_df=df.dropna(how='all')

new_df=df.dropna(thresh=2)

dt=pd.date_range("01-01-2017","01-11-2017")
idx=pd.DatetimeIndex(dt)


new_df=df.replace(-9999,np.abs)

new_df=df.replace([-9999,-8888],np.NaN)


new_df=df.replace({
        'temperature':-9999,
        'windspeed':-88888,
        'event':0
      }, np.NaN)
      
new_df=df.replace({
        -9999:np.NaN,
        -88888:np.NaN,
        'no event': 'Sunny'
        })

new_df=df.replace({
        'temperature':'[A-Za-z]',
        'windspeed':'[A-Za-z]',
      },'',regex=True)

##############################################

g=df.groupby('city')

for city, city_df in g:
    print(city)
    print(city_df)
    
g.get_group('mumbai')


g.max()

g.mean()

g.describe()


#################
#%matplotlib inline
#g.plot()

india_weather=pd.DataFrame({
        "city":['delhi','pune','mumbai'],
        "temperature":[44,23,32],
        "humidity":[80,90,70]
        }) 
    

us_weather=pd.DataFrame({
        "city":['new york','chicago','orlando'],
        "temperature":[44,23,32],
        "humidity":[80,90,70]
        }) 
    
    
df=pd.concat([india_weather, us_weather])



df=pd.concat([india_weather, us_weather], ignore_index=True)

df=pd.concat([india_weather, us_weather], keys=["a_set", "b_set"])


k=pd.Series(['humid','dry','rain'], name="events")

s=pd.concat([india_weather,k], axis=1)



## merging two csv together.
a=pd.DataFrame({
        "city":['delhi','pune','mumbai'],
        "temperature":[40,20,30],
        "humidity":[81,90,79]
        }) 
    

b=pd.DataFrame({
        "city":['delhi','pune','mumbai'],
        "temperature":[44,23,32],
        "humidity":[80,90,70]
        }) 
    
df3=pd.merge(a,b, on="city")



####  Pivot 
df.set_index('date')
g=df.pivot(index="date", columns='city', values="windspeed")


f=df.pivot_table(index="date", columns='city', margins=True)

df['date']= pd.to_datetime(df['date'])

dc=df.pivot_table(index=pd.Grouper(freq='M', key='date',), columns='city')


pf=pd.melt(df, id_vars=["?day"], var_name="city",value_name="temperature")




pt=pd.crosstab(df.event, df.city, margins=True)











    
