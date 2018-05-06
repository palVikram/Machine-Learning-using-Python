import pandas as pd
import numpy as np


#yearly period
y= pd.Period('2016')
y.start_time
y.end_time
# for next year
y+1


# monthly period
m= pd.Period('2011-1', freq='M' )
m.start_time
m.end_time

#daily period
d= pd.Period('2017-02-28', freq='D')
d.start_time
d.end_time


#For quarter 
q=pd.Period('2017Q1', freq='Q-JAN')

q2=pd.Period('2018Q2', freq='Q-JAN')


idx=pd.period_range('2011', periods=10, freq="Q-JAN")

ps=pd.Series(np.random.randn(len(idx)), idx)