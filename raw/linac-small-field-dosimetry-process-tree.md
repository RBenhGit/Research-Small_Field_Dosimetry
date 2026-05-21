# Linear Accelerator Small Field Dosimetry — Process Tree

**Source type:** Claude artifact (process tree document)
**Artifact ID:** bec02402-375e-40a0-82ea-6a5ede989a6a
**Coverage:** Output factor determination for conventional linacs, 6 MV and 10 MV, per IAEA TRS-483

---

## Scope and Applicability

- Applies to conventional linacs from Varian, Elekta, Siemens
- Field size range: 0.5 cm × 0.5 cm to 10 cm × 10 cm (reference field)
- Explicitly excludes: CyberKnife, Gamma Knife, TomoTherapy (require alternative approaches)
- Covers both WFF (With Flattening Filter) and FFF (Flattening Filter Free) beams

---

## Nine-Phase Structured Methodology

### Phase 1 — Linac Qualification & QA
Baseline performance verification including:
- Daily output constancy check
- Laser alignment
- MLC positional accuracy

### Phase 2 — Reference Dosimetry
- Beam quality determination via TPR₂₀,₁₀ measurement
- Absorbed dose calibration per TRS-398

### Phase 3 — Detector Selection
Algorithm-based detector choice optimized for specific field size ranges:
- **≥ 3 cm fields:** Small ionization chambers (e.g., PTW 31010 Semiflex, IBA CC01)
- **1–3 cm fields:** Intermediate Field Method combining ion chambers with microDiamond or unshielded diodes
- **< 1 cm fields:** PTW 60019 microDiamond preferred; plastic scintillator as reference standard
- **< 0.5 cm fields:** Extreme uncertainty (±5–7%); multiple detectors mandatory

### Phase 4 — Geometric Characterization
- Field size measurement via FWHM determination at 10 cm depth
- Penumbra analysis

### Phase 5 — Output Factor Measurement (Three Methods)

#### Method A — Standard (fields ≥ 3 cm)
- Interleaved reference field measurements to detect beam output drift
- Readings corrected for temperature, pressure, polarity, ion recombination

#### Method B — Intermediate Field Method (1–3 cm)
- Chains ion chamber measurements (10 cm → 3–4 cm) with small detector measurements (3–4 cm → clinical field)
- Minimizes energy-dependent corrections by reducing the size step at each stage

#### Method C — Small Field Method (< 1 cm)
- Direct measurement with appropriate small-field detector
- Mandatory multi-detector verification

### Phase 6 — Correction Factor Application
- Look up and interpolate from TRS-483 Tables 24 (6 MV) and 27 (10 MV)
- Tables cover both WFF and FFF beams (see WFF vs. FFF section below)
- Linear interpolation in field size space for field sizes not explicitly listed

### Phase 7 — Multi-Detector Verification
- Independent measurements with ≥ 2 detector types for validation

### Phase 8 — TPS Commissioning
- Source size optimization
- Beam model validation

### Phase 9 — QA Program
- Documentation and annual re-measurement protocols

---

## WFF vs. FFF Equivalence

A significant finding: correction factors show "no significant difference" between flattened and unflattened beams at the same nominal energy. Combined use of Tables 24 and 27 for both beam types is valid.

FFF-specific considerations:
- Higher dose rates → dedicated dose-rate dependence testing required
- Higher ion recombination in chambers

---

## Uncertainty Budget (component-level)

| Scenario | Combined uncertainty (k=1) |
|---|---|
| Reference dosimetry | ±0.9% |
| Fields ≥ 2 cm with appropriate detectors | ±1–2% |
| Fields 1–2 cm via Intermediate Field Method | ±1.5–2.5% |
| Fields < 1 cm | ±4–6% |

**Note:** Sub-5 mm linac fields represent "research rather than clinical dosimetry" for fields below 0.5 cm.

---

## Critical Implementation Requirements

1. Measure FWHM at precisely 10 cm depth (correction factors valid only at this depth)
2. Use only TRS-483-validated detectors
3. Perform independent verification with ≥ 2 detector types
4. Mandatory dose-rate testing for FFF beams

---

## Conventional Linac Advantages for TRS-483 Implementation

- Ability to establish true 10 × 10 cm reference field (unlike dedicated SRS units)
- Extensive correction factor database covering 25+ detector types
- Flexible collimation options (MLC, circular cones, jaws)
- Both WFF and FFF beams have validated correction factor equivalence
