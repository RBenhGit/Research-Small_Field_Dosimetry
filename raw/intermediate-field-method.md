# Intermediate Field Method for Small Field Dosimetry

**Source type:** Claude artifact (technical document)
**Artifact ID:** 665a239b-51c4-442c-ba82-8230a2ab8032
**Coverage:** Intermediate field calibration chain as defined in IAEA TRS-483 and AAPM TG-155

---

## Overview

The intermediate field method (also called the "daisy-chain" or "chain normalization" method) establishes calibration traceability between standard reference field measurements and small field dosimetry by using an intermediate-sized field (typically 2 × 2 to 4 × 4 cm) as a bridge.

Recognized in: IAEA TRS-483 and AAPM Task Group 155

Purpose: extends measurements from conventional 10 × 10 cm fields down to submillimeter stereotactic fields.

---

## Core Challenge Being Addressed

Solid-state detectors (silicon diodes, diamond detectors) exhibit significant energy-dependent response variations with field size:
- In smaller fields, scattered photon contributions diminish, causing detector response to shift relative to dose-to-water
- Electron fluence perturbation effects become prominent, causing detectors to **over-respond** relative to undisturbed water medium
- These effects grow rapidly as field size decreases, making direct small-field measurement with correction factors uncertain

---

## Six-Step Implementation Process

1. **Reference field calibration:** Ionization chamber measurement in 10 × 10 cm field
2. **Intermediate field selection:** Choose an appropriate intermediate field size (typically 3 × 3 or 4 × 4 cm)
3. **Ion chamber measurement at intermediate field:** Establish reference reading at intermediate size
4. **Cross-calibration of small detector:** Calibrate the small detector (diode, microDiamond) at the intermediate field
5. **Small field measurements:** Use the cross-calibrated detector for small field output factors
6. **Chain multiplication:** Multiply readings through the chain to obtain final output factors

---

## Key Strengths

- Reduces the magnitude of energy-dependent corrections needed (each step is a smaller field-size change)
- Maintains traceability through reference ionization chambers
- Enables measurement of very small fields where ionization chambers fail (too large, too noisy)
- Provides a systematic calibration pathway across the full range of clinical field sizes

---

## Important Limitations

- **Does NOT eliminate** fluence perturbation effects in small fields — only reduces them
- Propagates uncertainties through multiple measurement steps (uncertainty accumulates)
- Requires meticulous positioning: **±0.1 mm tolerance** for fields < 1 cm
- Requires careful correction factor management at each step in the chain

TG-155 caution: "if better detectors are available, they should be purchased and used so one does not need to over-rely on the daisy-chain method."

---

## Positioning Requirements

| Field size | Positioning tolerance |
|---|---|
| ≥ 3 cm | ±1 mm |
| 1–3 cm | ±0.5 mm |
| < 1 cm | ±0.1 mm |

---

## Relationship to TRS-483 / TG-155

- TRS-483 describes the intermediate field method as Method B in the output factor measurement protocol
- TG-155 provides updated guidance and notes that it is especially useful for 1–3 cm fields
- Both protocols agree that this method is a valid alternative to direct measurement with large correction factors, but not a substitute for better detector selection when possible
