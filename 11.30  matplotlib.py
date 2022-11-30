import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif'] = 'SimHei'
# plt.rcParams['axes.unicode_minus'] = False
# plt.figure(figsize=(10, 10))
# x = np.linspace(0, 2)
# y = x ** 2
# plt.subplot(211)
# plt.plot(x, y)
# plt.title("第一幅子图")
# plt.subplot(234)
# plt.plot(x, y)
# plt.title("第二幅子图")
# plt.subplot(235)
# plt.plot(x, y)
# plt.title("第三幅子图")
countries = ['挪威', '德国', '美国', '中国', '奥地利']
gold_medal = [13, 10, 8, 7, 6]
silver_medal = [7, 6, 7, 4, 7]
bronze_medal = [8, 4, 4, 2, 4]
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
plt.show()
