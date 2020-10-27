import datetime
import pandas as pd
import time

# Open file and prepare data

df_name = "/Users/minhpham/Desktop/Work/Python/clock_in/clock_in_df.csv"

df = pd.read_csv(df_name)

df = df.set_index('start_time')

df.index = pd.to_datetime(df.index, format='%Y-%m-%d')

# Sorting Data
start_date = datetime.date(2020, 6, 8)  # Start date (year, month, day)

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day

end_date = datetime.date(year, month, day)  # End date (year, month, day)

delta = datetime.timedelta(days=1)

# Separate DataFrame for processed info
df2 = pd.DataFrame([], columns=['Date', 'Work Time', 'Money Made'])
df2 = df2.set_index('Date')

while start_date <= end_date:
    # Adding up all the work time each day
    work_time = df.loc[start_date:(start_date + delta)]['work_time'].sum()

    # Adding up the money made each day
    money = df.loc[start_date:(start_date + delta)]['money_made'].sum()

    df2.loc[start_date] = [work_time, money]

    start_date += delta

# Sample processed DataFrame
total_work_time = df2["Work Time"].iloc[-1]
money_made = df2["Money Made"].iloc[-1]