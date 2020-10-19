import tushare as ts
import matplotlib.pyplot as plt

stock1 = ts.get_hist_data("600848")
time = stock1.index
stock1 = stock1.values
stock2 = ts.get_hist_data("600847").values
stock3 = ts.get_hist_data("600850").values
time_ls = []
xaxis = [i for i in range(30)]
for i in range(30):
    if i%5 == 0:
        time_ls.append(time[i])
    else:
        time_ls.append(" ")
plt.plot(xaxis,stock1[0:30,2])
plt.plot(xaxis,stock2[0:30,2])
plt.plot(xaxis,stock3[0:30,2])
plt.xticks(xaxis,time_ls,rotation = 45)
plt.show()
#有个问题，横坐标全挤在一起了。
#晚点有时间再改。
