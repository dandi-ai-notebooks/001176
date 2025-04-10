# This script loads the NWB file and explores EyeTracking and PupilTracking data.
# It generates plots of:
# - eye x and y position over time
# - pupil radius over time
# to understand animal's eye dynamics during experimental sessions.

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

# ----- Eye position -----
eye_pos_data = nwb.acquisition['EyeTracking'].spatial_series['eye_position'].data[:]
eye_pos_timestamps = nwb.acquisition['EyeTracking'].spatial_series['eye_position'].timestamps[:]

plt.figure(figsize=(10, 4))
plt.plot(eye_pos_timestamps, eye_pos_data[:,0], label='X position')
plt.plot(eye_pos_timestamps, eye_pos_data[:,1], label='Y position')
plt.xlabel('Time (s)')
plt.ylabel('Eye position (px)')
plt.title('Eye position over time')
plt.legend()
plt.tight_layout()
plt.savefig('tmp_scripts/eye_position.png')
plt.close()

# ----- Pupil radius -----
pupil_radius = nwb.acquisition['PupilTracking'].time_series['pupil_raw_radius'].data[:]
pupil_timestamps = nwb.acquisition['PupilTracking'].time_series['pupil_raw_radius'].timestamps[:]

plt.figure(figsize=(10, 4))
plt.plot(pupil_timestamps, pupil_radius)
plt.xlabel('Time (s)')
plt.ylabel('Pupil radius (px)')
plt.title('Pupil radius over time')
plt.tight_layout()
plt.savefig('tmp_scripts/pupil_radius.png')
plt.close()

io.close()
file.close()