# Intermediate Field Method

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-21
**Sources:** [intermediate-field-method], [trs-483], [tg-155]

## Summary

The intermediate field method (also called the daisy-chain or chain normalization method) establishes dosimetric traceability between the standard 10 × 10 cm reference field and sub-centimetre small fields by using an intermediate-sized field (typically 3 × 3 to 4 × 4 cm) as a calibration bridge. A reference ionization chamber first characterizes the intermediate field, and a small-field detector (diode, microDiamond) is cross-calibrated there before being deployed in even smaller fields. This approach reduces the magnitude of energy-dependent corrections at each step compared to a single large-to-tiny jump. IAEA TRS-483 and AAPM TG-155 both recognize it as a valid output factor measurement method — particularly useful for 1–3 cm fields — while cautioning that it is not a substitute for better detector selection when that option exists.

## Key Facts / Claims

- **Purpose:** Bridges the calibration gap between conventional 10 × 10 cm dosimetry (ion chamber, TRS-398) and very small fields where ion chambers cannot be used. [intermediate-field-method][trs-483]
- **Core challenge addressed:** Solid-state detectors (diodes, diamond) exhibit energy-dependent response shifts in small fields due to reduced scatter and increasing electron fluence perturbation; they over-respond relative to dose-to-water. The intermediate step reduces the size-change magnitude at which this shift must be corrected. [intermediate-field-method][tg-155]
- **Six implementation steps:** (1) ion chamber calibration at 10 × 10 cm; (2) select intermediate field (typically 3–4 cm); (3) ion chamber reading at intermediate field; (4) cross-calibrate small detector at intermediate field; (5) small detector reads clinical field; (6) chain-multiply readings for output factor. [intermediate-field-method]
- **Intermediate field range:** Typically 2 × 2 to 4 × 4 cm; selected so that ion chambers can still be used reliably (fields ≥ 1.5 cm are within conventional ionization-chamber capability). [intermediate-field-method][trs-483]
- **Does NOT eliminate perturbation:** The method reduces but does not remove fluence perturbation corrections; separate k_{Q_clin,Q_msr} factors are still required for the small-field segment of the chain. [intermediate-field-method][tg-155]
- **Uncertainty propagation:** Uncertainties accumulate multiplicatively along the chain; combined small-field output factor uncertainty is ±1.5–2.5% (k=1) for 1–2 cm fields using this method. [linac-small-field-dosimetry-process-tree]
- **Positioning tolerance:** ±0.1 mm required for the detector at fields < 1 cm; ±0.5 mm for 1–3 cm fields. [intermediate-field-method]
- **TG-155 caution:** "If better detectors are available, they should be purchased and used so one does not need to over-rely on the daisy-chain method." Plastic scintillators and microDiamond reduce reliance on this chain. [tg-155]
- **TRS-483 designation:** Classified as "Method B" in the output factor measurement hierarchy (standard Method A for ≥ 3 cm; intermediate Method B for 1–3 cm; small-field Method C for < 1 cm). [linac-small-field-dosimetry-process-tree]

## Connections

- [[small-field-output-correction-factors]] — Even with the intermediate method, k_{Q_clin,Q_msr} factors are still required for the small-field segment; this method modifies the normalization reference, not the correction factor need
- [[small-field-detectors]] — The method cross-calibrates a small detector (microDiamond, unshielded diode) at the intermediate field before deployment in < 1 cm conditions
- [[small-field-commissioning]] — The intermediate field method is Phase 5 Method B in the conventional linac output factor workflow
- [[iaea-trs-483]] — TRS-483 provides the normative framework for Method B in small-field output factor measurement
- [[aapm-tg-155]] — TG-155 provides updated positioning tolerances, cautions about daisy-chain reliance, and detector recommendations for the intermediate step
- [[lateral-charged-particle-equilibrium]] — r_LCPE determines which fields are accessible to direct ionization chamber measurement and therefore defines the upper end of the intermediate field range

## Open Questions

- At what intermediate field size does chain uncertainty reach a minimum? Is 3 × 3 cm always the optimal choice, or does this depend on beam energy and detector type?
- Can the intermediate field method be automated in water tank scanning software to reduce the positioning tolerance challenge?

## Raw Notes

- TG-155 notes that the "daisy-chain" normalizes out large-field fluence perturbation enhancement but does NOT account for small-field fluence perturbation; better detectors make the method less necessary (see also [[small-field-output-correction-factors]] Raw Notes).
- For FFF beams, the intermediate step also partially averages out the non-uniform fluence profile that complicates single-step small-field measurement.
