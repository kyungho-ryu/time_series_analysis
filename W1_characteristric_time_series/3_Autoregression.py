import numpy as np
import matplotlib.pyplot as plt
import math

# White noise
w = np.random.normal(0,1,150)

# Autoregressive data generation
# x_t = -.9x_{t-2} + w_t
def gernerate_AR1(n) :
    x = [0 for _ in range(n)]
    for i in range(n) :
        if (i-2) >= 0 :
            x[i] = -0.9 * x[i-2] + w[i]
        else :
            x[i] = w[i]

    return x[50:n+1]

def gernerate_MA(x) :
    v = [x[i] for i in range(len(x))]
    for i in range(len(v)) :
        if (i-3) >= 0 :
            v[i] = (x[i] + x[i-1] + x[i-2] + x[i-3])/4

    return v

x = gernerate_AR1(150)
v = gernerate_MA(x)
fig, ax = plt.subplots(figsize=(10,5))

ax.set_title('Autoregression', fontsize=15)
ax.plot(x)
ax.plot(v, '--')
ax.legend(['AR','MA'])

plt.show()
