#!/usr/bin/env python2.7
from intensities import *
import scipy.linalg as la


def nonconstantrows(x):
    nonconst = sp.ones(x.shape[0], dtype=bool)
    for i in xrange(0, x.shape[0]):
        if all(x[i, :] == x[i, 0]):
            nonconst[i] = False
    return nonconst


def removenonconstantrows(x):
    return x[nonconstantrows(x)]


def princomp(x):
    x -= sp.mean(x, axis=0)  # Center points at origin.
    x /= sp.std(x, axis=0)  # Scale to std unit size.
    u, s, v = la.svd(x)
    ind = np.argsort(s[::-1])  # Not sorted for some reason.
    s = s[ind]
    v = v[ind]  # Recall definition of SVD.
    pca = np.dot(x, v.T)
    # cov =  np.dot(np.dot(u, s**2), u.T)
    return pca, s, v


def scatter2(x, c=None):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    if c is not None:
        ax.scatter(x[:, 0], x[:, 1], c=c)
    else:
        ax.scatter(x[:, 0], x[:, 1])
    return ax


idx = nonconstantrows(wcl.values)
pca, s, v = princomp(wcl.values[idx, :].T)
scatter2(pca)
plt.title('WCL')
for label, x, y in zip(wcl.columns[:], pca[:, 0], pca[:, 1]):
    plt.annotate(
        label.replace("Intensity ", ""),
        xy=(x, y))

idx = nonconstantrows(wclp.values)
pca, s, v = princomp(wclp.values[idx, :].T)
scatter2(pca)
plt.title('WCLP')
for label, x, y in zip(wclp.columns[:], pca[:, 0], pca[:, 1]):
    plt.annotate(
        label.replace("Intensity ", ""),
        xy=(x, y))

idx = nonconstantrows(ub.values)
pca, s, v = princomp(ub.values[idx, :].T)
scatter2(pca)
plt.title('Ub')
for label, x, y in zip(ub.columns[:], pca[:, 0], pca[:, 1]):
    plt.annotate(
        label.replace("Intensity ", ""),
        xy=(x, y))

idx = nonconstantrows(ubp.values)
pca, s, v = princomp(ubp.values[idx, :].T)
scatter2(pca)
plt.title('UbP')
for label, x, y in zip(ubp.columns[:], pca[:, 0], pca[:, 1]):
    plt.annotate(
        label.replace("Intensity ", ""),
        xy=(x, y))

wcl_foldch[~np.isfinite(wcl_foldch)] = 0
idx = nonconstantrows(wcl_foldch.values)
pca, s, v = princomp(wcl_foldch.values[idx, :].T)
scatter2(pca)
plt.title('WCL log2 FC')
for label, x, y in zip(wcl_foldch.columns[:], pca[:, 0], pca[:, 1]):
    plt.annotate(
        label.replace("Intensity ", ""),
        xy=(x, y))

wclp_foldch[~np.isfinite(wclp_foldch)] = 0
idx = nonconstantrows(wclp_foldch.values)
pca, s, v = princomp(wclp_foldch.values[idx, :].T)
scatter2(pca)
plt.title('WCLP log2 FC')
for label, x, y in zip(wclp_foldch.columns[:], pca[:, 0], pca[:, 1]):
    plt.annotate(
        label.replace("Intensity ", ""),
        xy=(x, y))

ub_foldch[~np.isfinite(ub_foldch)] = 0
idx = nonconstantrows(ub_foldch.values)
pca, s, v = princomp(ub_foldch.values[idx, :].T)
scatter2(pca)
plt.title('Ub log2 FC')
for label, x, y in zip(ub_foldch.columns[:], pca[:, 0], pca[:, 1]):
    plt.annotate(
        label.replace("Intensity ", ""),
        xy=(x, y))

ubp_foldch[~np.isfinite(ubp_foldch)] = 0
idx = nonconstantrows(ubp_foldch.values)
pca, s, v = princomp(ubp_foldch.values[idx, :].T)
scatter2(pca)
plt.title('UbP log2 FC')
for label, x, y in zip(ubp_foldch.columns[:], pca[:, 0], pca[:, 1]):
    plt.annotate(
        label.replace("Intensity ", ""),
        xy=(x, y))

# alldata = pd.concat([wcl, wclp, ub, ubp], axis=1)
# alldata[~np.isfinite(alldata)] = 0
# idx = nonconstantrows(alldata.values)
# pca, s, v = princomp(alldata.values[idx, :])
# scatter2(pca)
# plt.title('All Data')
# for label, x, y in zip(names[idx], pca[:, 0], pca[:, 1]):
#     plt.annotate(
#         label,
#         xy=(x, y))

plt.show(block=False)
plt.show()
