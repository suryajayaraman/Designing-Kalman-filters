# Designing-Kalman-filters
Repo contains workflow for designing Kalman filters


## Table of contents
- [Chapter 1: The g-h Filter](Chapter1_summary)
- Chapter 2: The Discrete Bayes Filter
Chapter 3: Probabilities, Gaussians, and Bayes' Theorem



Introduces using Gaussians to represent beliefs in the Bayesian sense. Gaussians allow us to implement the algorithms used in the discrete Bayes filter to work in continuous domains.

Chapter 4: One Dimensional Kalman Filters

Implements a Kalman filter by modifying the discrete Bayes filter to use Gaussians. This is a full featured Kalman filter, albeit only useful for 1D problems.

Chapter 5: Multivariate Gaussians

Extends Gaussians to multiple dimensions, and demonstrates how 'triangulation' and hidden variables can vastly improve estimates.

Chapter 6: Multivariate Kalman Filter

We extend the Kalman filter developed in the univariate chapter to the full, generalized filter for linear problems. After reading this you will understand how a Kalman filter works and how to design and implement one for a (linear) problem of your choice.

Chapter 7: Kalman Filter Math

We gotten about as far as we can without forming a strong mathematical foundation. This chapter is optional, especially the first time, but if you intend to write robust, numerically stable filters, or to read the literature, you will need to know the material in this chapter. Some sections will be required to understand the later chapters on nonlinear filtering.

Chapter 8: Designing Kalman Filters

Building on material in Chapters 5 and 6, walks you through the design of several Kalman filters. Only by seeing several different examples can you really grasp all of the theory. Examples are chosen to be realistic, not 'toy' problems to give you a start towards implementing your own filters. Discusses, but does not solve issues like numerical stability.

Chapter 9: Nonlinear Filtering

Kalman filters as covered only work for linear problems. Yet the world is nonlinear. Here I introduce the problems that nonlinear systems pose to the filter, and briefly discuss the various algorithms that we will be learning in subsequent chapters.

Chapter 10: Unscented Kalman Filters

Unscented Kalman filters (UKF) are a recent development in Kalman filter theory. They allow you to filter nonlinear problems without requiring a closed form solution like the Extended Kalman filter requires.

This topic is typically either not mentioned, or glossed over in existing texts, with Extended Kalman filters receiving the bulk of discussion. I put it first because the UKF is much simpler to understand, implement, and the filtering performance is usually as good as or better then the Extended Kalman filter. I always try to implement the UKF first for real world problems, and you should also.

## References
- [Page contains all major sources for Kalman filters](https://resourcium.org/index.php/topic/kalman-filter)
