# This script loads fluorescence data from the selected NWB file of Dandiset 001176
# It visualizes the fluorescence trace vs. time for the single ROI (indicative of ACh sensor signal)
# The resulting figure will be saved as 'tmp_scripts/fluorescence_trace.png'

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

roi_response = nwb.processing['ophys'].data_interfaces['Fluorescence'].roi_response_series['RoiResponseSeries1']
timestamps = roi_response.timestamps[:]
fluorescence = roi_response.data[:, 0]

plt.figure(figsize=(12,5))
plt.plot(timestamps, fluorescence, lw=0.5)
plt.xlabel('Time (s)')
plt.ylabel('Fluorescence (a.u.)')
plt.title('Fluorescence trace (Ach sensor) over time')
plt.tight_layout()
plt.savefig('tmp_scripts/fluorescence_trace.png')