
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

scaling = 1
shift = -2

x = np.linspace(0, 2*np.pi, 100)
y = scaling * np.ones(x.shape) + shift
data_x = np.linspace(0, 2*np.pi, 10).repeat(3)
data = scaling * np.ones(data_x.shape) + shift
data += 0.5 * random_state.randn(*data.shape)

ax.plot(x, y, color="#000000", linestyle="--")
ax.plot(data_x, data, linewidth=0, marker="o", color="#ffffff",
        markeredgecolor="#000000", markeredgewidth=1)

ax.spines["right"].set_linewidth(0)
ax.spines["top"].set_linewidth(0)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel(r"\textbf{Time}", fontweight="bold", fontsize="large")
ax.set_ylabel(r"\textbf{Gene Expression}", fontweight="bold", fontsize="large")
ax.set_title(r"\textbf{DE}", fontweight="bold", fontsize="x-large")

try:
    os.makedirs("images")
except OSError:
    pass
fig.savefig("images/splines_DE.png")

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

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

shift = 0.8
scaling = 2.2

y = scaling * y + 1
data_x = np.linspace(0, 2*np.pi, 10).repeat(3)
data = scaling * np.sin(data_x) + shift
data += 0.5 * random_state.randn(*data.shape)


ax.plot(x, y, color="#000000", linestyle="--")
ax.plot(data_x, data, linewidth=0, marker="o", color="#ffffff",
        markeredgecolor="#000000", markeredgewidth=1)

ax.spines["right"].set_linewidth(0)
ax.spines["top"].set_linewidth(0)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel(r"\textbf{Time}", fontweight="bold", fontsize="large")
ax.set_ylabel(r"\textbf{Gene Expression}", fontweight="bold", fontsize="large")
ax.set_title(r"\textbf{not DE}", fontweight="bold", fontsize="x-large")

try:
    os.makedirs("images")
except OSError:
    pass
fig.savefig("images/splines_not_DE.png")

