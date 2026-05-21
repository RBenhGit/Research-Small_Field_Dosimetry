# Small Field Definition

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-21
**Sources:** [trs-483], [tg-155], [small-field-determination-criteria]

## Summary

A photon radiation field is designated "small" when at least one of three physical conditions holds: loss of lateral charged particle equilibrium (LCPE) on the beam axis, partial occlusion of the primary photon source by the collimating devices, or the detector size being similar to or larger than the beam dimensions. These conditions each cause the conventional dosimetry framework (calibration at a 10 cm × 10 cm reference field) to break down. For practical purposes at 6 MV, fields ≤3 cm × 3 cm are generally small; the exact threshold is beam-energy-dependent and quantified through the LCPE range r_LCPE.

## Key Facts / Claims

- **Three defining conditions** (TRS-483 §1.1.1; TG-155 §3): (i) loss of LCPE on beam axis; (ii) partial occlusion of primary photon source by collimating devices; (iii) detector size similar to or larger than beam dimensions. All three result in overlap between field penumbrae and the detector volume. [trs-483][tg-155]
- **Beam-related conditions:** LCPE is lost when the beam half-width/radius is smaller than the maximum secondary-electron range (r_LCPE). Source occlusion occurs when the field size is comparable to or smaller than the focal spot size (~0.5–3 mm for modern linacs). [trs-483]
- **Detector-related condition:** Volume averaging and fluence perturbation become significant when any outer edge of the detector lies within r_LCPE of a field edge. [trs-483]
- **Practical 6 MV threshold:** Fields ≤3 cm × 3 cm should be treated as small for most photon energies per TG-155. [tg-155]
- **TRS-483 field size convention:** Field size is defined as the FWHM of the lateral dose profile at the measurement depth (irradiation field size), NOT the collimator setting (geometrical field size). [trs-483]
- **FWHM measurement approach:** Identify the 50% dose points on both sides of the dose maximum in the lateral profile; the distance between them is the irradiation field size. FWHM-defined sizes typically exceed geometric collimator settings by **1–3 mm** due to penumbra effects. [small-field-determination-criteria]
- **Measurement depth:** 10 cm depth recommended (eliminates electron contamination contribution; also the depth at which TRS-483 correction factors are validated). [trs-483][linac-small-field-dosimetry-process-tree]
- **6 MV LCPE-based threshold (quantified):** r_LCPE ≈ 1.2 cm for 6 MV; fields smaller than approximately **2.4 cm × 2.4 cm** experience LCPE loss on the central axis. Higher energy beams have larger r_LCPE, making more fields subject to small-field classification. [small-field-determination-criteria]
- **Patient safety incidents:** Documented discrepancies of **up to 15%** in field output measurements for 0.6 cm × 0.6 cm fields when inappropriate detectors were used without correction factors, underscoring the consequences of misclassifying a small field. [small-field-determination-criteria]
- **Equivalent square small field:** S_clin = √(FWHM_x × FWHM_y) for rectangular or asymmetric fields. [tg-155]
- **Apparent field widening:** In small fields, penumbrae from opposing jaws overlap and lower the central axis dose; the 50% dose level (FWHM) migrates outward onto the penumbra curve, making the irradiation field size larger than the collimator setting. This congruence between collimator setting and FWHM breaks down for very small fields. [trs-483]
- **TG-155 practical criterion:** A field should be considered small if the distance from the central axis to the field edge is smaller than r_LCPE + detector half-dimension. [tg-155]
- **Geometrical vs. irradiation field size:** IEC defines both; in broad beams they are equal (FWHM = collimator setting); in small fields the irradiation size (FWHM) exceeds the geometrical size. TRS-483 advises recording both when reporting small-field data. [trs-483]
- **Source occlusion effect:** When field size approaches the focal spot size, the collimator blocks part of the focal spot, reducing on-axis fluence and creating steep dose gradients. For modern linacs (e.g., Varian TrueBeam), focal spot FWHM is 0.7–0.9 mm; source occlusion is significant for fields ≤2 cm × 2 cm. [tg-155]
- **Minimum collimator settings (examples from TG-155 Table 1):**
  - Linac IMRT/VMAT: 0.1 × 0.1 cm²; msr = 10×10 cm²
  - Linac SRS: 0.5 cm² cone; msr = 10×10 cm²
  - CyberKnife: 0.5 cm diameter; msr = 6.0 cm diameter
  - Gamma Knife: 0.4 cm diameter; msr = 1.6 or 1.8 cm diameter cone [tg-155]

## Connections

- [[lateral-charged-particle-equilibrium]] — r_LCPE quantifies the energy-dependent threshold for LCPE loss and is the key parameter in the small-field definition
- [[machine-specific-reference-field]] — The msr field is the reference substitute when standard 10×10 cm² conditions cannot be realized on the treatment machine
- [[iaea-trs-483]] — Provides the normative field size definition (FWHM convention) and the COP framework
- [[aapm-tg-155]] — Provides practical thresholds and guidance on applying the small-field definition
- [[small-field-output-correction-factors]] — Output correction factors are tabulated as a function of the irradiation field size (FWHM-based S_clin)
- [[small-field-detectors]] — Detector size relative to field size is the third defining condition; detector choice follows from this
- [[small-field-commissioning]] — The commissioning workflow uses FWHM characterization (Phase 4) to determine which measurement method applies for a given field

## Open Questions

- For FFF beams, the FWHM-collimator congruence also breaks down at larger field sizes than for WFF beams — is there an FFF-specific practical threshold comparable to "≤3 cm × 3 cm"?
- How should field size be reported for non-circular Gamma Knife plans with multiple isocentres?

## Raw Notes

- TG-155 notes that the equivalent square definition S_clin = √(FWHM_x × FWHM_y) has not been fully verified for specialized machines like Gamma Knife, CyberKnife, and TomoTherapy; these require machine-specific data collection approaches.
