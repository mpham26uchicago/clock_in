# Remember to redirect to the right file

import tkinter as tk
import time
import pandas as pd
import math
# import total_time
import manual_clock_in

root = tk.Tk()

a = 0


def save(start, end):
    # After first DataFrame has been created

    df_name = "/Users/minhpham/Desktop/Work/Python/clock_in/clock_in_df.csv"
    df = pd.read_csv(df_name)

    df = df.set_index('start_time')

    start_time = pd.to_datetime(time.ctime(start))
    end_time = pd.to_datetime(time.ctime(end))
    work_time = (end - start) / 3600
    pay_rate = df.iloc[-1]['pay_rate'] * math.pow(1.0024, (work_time / 8))
    money_made = pay_rate * work_time
    asset = df.iloc[-1]['asset'] + money_made

    # pandas .csv save
    df.loc[start_time] = [end_time, work_time, pay_rate, money_made, asset]

    df.to_csv(df_name)

    # .txt file save

    txt_name = "/Users/minhpham/Desktop/Work/Python/clock_in/book_keeping.txt"

    with open(txt_name, "a") as f:
        f.write(f"\n\n{time.ctime(start)}")
        f.write(f"\nStart time:    {time.ctime(start)}")
        f.write(f"\nEnd time:    {time.ctime(end)}")

        # work_time in hours
        hours = int(work_time)  # hours
        minutes = int((work_time - int(work_time)) * 60)  # minutes

        f.write(f"\nTotal work time:    {round(hours)} hours {round(minutes)} minutes")
        f.write(f"\nMoney earned:    ${round(money_made, 2)}")
        f.write(f"\nPay rate:    ${pay_rate}")
        f.write(f"\nOwned:    ${round(asset, 2)}")

        # Return information for tkinter
        # save tuple[ 0: hours, 1: minutes, 2: money_made, 3: asset, 4: pay_rate ]

    return hours, minutes, money_made, asset, pay_rate


def clockin():
    global a, start, end, label2, label4, label5, label6, label7, label8

    df_name = "/Users/minhpham/Desktop/Work/Python/clock_in/clock_in_df.csv"
    df = pd.read_csv(df_name)

    password = "Epsilon5"

    if a == 0:

        mdp = entry.get()
        start = time.time()
        label2 = tk.Label(text="")
        label2.pack()
        if str(mdp) == str(password):
            label4 = tk.Label(text = f"You clock in at {time.ctime()}")
            label4.pack()
            label5 = tk.Label(text=f"Your total asset value is $ {round(df.iloc[-1]['asset'], 2)}"
                                   f", your pay rate today is $ {round(df.iloc[-1]['pay_rate'], 2)}")
            label5.pack()

            a += 1

    elif (a % 2 == 0) & (a > 0):

        label2.pack_forget()
        label4.pack_forget()
        label5.pack_forget()
        label6.pack_forget()  # Turn off clock out
        label7.pack_forget()
        label8.pack_forget()

        mdp = entry.get()
        start = time.time()
        label2 = tk.Label(text="")
        label2.pack()
        if str(mdp) == str(password):
            label4 = tk.Label(text=f"You clock in at {time.ctime()}")
            label4.pack()
            label5 = tk.Label(text=f"Your total asset value is $ {round(df.iloc[-1]['asset'], 2)}"
                                   f", your pay rate today is $ {round(df.iloc[-1]['pay_rate'], 2)}")
            label5.pack()

            a += 1

    elif a % 2 == 1:

        mdp = entry.get()
        if str(mdp) == str(password):
            label6 = tk.Label(text=f"You clock out at {time.ctime()}")
            label6.pack()

            end = time.time()

            # file entry
            save_tuple = save(start, end)

            label7 = tk.Label(text=f"You've worked for {save_tuple[0]} hours and {round(save_tuple[1])}"
                                   f" minutes and earned $"
                                   f'{round(save_tuple[2], 2)}')
            label7.pack()

            label8 = tk.Label(text=f"Your total asset value is $ {round(save_tuple[3], 2)}"
                                   f", your pay rate today is $ {round(save_tuple[4], 2)}")
            label8.pack()

            a += 1


label1 = tk.Label(text="Please clock in")
entry = tk.Entry()
button = tk.Button(root, text="Enter", command=clockin)

label1.pack()
entry.pack()
button.pack()
root.mainloop()

print("GUI Program stopped")

time.sleep(3)

''' print(f"\nYou worked for {round(total_time.total_work_time, 1)} hours today and made "
      f"${round(total_time.money_made,2)}")'''

if input("Do you want to clock in manually  ") == "yes":
    manual_clock_in.manual(input("Input Start Time   # 2020-01-01 00:00:00   (year, month, day) (hour, minutes, "
                                 "seconds)  "),
                           input("Input End Time   # 2020-01-01 00:00:00   (year, month, day) (hour, minutes, "
                                 "seconds)  "))
else:
    pass
