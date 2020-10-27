# Function to manually input
import pandas as pd
import math
import time


def manual(start_time, end_time):

    work_time = (pd.to_datetime(end_time).timestamp() - pd.to_datetime(start_time).timestamp()) / 3600

    df_name = "/Users/minhpham/Desktop/Work/Python/clock_in/clock_in_df.csv"

    df = pd.read_csv(df_name)
    df = df.set_index('start_time')
    pay_rate = df.iloc[-1]['pay_rate'] * math.pow(1.0024, (work_time / 8))
    money_made = pay_rate * work_time
    asset = df.iloc[-1]['asset'] + money_made

    # pandas .csv save
    df.loc[start_time] = [end_time, work_time, pay_rate, money_made, asset]

    time.sleep(2)

    df.to_csv(df_name)

    start_time = time.ctime(pd.to_datetime(start_time).timestamp() + 3600 * 7)
    end_time = time.ctime(pd.to_datetime(end_time).timestamp() + 3600 * 7)

    txt_name = "/Users/minhpham/Desktop/Work/Python/clock_in/book_keeping.txt"

    with open(txt_name, "a") as f:
        f.write(f"\n\n{start_time}")
        f.write(f"\nStart time:    {start_time}")
        f.write(f"\nEnd time:    {end_time}")

        # work_time in hours
        hours = int(work_time)  # hours
        minutes = int((work_time - int(work_time)) * 60)  # minutes

        f.write(f"\nTotal work time:    {round(hours)} hours {round(minutes)} minutes")
        f.write(f"\nMoney earned:    ${round(money_made, 2)}")
        f.write(f"\nPay rate:    ${pay_rate}")
        f.write(f"\nOwned:    ${round(asset, 2)}")
