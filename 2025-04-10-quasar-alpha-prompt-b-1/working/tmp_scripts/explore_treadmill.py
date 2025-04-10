# This script loads the NWB file and visualizes treadmill velocity over time,
# to explore behavioral state changes (e.g., running/rest).
# This helps relate behavior to neural or imaging data.

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

velocity = nwb.acquisition['treadmill_velocity'].data[:]
timestamps = nwb.acquisition['treadmill_velocity'].timestamps[:]

plt.figure(figsize=(10, 4))
plt.plot(timestamps, velocity)
plt.xlabel('Time (s)')
plt.ylabel('Treadmill velocity (cm/s)')
plt.title('Treadmill velocity over time')
plt.tight_layout()
plt.savefig('tmp_scripts/treadmill_velocity.png')
plt.close()

io.close()
file.close()