import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

stats = np.array([30, 168])
with plt.xkcd():
    fig, ax = plt.subplots()
    ax.bar(np.arange(2) - 0.5, stats, color="#000000")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.set_xticklabels(("0", "Attendants", "Applicants"), fontsize="large")
    ax.set_ylabel("Number", fontsize="large")
    fig.savefig("fig_1.png")
