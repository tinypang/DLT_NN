import numpy as np
import nnsetup as nns
def saesetupm(arrsize):
	sae = {}
	for u in range(1, len(arrsize)):
		sae[u] = nns.nnsetup([arrsize[u-1], arrsize[u], arrsize[u-1]])
	return sae
