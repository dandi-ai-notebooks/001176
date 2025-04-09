# %% [markdown]
# # Dandiset 001176: Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavior state
# 
# **IMPORTANT**: This notebook was AI-generated using dandi-notebook-gen and has **not been fully verified**. Please be careful when interpreting any results or analyses herein.
# 
# This Dandiset provides simultaneous in vivo cortical imaging data of acetylcholine (ACh) sensors and GCaMP-expressing axons recorded during spontaneous behavioral state changes in awake mice.
# 
# **Dandiset metadata summary:**
# * **Dandiset ID:** 001176 (draft)
# * **Title:** Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavior state
# * **Description:** Imaging data capturing cortical ACh activity, axonal activity, and behavioral measures like pupil size during state changes.
# * **Contributors:** NIH; Jacob Reimer; Erin Neyhart
# * **Date Created:** 2024-08-20
# * **Keywords:** acetylcholine, brain states, two-photon imaging, neuromodulator, axon imaging
# * **License:** CC-BY-4.0 (Open Access)
# * **Techniques:** behavioral, analytical, surgical

# %% [markdown]
# ## List of Dandiset Assets
# 
# Use DANDI API client to get the list of assets (NWB files):

# %%
from dandi.dandiapi import DandiAPIClient
client = DandiAPIClient()
dandiset = client.get_dandiset("001176")
assets = list(dandiset.get_assets())
assets[:5]  # preview first five assets

# %% [markdown]
# ## Selected NWB file for demonstration
# 
# This notebook uses:
# 
# `sub-16/sub-16_ses-16-1-2-Ach-M1_behavior+ophys.nwb`
# 
# URL: https://api.dandiarchive.org/api/assets/4550467f-b94d-406b-8e30-24dd6d4941c1/download/
# 
# The code below shows how to load this NWB file remotely, following `dandi-notebook-gen-tools nwb-file-info` instructions.

# %%
import remfile
import h5py
import pynwb

url = "https://api.dandiarchive.org/api/assets/4550467f-b94d-406b-8e30-24dd6d4941c1/download/"
file = remfile.File(url)
f = h5py.File(file)
io = pynwb.NWBHDF5IO(file=f)
nwb = io.read()

print(f"Loaded NWB session: {nwb.session_description}, Subject ID: {nwb.subject.subject_id}")

# %% [markdown]
# ## Exploring dataset structure and metadata

# %%
print("Available acquisitions:", list(nwb.acquisition.keys()))
print("Processing modules:", list(nwb.processing.keys()))
print("Subject info:", nwb.subject)
print("Session start:", nwb.session_start_time)

# %% [markdown]
# ## Fluorescence Ach sensor recording (trace over time)
# 
# This is the raw fluorescence trace for one segmented ROI expressing the Ach sensor.

# %%
import matplotlib.pyplot as plt
import numpy as np

roi_response = nwb.processing['ophys'].data_interfaces['Fluorescence'].roi_response_series['RoiResponseSeries1']
timestamps = roi_response.timestamps[:]
fluorescence = roi_response.data[:, 0]

plt.figure(figsize=(12,5))
plt.plot(timestamps, fluorescence, lw=0.5)
plt.xlabel('Time (s)')
plt.ylabel('Fluorescence (a.u.)')
plt.title('Fluorescence trace (Ach sensor)')
plt.tight_layout()
plt.show()

# %% [markdown]
# This trace shows the dynamic fluctuations and noise typical in in vivo Ach imaging data. Further filtering or event detection could be performed depending on desired analyses.

# %% [markdown]
# ## Pupil radius over time
# 
# This behavioral signal reflects arousal/state changes.

# %%
pupil_ts = nwb.acquisition['PupilTracking'].time_series['pupil_raw_radius']
pupil_times = pupil_ts.timestamps[:]
pupil_radius = pupil_ts.data[:]

plt.figure(figsize=(12,5))
plt.plot(pupil_times, pupil_radius, lw=0.5)
plt.xlabel('Time (s)')
plt.ylabel('Pupil radius (px)')
plt.title('Pupil radius over time')
plt.tight_layout()
plt.show()

# %% [markdown]
# The pupil radius fluctuates and contains gaps/artifacts typical of behavioral tracking data.

# %% [markdown]
# ## Eye position (X and Y) over time
# 
# Tracking of pupil center coordinates in pixels.

# %%
eye_spatial_series = nwb.acquisition['EyeTracking'].spatial_series['eye_position']
eye_times = eye_spatial_series.timestamps[:]
eye_pos = eye_spatial_series.data[:, :]

plt.figure(figsize=(12,5))
plt.plot(eye_times, eye_pos[:,0], label='X position (px)', lw=0.5)
plt.plot(eye_times, eye_pos[:,1], label='Y position (px)', lw=0.5)
plt.xlabel('Time (s)')
plt.ylabel('Eye position (px)')
plt.legend()
plt.title('Eye position over time')
plt.tight_layout()
plt.show()

# %% [markdown]
# This visualization shows intermittent, noisy xy movements. Smoothing and segmentation can be used for detailed eye behavior analysis.

# %% [markdown]
# ## Treadmill velocity over time
# 
# Locomotor activity during imaging.

# %%
tm = nwb.acquisition['treadmill_velocity']
tm_times = tm.timestamps[:]
velocity = tm.data[:]

plt.figure(figsize=(12,5))
plt.plot(tm_times, velocity, lw=0.5)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (cm/s)')
plt.title('Treadmill velocity')
plt.tight_layout()
plt.show()

# %% [markdown]
# This plot reveals alternations between locomotor quiescence and bouts of movement, characteristic of awake behaving animals.

# %% [markdown]
# ## Summary
# 
# This notebook provided basic guidance on exploring Dandiset 001176, including:
# - Accessing the Dandiset programmatically
# - Loading a representative NWB file remotely via Python
# - Examining key metadata fields and dataset structure
# - Visualizing neural signals (Ach sensor fluorescence)
# - Exploring behavioral correlates (pupil size, eye movement, locomotion)
# 
# Use this as a starting point. Further analyses could include:
# - Statistical comparisons across behavioral states
# - Event-aligned averaging
# - Signal correlation analyses
# 
# but such analyses require domain judgment and additional code development. Use appropriate caution interpreting observed fluctuations without quantification.