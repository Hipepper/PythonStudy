import datetime as dt
import pandas as pd
df = pd.DataFrame({'date':[42580.3333333333, 43318]})
df['real_date'] = pd.TimedeltaIndex(df['date'], unit='d') + dt.datetime(1899, 12, 30)

print(df)

print(pd.to_datetime('1899-12-30') + pd.to_timedelta(32331.06, 'D'))
print(pd.to_datetime('1899-12-30') + pd.to_timedelta(43318, 'D'))
print(dt.datetime(1899, 12, 30) + pd.to_timedelta(43318, 'D'))