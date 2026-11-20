# Investigation 42 — What would move Control toward content v1?

**Question:** Our mathematical observer, actuator and tube algorithms pass thousands of tests. Does that qualify a real machine or even complete the control reference domain?

**Answer:** No. The tests concern authored models, not observed equipment. A scoped Control content v1 should cover experimentally identified plant dynamics with an authentic, rights-cleared time series; parameter uncertainty and sensor calibration; multivariable output feedback; known actuator rate/lag data; independent validation/held-out replay; and an explicit match from the physical model to any control-theory claim. The present v0.6 adds a significant missing interface—state estimate and applied actuator dynamics—but only in a bounded scalar setting.

**Research plan:** obtain permissioned genuine plant data, define safe sampling and audit requirements, estimate a model with train/validation splits, measure actual actuator response and timestamp error, specify state/noise bounds with independent evidence, compare plausible models, and evaluate finite envelopes against genuine unseen traces. Any future hardware experiment requires qualified authorization, safe interlocks, supervised procedures and independent review. None of those actions is implemented by this reference.

**Project-wide sequencing:** build all 30 Atlas domain content libraries first. Preserve each node's source closure and immutable historical revisions. Only after domain content development should the separate Bitwork-driven routing system be built and tested on independent benchmark questions with actual models. After final integration and PC-side verification, transfer the collection as a complete versioned release. Never silently treat the routing design as an already deployed system.

**Outcome:** a defensible v0.6 research milestone with sharply defined future gates, not a falsely labeled scientific v1 or engineering safety certificate.
