# Chapter 31 — Chemistry to AI hardware: dependencies and missing links

**Domain:** AI infrastructure  
**Release:** Chemistry Atlas 0.1.0  
**Evidence:** original mathematical/scientific explanation with selected publisher references, no original publisher bytes retained.

## Definitions and scientific meaning

Advanced AI depends on a physical computing stack: pure materials, controlled dopants, oxide and interconnect chemistry, dielectrics, packaging, thermal management, sensors, power conversion and repeatable metrology. Chemistry provides the link between atomic bonding and the physical devices on which software runs. The shortest viable knowledge reference must preserve enough physics and chemistry to understand *why* hardware methods work and what evidence tests them. A theory of silicon conductivity without process contamination limits is insufficient for manufacturing; a chemistry library without architecture and compiler knowledge cannot recreate intelligent software.

## Mathematical or physical principle

`Dependency chain: SI/chemical measurements → electronic structure → material purity and interfaces → semiconductor transport → electronic devices → computer architecture → AI algorithms.`

**Important:** The formula is meaningful only with its physical quantities, reference states, units, and stated assumptions. An internally consistent output does not establish that a material or chemical reaction actually exists in a measured sample.

## Derivation, reasoning and model limits

This chain is not a one-way sequence of factory instructions. Feedback from device testing changes material specifications, while advances in modeling guide chemical synthesis research. The Atlas should expose cross-node relations to Measurement, Materials, Energy, Computation and later Electronics/Manufacturing nodes. Relationships mean conceptual relevance, not actual integration or an observed performance gain. Future automated agents should retrieve source-closed context and preserve uncertainty rather than fabricate process parameters.

## Reconstruct an illustrative result offline

Suppose a synthetic silicon calculation predicts improved conductivity after increasing assumed electron density. Enumerate the missing device requirements: mobility measurement, contacts, breakdown, oxide quality, wafer purity and yield. Then identify which existing Atlases already contain supporting theory.

Retain the example input values, their declared source (author-created, not observational), the exact calculation method and at least one counterexample. If measured results differ, investigate source sample, phase, temperature, uncertainty, instrumental calibration and model applicability. Do not silently revise the data to agree with theory.

## Counterexample and what we have not established

No semiconductor is fabricated and no AI accelerator performance is measured. This chapter is a reconstruction dependency map, not proof of manufacturability or a novel chip process.

No chemical compound is prepared by this chapter. No current laboratory safety requirements are waived. Qualified chemical/industrial expertise is necessary for authentic process development.

## Scientific sources and original-rights gap

- [MIT OCW, Solid State Chemistry, Semiconductors](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/electronic-materials/14-semiconductors/) — inspected: Intrinsic/extrinsic carrier concepts, donor acceptor and band structure; not a fabrication tutorial
- [MIT OpenCourseWare Introduction to Solid-State Chemistry](https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/) — inspected: Undergraduate chemistry curriculum and link to electronics, polymers, phase diagrams and materials

These links identify selected supporting publications. They are **not** authenticated local original publisher files, and the Atlas does not grant new rights over them.
