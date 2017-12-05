import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

stats = np.array([15, 38])
with plt.xkcd():
    fig, ax = plt.subplots()
    ax.bar(np.arange(2) - 0.5, stats, color="#000000")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.set_xticklabels(("0", "Attendants", "Applicants"), fontsize="large")
    ax.set_ylabel("Nationality", fontsize="large")
    fig.savefig("fig_2.png")
