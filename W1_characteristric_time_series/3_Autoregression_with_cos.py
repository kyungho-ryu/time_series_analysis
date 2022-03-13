import numpy as np
import matplotlib.pyplot as plt
import math

# White noise
w = np.random.normal(0,1,150)

# Autoregressive data generation
# x_t = cos(2*\pi*t/4)
def gernerate_AR2(n) :
    x = [0 for _ in range(n)]
    for t in range(n) :
        x[t] = math.cos(2 * math.pi * t /4)

    return x

def gernerate_MA(x) :
    v = [x[i] for i in range(len(x))]
    for i in range(len(v)) :
        if (i-3) >= 0 :
            v[i] = (x[i] + x[i-1] + x[i-2] + x[i-3])/4

    return v

x = gernerate_AR2(100)
v = gernerate_MA(x)
fig, ax = plt.subplots(figsize=(10,5))

ax.set_title('Autoregression with cos', fontsize=15)
ax.plot(x)
ax.plot(v, '--')
ax.legend(['AR','MA'])

#plt.show()
plt.savefig('AR_with_cos.png')
