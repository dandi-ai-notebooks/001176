# This script loads pupil radius data from the selected NWB file of Dandiset 001176
# It visualizes the pupil size over time, informative of arousal and behavioral state
# The resulting figure will be saved as 'tmp_scripts/pupil_radius.png'

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

pupil_ts = nwb.acquisition['PupilTracking'].time_series['pupil_raw_radius']
timestamps = pupil_ts.timestamps[:]
pupil_radius = pupil_ts.data[:]

plt.figure(figsize=(12,5))
plt.plot(timestamps, pupil_radius, lw=0.5)
plt.xlabel('Time (s)')
plt.ylabel('Pupil radius (px)')
plt.title('Pupil radius over time')
plt.tight_layout()
plt.savefig('tmp_scripts/pupil_radius.png')