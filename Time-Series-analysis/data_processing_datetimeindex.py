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

#setting up new index argument
df.set_index(rng, inplace=True)


st=df.Close
st.plot()


#Generating frequency on missing days or weekends, it will carry over the last
#date figure

pt=st.asfreq('D', method='pad')


#When you only know about starting date, freq='H'

rng=pd.date_range(start='6/1/2017', periods=72, freq='B')


# it is useful when we have to do unit, we can generate fake dataset using this
 
import numpy as np
ts=pd.Series(np.random.randint(1,10,len(rng)), index=rng)


# using custom calendar (US calendar)

from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

usb=CustomBusinessDay(calender=USFederalHolidayCalendar())


# Creating a specific calendar
from pandas.tseries.holiday import  AbstractHolidayCalendar, nearest_workday, Holiday
class myBirthdayCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('Vikram pal Birthday', month=9, day=7)
    ]


myc=CustomBusinessDay(calendar=myBirthdayCalendar())

rng=pd.date_range(start='6/1/2017', periods=72, freq=myc)


# changing week days range such for Eygpht sunday is working day and fri and sat
# are holiday
b=CustomBusinessDay(weekmask='Sun Mon Tue Wed Thu')
rng=pd.date_range(start='6/1/2017', periods=72, freq='B')









