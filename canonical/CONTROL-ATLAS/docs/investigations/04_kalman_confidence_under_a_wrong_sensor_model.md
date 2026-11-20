# Investigation 04: Kalman confidence under a wrong sensor model

**Origin:** synthetic authored model, no real equipment.

A scalar filter given process variance .01, measurement variance .1 and selected synthetic readings produces a decreasing variance and a posterior estimate. If the sensor has an unmodeled constant bias, its reported covariance need not cover the true state; increasing the number of readings can make it confidently wrong. The local filter does not estimate covariance from data, handle correlated noise or filter a real sensor stream.

**Source:** https://underactuated.mit.edu/state_estimation.html

**What to investigate next:** request the actual plant, source coefficients, test conditions and independent reviewer sign-off; a fitted mathematical example cannot prove controller suitability.
