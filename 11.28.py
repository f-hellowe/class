import matplotlib.pyplot as plt
import numpy as np

# x=np.arange(-50,51)
# y=x**2
# plt.plot(x,y,color='c',alpha=0.3,linestyle='--',linewidth=5,marker='o')
# plt.plot(x,y,'--o')
# plt.plot(x ,y,'-g')
# plt.plot(x,y,'-k')
# plt.plot(x,y,'-r')
# plt.plot(x,y,'x')
# plt.plot(x,y,'dr')

# plt.rcParams['font.sans-serif'] = ["LiSu"]
# plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['figure.dpi']=100
# plt.rcParams['figure.figsize']=(6,4)

# fig = plt.figure('f3', figsize=(6,4), facecolor='red')
# x = np.arange(0,20)
# y = x**2
# y1=x*2
# plt.rcParams['font.sans-serif'] = ["LiSu"]
# plt.rcParams['axes.unicode_minus'] = False
# ax1 = fig.add_axes([0,0,1,1])
# ax1.set_title('区域1')
# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax1.plot(x, y, label='ax1')
# ax1.legend()
# ax2 = fig.add_axes([0.4, 0.4, 0.5, 0.5])
# ax2.set_title('区域2')
# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax2.plot(x, y1, label='ax2')
# ax2.legend()


plt.rcParams['font.sans-serif'] = ["LiSu"]
plt.rcParams['axes.unicode_minus'] = False
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('Sin(x)')
plt.xlabel('x1')
plt.ylabel('y1')
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cos(x)')
plt.xlabel('x2')
plt.ylabel('y2')
plt.show()

