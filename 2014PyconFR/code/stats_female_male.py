import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

stats_ = np.array([13, 36, 17, 132])

with plt.xkcd():
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.bar(np.arange(0, 4, 2) - 0.5, stats_[::2], color="#000000")
    ax.bar(np.arange(1, 4, 2) - 0.55, stats_[1::2], color="darkblue")

    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.set_xticklabels(
        ("0", "Female Attendants", "Female Applicants", "Male Attendants",
         "Male Applicants"), fontsize="large")
    ax.set_ylabel("Nationality", fontsize="large")
    fig.savefig("fig_3.png")
