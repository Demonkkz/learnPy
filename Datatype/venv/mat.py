import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,200)
y = np.sin(x)
# plt.plot(x,y,'--')
# plt.plot(x,np.cos(x))

# fig = plt.figure() # 用于保存图像
#
# plt.subplot(2,1,1)
# plt.plot(x,np.cos(x))
#
# plt.savefig('first.png')
# plt.show()
# plt.plot(x,np.cos(x),'o')

# 加标题
plt.plot(x,y,label='sin(x)')
plt.plot(x,np.cos(x),label='cox(x)')
plt.legend()
plt.show()

