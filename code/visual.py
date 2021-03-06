"""
    Name: Ayush Kumar, Kaushik S Kalmady
    Date: 5/10/2017

    Ref : https://github.com/jakeret/tf_unet/blob/master/demo/demo_radio_data.ipynb
	Visualizing processed data to know what the dataset looks like


    Follow instructions in process_data.py and run it before you run this script.
	This code requires the .h5 files generated by that script.

    Make sure you save a copy of this folder in case you need the original files.


    You will also need to have tf_unet installed.
    For installation instructions: tf_unet.readthedocs.io


"""




from __future__ import division, print_function
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import glob
import os
from scripts.radio_util import DataProvider
from tf_unet import unet


plt.rcParams['image.cmap'] = 'gist_earth'


# Read all required files
files = glob.glob('bgs_example_data/seek_cache/*')

# This is a tf_unet DataProvider
# It's a generator that provides training data and grund truth as required
# Still unsure what the first parameter does
data_provider = DataProvider(10000, files)
x_test, y_test = data_provider(96) # Get all 96 files

fig, ax = plt.subplots(1,2, figsize=(12,4))

for i in range(96):
    ax[0].imshow(x_test[i,...,0], aspect="auto")
    ax[1].imshow(y_test[i,...,1], aspect="auto")
	fig.savefig("pic_10000_"+str(i)+".png")



# We'll change the first parameter and see how different the data looks
# The source code did not mention anything about what each axis represents
data_provider = DataProvider(600, files)
x_test, y_test = data_provider(96)

fig, ax = plt.subplots(1,2, figsize=(12,4))

for i in range(96):
    ax[0].imshow(x_test[i,...,0], aspect="auto")
    ax[1].imshow(y_test[i,...,1], aspect="auto")
	fig.savefig("pic_600_"+str(i)+".png")


print ("Done processing. Images saved in current directory.")
print("It should look something like the ones here : https://imgur.com/a/D7vns")
