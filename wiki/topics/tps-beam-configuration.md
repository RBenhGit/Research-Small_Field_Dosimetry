# TPS Beam Configuration: Small-Field Output Factor Entry

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-22
**Sources:** [small-field-output-factor-tps-entry], [iaea-trs-483]

## Summary

When entering small-field output factors into a Treatment Planning System (TPS) beam model, the table index is the nominal collimator/jaw setting — not the FWHM or S_clin. The value entered must be the corrected field output factor Ω measured at that nominal jaw setting, with the detector correction factor k looked up at the actual physical S_clin derived from the measured FWHM. Extrapolating to a hypothetical field whose FWHM exactly matches the nominal size introduces a systematic beam-model error because the TPS will never produce that physical state at the nominal jaw setting.

## Key Facts / Claims

- **TPS indexing convention:** TPS beam configuration tables index output factors by nominal collimator (jaw) setting — e.g., the "1×1 cm²" table entry corresponds to the machine's 1×1 jaw configuration. TPS models do NOT index by FWHM or equivalent square S_clin. [small-field-output-factor-tps-entry]
- **Four-step workflow for a 1×1 cm² entry:**
  1. Set jaws to 1×1 cm²; measure central-axis detector reading M_f_clin at reference depth (10 cm).
  2. Measure cross-plane and in-plane profiles at the same setting; compute S_clin = √(FWHM_x × FWHM_y).
  3. Look up the detector-specific k_{Q_clin,Q_msr} in TRS-483 Tables 24/27 using the actual S_clin (e.g., 1.05 cm), not the nominal 1.0 cm.
  4. Calculate Ω = (M_f_clin / M_f_msr) × k and enter this value as the "1×1 cm²" entry in the TPS.
  [small-field-output-factor-tps-entry]
- **FWHM vs nominal jaw discrepancy:** For a 1×1 cm² jaw setting, the measured FWHM (and therefore S_clin) is typically 1–3 mm larger than the nominal setting due to penumbra overlap in small fields. Source occlusion, linac focal spot size, and beam energy all affect the magnitude of this discrepancy. [small-field-output-factor-tps-entry]
- **Extrapolation risk:** If the user extrapolates to find Ω for a hypothetical field with FWHM = 1.0 cm exactly (matching the jaw label), they are computing the output for a physical state the linac does not produce at the 1×1 jaw setting. Entering this extrapolated value introduces a systematic beam-model error. [small-field-output-factor-tps-entry]
- **When extrapolation is valid (TRS-483 guidance):** Extrapolation to a different field size is appropriate only when (a) no tabulated k data exists for the measured S_clin, or (b) characterizing fields smaller than the smallest achievable jaw setting. [small-field-output-factor-tps-entry][iaea-trs-483]
- **Summary of nominal vs physical distinction:**

  | Step            | Field Reference       | Value Used                    |
  |-----------------|-----------------------|-------------------------------|
  | Measurement     | Nominal (1×1 cm²)     | M_f_clin                      |
  | Profile analysis| Physical (FWHM)       | Determine S_clin              |
  | TRS-483 lookup  | Physical (FWHM)       | Find k at S_clin              |
  | TPS entry       | Nominal (1×1 cm²)     | Enter corrected Ω             |

  [small-field-output-factor-tps-entry]

## Connections

- [[small-field-output-correction-factors]] — The k_{Q_clin,Q_msr} correction factor is looked up at the physical S_clin and applied to produce the corrected Ω for TPS entry
- [[small-field-definition]] — S_clin = √(FWHM_x × FWHM_y) is the physical field size; it diverges from the nominal jaw setting in small fields by 1–3 mm
- [[small-field-commissioning]] — Phase 8 of the commissioning workflow is TPS entry; this page details the specific procedure for that phase
- [[iaea-trs-483]] — Normative source for the Ω formalism, k factor tables, and guidance on when extrapolation is permissible
- [[machine-specific-reference-field]] — M_f_msr is the denominator in the Ω ratio; the msr field provides the reference reading

## Open Questions

- Do all major TPS vendors (Eclipse, Monaco, RayStation, Pinnacle) use nominal jaw setting as the field size index for output factor tables, or do any accept FWHM-based input directly?
- For MLC-defined fields (no jaw movement), should the nominal MLC aperture or the FWHM-derived S_clin be used as the TPS table index?
- How should the TPS entry be handled for fields where S_clin is between two tabulated jaw settings (e.g., S_clin = 1.08 cm between 1×1 and 2×2 entries)?

## Raw Notes

- The core insight from TRS-483: the k factor accounts for the detector's response at the physical field size, while the TPS label corresponds to the machine jaw setting. These are two different quantities that must be handled independently.
- In practice, most clinical TPS beam models are configured during commissioning with output factors measured at discrete jaw settings; the continuous FWHM variation is captured via the k correction applied at measurement time.
