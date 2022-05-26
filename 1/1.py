from cmath import exp
import numpy as np
import matplotlib.pyplot as plt
import math


y = np.random.uniform(low=0, high=1, size=1000)

x = []
for i in y:
    if i <= 0.5:
        x.append(math.log(2 * i) / math.sqrt(2))
    else:
        x.append(-1 * math.log(2 - 2 * i) / math.sqrt(2))

# 绘制样本顶点
plt.plot(x, [exp((-1) * math.sqrt(2) * abs(i)) / math.sqrt(2) for i in x], ".")
plt.show()
