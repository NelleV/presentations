
import os
import numpy as np
import matplotlib
matplotlib.rc('text', usetex=True)

import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

shift = 1
scaling = 2
random_state = np.random.RandomState(seed=42)

y = scaling * y + 1
data_x = np.linspace(0, 2*np.pi, 10).repeat(3)
data = scaling * np.sin(data_x) + shift
data += 0.5 * random_state.randn(*data.shape)

fig, ax = plt.subplots()
ax.plot(x, y, color="#000000")
ax.plot(data_x, data, linewidth=0, marker="o", color="#000000")

# Show the shift
x_ = y.argmax()
shift_x = [x[x_], x[x_]]
shift_y = np.array([scaling * y[x_], scaling * y[x_] + shift])

ax.spines["right"].set_linewidth(0)
ax.spines["top"].set_linewidth(0)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel(r"\textbf{Time}", fontweight="bold", fontsize="large")
ax.set_ylabel(r"\textbf{Gene Expression}", fontweight="bold", fontsize="large")

try:
    os.makedirs("images")
except OSError:
    pass

fig.savefig("images/splines_fit.png")
fig.savefig("images/splines_fit.pdf")
fig.savefig("images/splines_fit.eps")

