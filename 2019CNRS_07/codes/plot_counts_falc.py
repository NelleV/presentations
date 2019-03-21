import numpy as np

from iced import io
from iced import filter
from iced import normalization
from iced import utils

from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt


lengths = io.load_lengths("data/trophozoites_10000_raw.bed")
counts = io.load_counts("data/trophozoites_10000_raw.matrix", lengths=lengths)
counts = utils.from_sparse_to_dense(counts)

normed = filter.filter_low_counts(counts, remove_all_zeros_loci=True,
                                  sparsity=False)
normed = normalization.ICE_normalization(normed)

normed, l = utils.extract_sub_contact_map(normed, lengths, [6, 7])
to_rm = normed.sum(axis=0) == 0
normed[to_rm] = np.nan
normed[:, to_rm] = np.nan

fig, ax = plt.subplots()
m = ax.matshow(np.log(normed+1), cmap="RdYlBu_r", vmax=5)
ax.set_xticks([])
ax.set_yticks([])
l = np.concatenate([[0], l])
[ax.axhline(i, color="0", linestyle="--") for i in l.cumsum()]
[ax.axvline(i, color="0", linestyle="--") for i in l.cumsum()]
ax.set_xlim(-20, l.sum()+20)
ax.set_ylim(-20, l.sum()+20)
ax.spines["top"].set_alpha(0)
ax.spines["bottom"].set_alpha(0)
ax.spines["left"].set_alpha(0)
ax.spines["right"].set_alpha(0)
ax.text(-20, 72.5, "Chr 7", rotation=90, fontweight="bold",
        horizontalalignment="center", verticalalignment="center")
ax.text(-20, 217, "Chr 8", rotation=90, fontweight="bold",
        horizontalalignment="center", verticalalignment="center")

ax.text(72.5, -20, "Chr 7", fontweight="bold",
        horizontalalignment="center", verticalalignment="center")
ax.text(217, -20, "Chr 8", fontweight="bold",
        horizontalalignment="center", verticalalignment="center")
ax.set_title("P. falciparum", fontweight="bold")

cb = fig.colorbar(m)
ticks = cb.get_ticks()
cb.set_ticks([ticks.min(), ticks.max()])
cb.set_ticklabels(["bas", "élevé"])

fig.savefig("images/counts_pfalc.pdf")
