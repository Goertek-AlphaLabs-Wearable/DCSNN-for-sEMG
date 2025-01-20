# DCSNN-for-sEMG
The repository has made the core algorithm framework of DCSNN and the associated EMG micro-gesture datasets publicly available. For access to the complete engineering for academic research or commercial collaboration, please reach out to the author directly.
![pipeline](https://github.com/user-attachments/assets/e8675b0f-c16f-4b74-8b7e-db039055d892)


# TAD-LIF
We designed a method of event detection called leaky integrate-and-fire for transient-state action detection (TAD-LIF) to identify transient-state actions. TAD-LIF significantly reduces the amount of required computation and quickly locates the target actions.
![figure7](https://github.com/user-attachments/assets/1e049ba8-380d-4de7-a5a4-bf5b4ad4d4a8)


# DCSNN
We proposed a novel deep compressed spiking neural network (DCSNN), which can accurately identify transient-state micro-gestures, and achieves orders of magnitudes of improvement in terms of power consumption, inference speed, and memory usage.
![figure8](https://github.com/user-attachments/assets/787ef4b5-7d9f-4892-bea3-172a42f965fb)


# dataset
link:

![figure4](https://github.com/user-attachments/assets/d9e131bd-4988-4354-b0e9-fbf90959419e)
In all files, except for "Other," the first 8/3 columns represent the raw sEMG data, corresponding to the original data from each channel of GBS-I and GBS-II, respectively. The 4th/9th column indicates the data state, where 0 represents a Neutral state and 1 signifies an Action state.
In the "Other" files, the user performs various gestures randomly, so there is no label in the final column.
