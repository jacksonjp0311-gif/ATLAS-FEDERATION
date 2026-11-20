# COMPUTATION ATLAS · 0.1.0

![ATLAS FORGE knowledge hub](assets/atlas_forge_knowledge_hub.png)

**A reconstructable reference to computation theory, data structures, algorithms, numerical reasoning, and finite-state verification.**

Part of **ATLAS FORGE**, a long-running program to build 30 domain libraries before implementing any Bitwork routing or desktop transfer.

## Read first

- [Full original computation manual](docs/DEPTH_MANUAL_v0.1.0.md): 34 numbered chapters with proofs, derivations, reconstruction exercises and failure boundaries
- [Worked casebook](docs/CASEBOOK.md): 16 executable author-created investigations
- [Source register](docs/SOURCE_REGISTER.md): publisher locators, checked scopes, rights uncertainty, missing primary bytes
- [Coverage matrix](docs/COVERAGE_MATRIX.md): gaps and future work
- [Reconstruction and survival guide](docs/REFERENCE_GUIDE.md)
- [Machine-readable common data](data/): sealed research records and relations
- [Executable methods](computation_atlas/models.py), [finite proof checkers](computation_atlas/proofs.py), [tests](tests/)

## Offline usage

```sh
python -m computation_atlas
python -m unittest discover -s tests
python tools/check_manifest.py verify .
```

No dependencies are needed for the core algorithms or their tests beyond Python. This is **not** a tool-executing agent, general-purpose theorem prover, live Bitwork router, or scientific-certified controller.

## Evidence standards

- Every record retains exact source IDs, revision hashes, assumptions, applicability, limitations, uncertainty, and rights status.
- `15` bibliographic source cards are included. **None of their original transport bytes is archived.** No current claim of full offline primary-source survival.
- 34 chapter explanations and derivations are original, human-readable and available offline. They are not certified by independent peer review.
- Numerical validations use invented or published mathematical test examples, not live scientific experiments.
- Original Agent, Control, Measurement, Causal, Materials, Cymatics, and Signal data remain byte-for-byte unchanged in the shared collection.

## Intended next stages

Deepen Computation toward scoped content v1.0: advanced complexity reductions, numerical linear algebra, parallel and external-memory cost models, probabilistic algorithms, formal proof mechanization, rights-cleared primary source archives, human-reviewed source passages. Only after all 30 domains, build and test Bitwork routing.

## Attribution

Original educational synthesis drafted with AI assistance in the James Paul Jackson research program. Linked third-party publishers retain their rights. Original published text is not copied into this package. License for this original code/text: see `LICENSE.md`; imported earlier node licenses remain unchanged.

## Standalone versus full federation

The standalone wheel contains 162 exact computation records and 170 local relations. Five additional cross-domain relations exist only in the complete eight-node collection because their target records reside in older nodes. This intentional projection keeps both exports source-closed; do not merge standalone relation counts into the federation without accounting for this distinction.
