import pandas as pd

df=pd.read_csv('walmartdataset.csv')

df.set_index('Line Item', inplace=True)

df=df.T

df.index=pd.PeriodIndex(df.index, freq='Q-JAN')


df['Start Date']=df.index.map(lambda x:x.start_time)

df['End Date']=df.index.map(lambda x:x.end_time)





