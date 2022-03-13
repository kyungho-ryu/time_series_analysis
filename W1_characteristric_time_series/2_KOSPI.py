from pandas_datareader import data
from datetime import datetime
import collections
import matplotlib.pyplot as plt

start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 12, 31)

kospi_df = data.get_data_yahoo("^KS11", start_date, end_date)

def get_avg(data, current, period) :
    temp =0

    if current +1 < period : return None
    for i in range(len(data)) :
        temp += data[i]

    return temp / len(data)

def get_MA_from_innerFunc(kospi_df):
    a = kospi_df['Close'].rolling(5).mean()
    b = kospi_df['Close'].rolling(20).mean()
    c = kospi_df['Close'].rolling(60).mean()

    return a,b,c

def get_MA_from_actualCalc(kospi_df):
    kospi_df['MA5'] = kospi_df['Close']

    list_5 = [0 for _ in range(len(kospi_df['Close']))]
    list_20 = [0 for _ in range(len(kospi_df['Close']))]
    list_60 = [0 for _ in range(len(kospi_df['Close']))]

    temp_5 = collections.deque(5*[0], 5)
    temp_20 = collections.deque(20*[0], 20)
    temp_60 = collections.deque(60*[0], 60)
    for i in range(0, len(kospi_df["Close"])) :
        temp_5.append(kospi_df["Close"][i])
        temp_20.append(kospi_df["Close"][i])
        temp_60.append(kospi_df["Close"][i])

        list_5[i] = get_avg(temp_5, i, 5)
        list_20[i] = get_avg(temp_20, i, 20)
        list_60[i] = get_avg(temp_60, i, 60)

    return list_5, list_20, list_60


MA5,MA20,MA60 = get_MA_from_actualCalc(kospi_df)


fig, ax = plt.subplots(figsize=(10,5))

ax.set_title('KOSPI', fontsize=15)
ax.set_ylabel("KOSPI")
ax.set_xlabel("Date time")
print(kospi_df)
ax.plot(kospi_df.index, kospi_df['Close'])
ax.plot(kospi_df.index, MA5)
ax.plot(kospi_df.index, MA20)
ax.plot(kospi_df.index, MA60)
ax.legend(['Value','MA5','MA20', "MA60"])
#plt.show()
plt.savefig('KOSPI.png')




