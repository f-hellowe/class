from pylab import *
import matplotlib.pyplot as plt

G = plt.GridSpec(2, 3)
countries = ['挪威', '德国', '美国', '中国', '奥地利']
gold_medal = [13, 10, 8, 7, 6]
silver_medal = [7, 6, 7, 4, 7]
bronze_medal = [8, 4, 4, 2, 4]
axes_1 = subplot(G[0, :])
x = np.arange(len(countries))
width = 0.2
gold_x = x
silver_medal_x = x + width
bronze_medal_x = x + 2 * width
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(gold_x, gold_medal, width=0.2, color='gold', label='金')
plt.bar(silver_medal_x, silver_medal, width=0.2, color='Lime', label='银')
plt.bar(bronze_medal_x, bronze_medal, width=0.2, color='brown', label='铜')
plt.xticks(x + width, countries, color='red')
plt.legend()
for i in range(len(countries)):
    plt.text(gold_x[i], gold_medal[i], gold_medal[i], va='bottom', ha='center')
    plt.text(silver_medal_x[i], silver_medal[i], silver_medal[i], va='bottom', ha='center')
    plt.text(bronze_medal_x[i], bronze_medal[i], bronze_medal[i], va='bottom', ha='center')
ax_2 = subplot(G[1,0])
plt.bar(range(len(gold_medal)), gold_medal,tick_label=countries,color='gold')
ax_3 = subplot(G[1,-2])
plt.bar(range(len(silver_medal)), silver_medal,tick_label=countries,color='Lime')
ax_4 = subplot(G[1,-1])
plt.bar(range(len(bronze_medal)), bronze_medal,tick_label=countries,color='brown')
plt.show()
