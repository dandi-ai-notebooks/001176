# This script loads eye position data from the selected NWB file of Dandiset 001176
# It visualizes the x and y pupil positions over time
# The resulting figure is saved as 'tmp_scripts/eye_position.png'

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import remfile
import h5py
import pynwb

url = "https://api.dandiarchive.org/api/assets/4550467f-b94d-406b-8e30-24dd6d4941c1/download/"
file = remfile.File(url)
f = h5py.File(file)
io = pynwb.NWBHDF5IO(file=f)
nwb = io.read()

eye_spatial_series = nwb.acquisition['EyeTracking'].spatial_series['eye_position']
timestamps = eye_spatial_series.timestamps[:]
eye_pos = eye_spatial_series.data[:, :]

plt.figure(figsize=(12,5))
plt.plot(timestamps, eye_pos[:,0], label='X position (px)', lw=0.5)
plt.plot(timestamps, eye_pos[:,1], label='Y position (px)', lw=0.5)
plt.xlabel('Time (s)')
plt.ylabel('Eye position (px)')
plt.title('Eye position (X and Y) over time')
plt.legend()
plt.tight_layout()
plt.savefig('tmp_scripts/eye_position.png')