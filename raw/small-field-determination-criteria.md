# Small Field Determination Criteria in Radiation Therapy Dosimetry

**Source type:** Claude artifact (technical document)
**Artifact ID:** de458e9e-3c29-44e8-937a-5079249a5ab7
**Coverage:** Quantitative methods for identifying when radiation therapy fields require specialized dosimetry

---

## Summary

A field qualifies as "small" when it meets at least one of three conditions:

1. **Loss of Lateral Charged Particle Equilibrium (LCPE)** on the beam central axis — when field dimensions fall below 2 × r_LCPE
2. **Partial occlusion of the primary photon source** — reducing effective source size and photon fluence
3. **Detector dimensions comparable to field dimensions** — causing substantial volume averaging effects

---

## Field Size Determination Method

**Standard approach: FWHM at 10 cm depth**

- Identify the 50% dose points on both sides of the dose maximum in the lateral profile
- The distance between these points defines the field size (irradiation field size)
- Measurement depth: 10 cm in water
- **FWHM-defined sizes often exceed geometric collimator settings by 1–3 mm** due to penumbra effects

---

## Key Clinical Thresholds

**6 MV beams (most common clinically):**
- r_LCPE ≈ 1.2 cm
- Fields smaller than approximately **2.4 cm × 2.4 cm** experience LCPE loss on central axis

**Higher energy beams:**
- Have larger equilibrium ranges (larger r_LCPE)
- More fields are subject to small-field classification at any given collimator setting

---

## Patient Safety Context

Documented incidents have involved up to **15% discrepancies** in field output measurements for 0.6 cm × 0.6 cm fields when inappropriate detectors were used without correction factors. This highlights the critical importance of proper small field recognition and dosimetry protocols.

---

## Practical Checklist for Field Classification

A field should be treated as small if ANY of the following are true:
- Field dimension < 2 × r_LCPE for the beam energy (e.g., < 2.4 cm for 6 MV)
- Field dimension approaches or is smaller than the focal spot FWHM
- Any detector outer edge lies within r_LCPE of the field edge
- FWHM-based field size and collimator setting differ significantly (>1–2 mm)
