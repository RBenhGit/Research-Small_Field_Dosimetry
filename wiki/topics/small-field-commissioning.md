# Small-Field Commissioning (Conventional Linac)

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-21
**Sources:** [linac-small-field-dosimetry-process-tree], [trs-483], [tg-155]

## Summary

Small-field commissioning on a conventional linear accelerator (Varian, Elekta, Siemens) follows a nine-phase structured workflow that begins with baseline linac QA and culminates in a documented QA program with annual re-measurement obligations. The central tasks are reference dosimetry per TRS-398, FWHM-based field size characterization, output factor measurement (by one of three methods depending on field size), and application of TRS-483 detector-specific correction factors from Tables 24 and 27. Conventional linacs have key advantages over dedicated SRS units for TRS-483 implementation: they can establish a true 10 × 10 cm reference field, and a validated correction factor database exists for 25+ detector types across their field size range.

## Key Facts / Claims

- **Scope:** Field sizes 0.5 cm × 0.5 cm to 10 cm × 10 cm on conventional linacs; excludes CyberKnife, Gamma Knife, TomoTherapy. [linac-small-field-dosimetry-process-tree]
- **Nine phases:** (1) Linac QA & qualification; (2) Reference dosimetry (TPR₂₀,₁₀, TRS-398 calibration); (3) Detector selection; (4) Geometric characterization (FWHM); (5) Output factor measurement; (6) Correction factor application; (7) Multi-detector verification; (8) TPS commissioning; (9) QA program. [linac-small-field-dosimetry-process-tree]
- **Three output factor measurement methods by field size:**
  - Method A (Standard, ≥ 3 cm): small ion chamber; interleaved reference measurements; correct for T/P, polarity, recombination
  - Method B (Intermediate Field, 1–3 cm): chain of ion chamber + small detector measurements; see [[intermediate-field-method]]
  - Method C (Small Field, < 1 cm): microDiamond or plastic scintillator; mandatory multi-detector verification [linac-small-field-dosimetry-process-tree]
- **Detector selection by field size:**
  - ≥ 3 cm: PTW 31010 Semiflex, IBA CC01 (small ion chambers)
  - 1–3 cm: Intermediate Field Method combining ion chambers with microDiamond or unshielded diodes
  - < 1 cm: PTW 60019 microDiamond preferred; plastic scintillator as reference standard
  - < 0.5 cm: Extreme uncertainty (±5–7%); multiple detectors mandatory [linac-small-field-dosimetry-process-tree]
- **Correction factor tables:** TRS-483 Tables 24 (6 MV) and 27 (10 MV); linear interpolation in field size space for unlisted field sizes. [linac-small-field-dosimetry-process-tree]
- **WFF/FFF equivalence:** Correction factors show no significant difference between flattened and unflattened beams at the same nominal energy; Tables 24 and 27 apply to both beam types. [linac-small-field-dosimetry-process-tree]
- **FFF-specific requirements:** Higher dose rates require dedicated dose-rate dependence testing; higher ion recombination in chambers must be corrected. [linac-small-field-dosimetry-process-tree]
- **Multi-detector verification:** ≥ 2 independent detector types required for all methods; comparison validates the output factor and correction factor application. [linac-small-field-dosimetry-process-tree]
- **Clinical sub-5 mm caveat:** Fields below 0.5 cm represent "research rather than clinical dosimetry" per TRS-483; measurement uncertainty of ±5–7% (k=1) is typical. [linac-small-field-dosimetry-process-tree]

## Uncertainty Budget

| Field size range | Method | k=1 uncertainty |
|---|---|---|
| Reference dosimetry | TRS-398 | ±0.9% |
| ≥ 2 cm with appropriate detector | Method A | ±1–2% |
| 1–2 cm via Intermediate Field | Method B | ±1.5–2.5% |
| < 1 cm | Method C | ±4–6% |

[linac-small-field-dosimetry-process-tree]

## Connections

- [[intermediate-field-method]] — Method B for the 1–3 cm range; key component of the commissioning workflow
- [[small-field-output-correction-factors]] — Phases 5–6 apply TRS-483 k factors; Tables 24 and 27 are the normative lookup source
- [[small-field-detectors]] — Phase 3 detector selection drives the whole workflow; correct detector choice by field size is critical
- [[iaea-trs-483]] — Provides the normative framework, correction factor tables, and reference field definition for this workflow
- [[aapm-tg-155]] — Provides updated detector guidance, uncertainty analysis, and FFF beam considerations
- [[reference-dosimetry-kq]] — Phase 2 reference dosimetry uses TRS-398/TRS-483 k_Q formalism
- [[machine-specific-reference-field]] — Not applicable to conventional linacs (which can realize 10 × 10 cm), but the msr formalism is relevant if the linac is used in SRS mode with a non-standard reference field
- [[small-field-definition]] — Phase 4 geometric characterization applies the FWHM-based field size definition; understanding when a field is small determines which method applies

## Open Questions

- For linacs with very small focal spots (< 0.5 mm), does the WFF/FFF correction factor equivalence hold, or are machine-specific MC calculations required?
- How often should annual re-measurement protocols be triggered by linac hardware changes (MLC replacement, beam tuning)?

## Raw Notes

- Conventional linacs are advantageous for TRS-483 implementation because they have an extensive validated k factor database; dedicated SRS units (CyberKnife, Gamma Knife) often require machine-specific MC calculations due to limited tabulation.
- The 9-phase structure is not explicitly numbered in TRS-483 itself; it represents a synthesis of the recommended workflow derived from the protocol.
