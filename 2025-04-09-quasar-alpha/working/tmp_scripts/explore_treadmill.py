# This script loads treadmill velocity data from the NWB file of Dandiset 001176
# It visualizes animal locomotion over time
# The resulting figure is saved as 'tmp_scripts/treadmill_velocity.png'

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

tm = nwb.acquisition['treadmill_velocity']
timestamps = tm.timestamps[:]
velocity = tm.data[:]

plt.figure(figsize=(12,5))
plt.plot(timestamps, velocity, lw=0.5)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (cm/s)')
plt.title('Treadmill velocity over time')
plt.tight_layout()
plt.savefig('tmp_scripts/treadmill_velocity.png')