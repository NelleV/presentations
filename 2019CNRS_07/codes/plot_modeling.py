import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rc('text', usetex=True)


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
y_min = y.min()
y -= y.min()
y_max = y.max()
y /= y.max()

shift = 1
scaling = 2
random_state = np.random.RandomState(seed=42)

data_x = np.linspace(0, 2*np.pi, 10).repeat(3)
data_y = np.sin(data_x)
data_y -= y_min
data_y /= y_max
data = scaling * data_y + shift
data += 0.2 * random_state.randn(*data.shape)

###############################################################################
# Just the data
fig, ax = plt.subplots(gridspec_kw={"right": 0.85})
ax.set_facecolor('none')
ax.plot(data_x, data, linewidth=0, marker="o", color="#000000")
ax.spines["right"].set_linewidth(0)
ax.spines["top"].set_linewidth(0)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel(r"\textbf{Temps}", fontweight="bold", fontsize="xx-large")
ax.set_ylabel(r"\textbf{\'Expression g\'enique}", fontweight="bold",
              fontsize="xx-large")

try:
    os.makedirs("images")
except OSError:
    pass
fig.savefig("images/splines_data.pdf", transparent=True)
fig.savefig("images/splines_data.png", transparent=True)

###############################################################################
# Just the data

fig, ax = plt.subplots(gridspec_kw={"right": 0.85})
ax.set_facecolor('none')
ax.plot(x, scaling * y + shift, color="#000000")
ax.plot(data_x, data, linewidth=0, marker="o", color="#000000")
ax.spines["right"].set_linewidth(0)
ax.spines["top"].set_linewidth(0)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel(r"\textbf{Temps}", fontweight="bold", fontsize="xx-large")
ax.set_ylabel(r"\textbf{\'Expression g\'enique}", fontweight="bold",
              fontsize="xx-large")

fig.savefig("images/splines_modeling.pdf", transparent=True)
fig.savefig("images/splines_modeling.png", transparent=True)
