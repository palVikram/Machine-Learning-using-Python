import pandas as pd

dates = ['2017-01-05', 'Jan 5, 2017', '01/05/2017', '2017.01.05', '2017/01/05','20170105']
pd.to_datetime(dates)

#European style dates with day first
pd.to_datetime('30-12-2016')

pd.to_datetime('5-1-2016', dayfirst=True)


#Custom date time format
pd.to_datetime('2017$01$05', format='%Y$%m$%d')

pd.to_datetime('2017#01#05', format='%Y#%m#%d')
               
#Handling invalid dates
pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='ignore')

pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='coerce')


#Epoch or Unix time means number of seconds that have passed since Jan 1, 1970 00:00:00 UTC time
current_epoch = 1501324478
pd.to_datetime(current_epoch, unit='s')


t = pd.to_datetime([current_epoch], unit='s')

t.view('int64')


