# Architecture

## Abstraction: Multi-Tiered (Composed)

The abstraction for which was chosen is meant to mimic a constrained version of how the reverse of fourier transform works. Rather than deconstructing to unique frequencies, we are systematically composing layers of sounds.

<p align="center">
  <img width="700" height="500" src="imgs/fourier.png">
</p>

During this process, the subtle agent guidance by variance based on neurofeedback measurement helps to create more plasticity in the way the brain can 'accepts' tone and sound via constraints. 

<p align="center">
  <img width="700" height="500" src="imgs/abstraction.png">
</p>

The guided sound 'waves' amount to a layered sound the user will listen to based on relative agent reward response.

## Abstraction: Single Trajectory

In the single trajectory, the agent only acts on the tuning of a single band. The variation of frequency of the band dictates the 3rd binaural sound perceived.

```
frequency hz ranges

~delta = 1;     // 0.5 - 2. deep sleep, unsconsciousness
~theta = 5.5;   // 4 - 7. Meditative, drowsy, sleeping. Memory, spatial learning
~mu = 9;        // 9 - 11. associated with voluntary movement
~alpha = 10;    // 7.5 - 12.5. Relaxed states of mind
~beta1 = 14;    // 12.5 - 16. Normal waking consciousness
~beta2 = 18;    // 16.5 - 20.
~beta3 = 24;    // 20.5 - 28
~gamma = 35;    // 32 - 100. Visual awareness, transcendental mental states
```

<p align="center">
  <img width="700" height="500" src="imgs/digInFirstFundamentalTheoremOfCalculus-figure0.svg">
</p>

The experience can be thought of as 

<p align="center">
  <img width="700" height="500" src="imgs/plot_fnirs.png">
</p>

## Abstraction: Multi-player

something with p2p networking & fft covariance matching.

# Architecture Sub-system

<p align="center">
  <img width="700" height="500" src="imgs/sub-system.png">
</p>

# Setup Goals
Easy of plugging in any stream of EEG, fNIRS, or haptic data stream that might be an input.

## Input Convolution
5x5

## Randomization
Action space has a 50% randomization for state selection.

## Agent Type
Policy Network, more on this [here](https://towardsdatascience.com/policy-networks-vs-value-networks-in-reinforcement-learning-da2776056ad2?gi=3f17354ded7d)

## Reward Function
TODO
