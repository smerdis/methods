# Compatibility with Python 3
from __future__ import print_function, division

# Interactive graphs for matplotlib at the IPython prompt
%matplotlib

# Standard imports of libraries
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

fn = 'ds114_sub009_t2r1.nii'

anat = nib.load(fn)
data = anat.get_data()

n_tps = data.shape[-1]
stds = np.zeros(n_tps)
for t in range(n_tps):
	vol = data[:,:,:,t]
	stds[t] = np.std(vol)
	str = 'vol {t}, shape {s}, std={sd}'.format(t=t,s=vol.shape,sd=stds[t])
	print(str)

# plot standard deviations of each volume
plt.imshow(stds)


