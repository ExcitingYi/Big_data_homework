import matplotlib.pyplot as plt
import tushare as ts
plt.rcParams['font.sans-serif'] = ['KaiTi']
stocks=ts.get_stock_basics()
stocks = stocks.values
ind_set = set(stocks[:,2])
ls_ind = []
ls_num = []
j = 0
#print(stocks[stocks[:,1] == "电气设备"].shape[0])
#print(stocks[stocks[:,1] == "房产开发"].shape)
for i in ind_set:
    ls_ind.append(i)
    ls_num.append(stocks[stocks[:,2] == i].shape[0])

plt.title("各地区占比")
plt.pie(ls_num,labels = ls_ind)
plt.show()
