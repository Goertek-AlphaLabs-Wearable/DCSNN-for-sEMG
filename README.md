# DCSNN-for-sEMG
The repository has made the core algorithm framework of DCSNN and the associated EMG micro-gesture datasets publicly available. For access to the complete engineering for academic research or commercial collaboration, please reach out to the author directly.
<div align="center">
  <img src="https://github.com/Goertek-AlphaLabs-Wearable/DCSNN-for-sEMG/blob/main/Figures/pipeline.png">
</div>


# TAD-LIF
We designed a method of event detection called leaky integrate-and-fire for transient-state action detection (TAD-LIF) to identify transient-state actions. TAD-LIF significantly reduces the amount of required computation and quickly locates the target actions.

# DCSNN
We proposed a novel deep compressed spiking neural network (DCSNN), which can accurately identify transient-state micro-gestures, and achieves orders of magnitudes of improvement in terms of power consumption, inference speed, and memory usage.

# dataset
link:

In all files, except for "Other," the first 8/3 columns represent the raw sEMG data, corresponding to the original data from each channel of GBS-I and GBS-II, respectively. The 4th/9th column indicates the data state, where 0 represents a resting state and 1 signifies an active state.
In the "Other" files, the user performs various gestures randomly, so there is no label in the final column.
