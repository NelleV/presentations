import os
import numpy as np
import matplotlib
matplotlib.rc('text', usetex=True)

import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
y_min = y.min()
y -= y.min()
y_max = y.max()
y /= y.max()

shift = 0.5
scaling = 1.5
random_state = np.random.RandomState(seed=42)

data_x = np.linspace(0, 2*np.pi, 10).repeat(3)
data_y = np.sin(data_x)
data_y -= y_min
data_y /= y_max
data = scaling * data_y + shift
data += 0.2 * random_state.randn(*data.shape)

data_ = data_y + 0.2 * random_state.randn(*data.shape)


###############################################################################
# Plot data
fig, ax = plt.subplots(gridspec_kw={"right": 0.85})
ax.set_facecolor('none')
ax.plot(x, y, linewidth=2)
ax.plot(x, y, linewidth=2, color="#000000")
ax.plot(data_x, data_, linewidth=0, marker="o", markeredgecolor="#000000",
        markerfacecolor="none")
ax.plot(x, scaling * y + shift, color="#000000")
ax.plot(data_x, data, linewidth=0, marker="o", color="#000000")
ax.set_xticks([])
ax.set_yticks([])
ax.spines["right"].set_linewidth(0)
ax.spines["top"].set_linewidth(0)

ax.set_xlabel(r"\textbf{Temps}", fontweight="bold", fontsize="xx-large")
ax.set_ylabel(r"\textbf{Expression g\'enique}", fontweight="bold",
              fontsize="xx-large")
y_lim = ax.get_ylim()
try:
    os.makedirs("images")
except OSError:
    pass
fig.savefig("images/gene_data.pdf", transparent=True)
fig.savefig("images/gene_data.png", transparent=True)

###############################################################################
# Plot centroids
fig, ax = plt.subplots(gridspec_kw={"right": 0.85})
ax.set_facecolor('none')
ax.plot(x, y, linewidth=2, color="#AB0000")
ax.plot(x, scaling * y, color="#000000", linestyle="--")
ax.plot(x, scaling * y + shift, color="#000000")
ax.plot(data_x, data, linewidth=0, marker="o", color="#000000")

# Show the shift
x_ = y.argmax()
shift_x = [x[x_], x[x_]]
shift_y = np.array([scaling * y[x_], scaling * y[x_] + shift])
ax.plot(shift_x, shift_y, color="0.6")
ax.text(x[x_] + 0.1, shift_y.mean(), r"$\mathbf{b_i}$", fontsize="xx-large")

ax.text(x[-1] + 0.1, y[-1], r"$\mathbf{\mu(t)}$", fontsize="xx-large")
ax.text(x[-1] + 0.1, scaling * y[-1] + shift,
        r"$\mathbf{a_i \mu(t) + b_i}$", fontsize="xx-large")
ax.set_ylim(y_lim)
ax.spines["right"].set_linewidth(0)
ax.spines["top"].set_linewidth(0)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel(r"\textbf{Temps}", fontweight="bold", fontsize="xx-large")
ax.set_ylabel(r"\textbf{Expression g\'enique}", fontweight="bold",
              fontsize="xx-large")

fig.savefig("images/scaled_centroids.pdf", transparent=True)
fig.savefig("images/scaled_centroids.png", transparent=True)
