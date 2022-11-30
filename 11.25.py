import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ["LiSu"]
plt.rcParams['axes.unicode_minus'] = False
time = np.arange(2000, 2020).astype(np.str_)
sale = [109, 150, 172, 260, 273, 333, 347, 393, 402, 446, 466, 481, 499, 504, 513, 563, 815, 900, 930, 961]
plt.title('销量表')
plt.xlabel('日期')
plt.ylabel('销量')
plt.xticks(range(0, len(time), 2), rotation=60, color='red')
plt.plot(time, sale, linewidth=3, label='销量')
plt.legend(loc='lower right')
for x, y in zip(time, sale):
    plt.text(x, y, '%s元' % y, horizontalalignment='center')
plt.show()


# dates=np.arange(1991,2021)
# sales=np.random.randint(50,1000,size=len(dates))
# plt.xticks(np.arange(dates.min(),dates.max()+2.2))
# plt.plot(dates,sales)
# plt.show()

# x=np.arange(0,20)
# y=np.random.randint(10,50,size=len(x))
#
# plt.rcParams['font.sans-serif'] = ["LiSu"]
# plt.title('随机')
# plt.xlabel('x轴')
# plt.ylabel('y轴')
# plt.plot(x,y)
# plt.grid(True,linestyle='--',color='green',linewidth='1',axis='y')
# plt.show()

# x = np.arange(-50, 51)
# y = x ** 2
# a = plt.gca()  # 获取当前的坐标值
# # 通过坐标轴spines,top,bottom,left,right
# # set_color 设置颜色 none:空
# a.spines['right'].set_color('green')
# a.spines['top'].set_color('red')
# # 移动轴到指定位置
# # 在这里，postion位置参数有三种 data outward axes
# # axes:0.0-1.0之间的值，整个轴的比例
# a.spines['left'].set_position(('axes', 0.5))
# # data: 表示按数值移动，其数字代表移动到v轴的刻度值
# a.spines['bottom'].set_position(('data', 0))
# plt.rcParams['axes.unicode_minus'] = False
# plt.plot(x, y)
# plt.show()



# x = np.arange(-50,51)
# y=x**2
# plt.rcParams["figure.dpi"]=500
# plt.rcParams["figure.figsize"]=(8.0,4.0)
# plt.plot(x,y)
# plt .show()