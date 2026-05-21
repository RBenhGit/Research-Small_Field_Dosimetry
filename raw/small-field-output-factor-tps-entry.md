# Small Field Output Factor Determination for TPS Entry

**Source:** Gemini conversation (Deep Research), published 2026-04-15
**Topic:** Which output factor value to enter into the beam configuration of a Treatment Planning System (TPS) for small fields, per IAEA TRS-483.

---

## Question

According to small field dosimetry code of practice, the field size is determined by its FWHM and not the jaws configuration. What output factor should I enter to the beam configuration data? The output measured on a 1×1 jaws, or converting to the equivalent field size given by its FWHM and then extrapolating to 1×1?

---

## Answer (per IAEA TRS-483)

### Short Answer

Enter the output factor measured for the **1×1 cm² jaw setting**, but that measurement must be corrected using the k factor corresponding to the **actual measured FWHM** of that field. Do NOT extrapolate to a hypothetical field with a 1.0 cm FWHM unless the TPS explicitly indexes its tables by FWHM (which is rare).

---

### Detailed Workflow

For a clinical field f_clin (e.g., 1×1 cm² nominal field):

1. **Measure the Profiles:** Set jaws to 1×1 cm² and measure cross-plane and in-plane profiles at the reference depth (typically 10 cm).

2. **Determine S_clin:** Calculate the equivalent square field size as the geometric mean of the FWHM in both directions:

   S_clin = sqrt(FWHM_x × FWHM_y)

   In small fields, a 1×1 cm² jaw setting may produce a FWHM slightly larger (e.g., 1.05 cm) or smaller depending on linac type and source occlusion.

3. **Select the Correction Factor (k):** Look up the detector-specific output correction factor in TRS-483 tables (e.g., Tables 26 or 27) using the **actual S_clin** (e.g., 1.05 cm), not the nominal 1.0 cm.

4. **Calculate the Field Output Factor (Ω):**

   Ω = (M_f_clin / M_f_msr) × k

   where M_f_clin is the measurement at the 1×1 cm² jaw setting.

---

### Entering Data into the TPS

Treatment Planning Systems generally use the **nominal collimator setting** as the index for their beam configuration tables. When the TPS beam model calculates dose for a "1×1" field, it looks for the output factor associated with the machine setting of 1×1 cm².

- **The Mismatch:** If you extrapolate to a field with an exact 1.0 cm FWHM, you are finding the output for a physical state the machine does not necessarily produce at its 1×1 cm² jaw setting. This introduces a systematic error in the beam model.

- **The Accurate Approach:** The value entered for the 1×1 cm² entry in the TPS is the Ω calculated from the measurement of the 1×1 cm² jaw setting, **properly corrected for the beam's actual physical dimensions (S_clin)**.

---

### Summary Table

| Step            | Field Reference       | Value Used                 |
|-----------------|-----------------------|----------------------------|
| Measurement     | Nominal (1×1 cm²)     | M_f_clin                   |
| Profile Analysis| Physical (FWHM)       | Determine S_clin           |
| TRS-483 Lookup  | Physical (FWHM)       | Find k for S_clin          |
| TPS Entry       | Nominal (1×1 cm²)     | Enter corrected Ω          |

---

### Note on Extrapolation

Extrapolation is only recommended by TRS-483 if:
- No detector correction data exists for your specific S_clin, or
- You are trying to characterize fields smaller than your smallest measurable jaw setting.

For a standard 1×1 cm² commissioning point, use the corrected measurement of that specific jaw setting.
