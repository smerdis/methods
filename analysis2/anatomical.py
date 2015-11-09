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

# first timepoint
vol1 = data[:,:,:,0]

# show the central slice
sl = vol1[:,:,15]
plt.imshow(sl)

# what's with the memmap thing?
print(np.std(sl))
