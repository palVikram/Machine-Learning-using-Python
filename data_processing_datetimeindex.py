import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('appl_withoutdates.csv')


### check date is string or not. If yes, then parse it.

type(df.Date[0])


df["2017-01"].Close.mean()




df["2017-01-07":"2017-01-01"]

sf=df.Close.resample('M').mean()
sf.plot()

# date range 

rng=pd.date_range(start='6/1/2017', end='6/30/2017', freq='B')

#setting up new argument
df.set_index(rng, inplace=True)




