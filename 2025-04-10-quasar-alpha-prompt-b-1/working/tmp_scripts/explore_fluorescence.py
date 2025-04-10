# This script loads the NWB file and explores fluorescence traces from ROI Response Series 1.
# It generates a plot of fluorescence intensity over time for an ROI,
# illustrating calcium or acetylcholine dynamics during the recording.

import pynwb
import remfile
import h5py
import matplotlib.pyplot as plt
import numpy as np

# Load NWB file remotely
url = "https://api.dandiarchive.org/api/assets/be84b6ff-7016-4ed8-af63-aa0e07c02530/download/"
file = remfile.File(url)
h5file = h5py.File(file)
io = pynwb.NWBHDF5IO(file=h5file, load_namespaces=True)
nwb = io.read()

# Access fluorescence data for ROI 1
flu_data = nwb.processing['ophys'].data_interfaces['Fluorescence'].roi_response_series['RoiResponseSeries1'].data[:]
flu_timestamps = nwb.processing['ophys'].data_interfaces['Fluorescence'].roi_response_series['RoiResponseSeries1'].timestamps[:]

plt.figure(figsize=(10, 4))
plt.plot(flu_timestamps, flu_data[:,0], label='ROI 1')
plt.xlabel('Time (s)')
plt.ylabel('Fluorescence (a.u.)')
plt.title('Fluorescence trace for ROI 1 over time')
plt.legend()
plt.tight_layout()
plt.savefig('tmp_scripts/fluorescence_trace.png')
plt.close()

io.close()
file.close()