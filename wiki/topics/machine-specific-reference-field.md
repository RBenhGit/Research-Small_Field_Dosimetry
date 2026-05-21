# Machine-Specific Reference Field (msr)

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-21
**Sources:** [trs-483], [tg-155]

## Summary

The machine-specific reference (msr) field is an intermediate calibration field introduced by Alfonso et al. (2008) for radiotherapy machines that cannot establish the conventional 10 cm × 10 cm reference conditions (e.g., Gamma Knife, CyberKnife, TomoTherapy). It is defined as the largest field achievable on the machine, chosen as close as possible to the conventional reference field while still satisfying the geometric conditions required for ion chamber dosimetry. The msr field serves as the reference from which clinical field output factors (Ω) are determined.

## Key Facts / Claims

- **Origin:** Alfonso R, Andreo P, Capote R et al. (2008) *Med Phys* 35:5179–5186 introduced the msr field concept and the general dosimetry formalism for small and nonstandard fields. [tg-155]
- **Definition:** The msr field is the largest field that can be produced by a given machine, with dimensions as close as possible to those of the conventional reference field (f_ref, 10 cm × 10 cm at 100 cm SSD). It must extend at least r_LCPE beyond the outer boundaries of the reference ionization chamber. [trs-483]
- **Why needed:** Specialized systems (Gamma Knife, CyberKnife, TomoTherapy) and linacs in SRS mode cannot physically produce a 10×10 cm² field; using correction factors based on the conventional reference would introduce unacceptable uncertainty. [trs-483]
- **msr field examples:**
  - Linac (conventional): f_msr = f_ref = 10×10 cm² (no msr needed)
  - Gamma Knife: 1.6 cm or 1.8 cm diameter cone
  - CyberKnife: 6.0 cm diameter
  - TomoTherapy: 5 cm × 20 cm [tg-155]
- **Reference dosimetry formalism (TRS-483 Eq. 1a and 1b):**
  - D_w,Q_msr^f_msr = M^f_msr_Q_msr × N_D,w,Q0 × k_Q,Q0 × k_{Q_msr,Q0}^{f_msr,f_ref}
  - Or equivalently: D_w,Q_msr^f_msr = M^f_msr_Q_msr × N_D,w,Q_msr^f_msr × k_{Q_msr,Q0}^{f_msr,f_ref}
  where N_D,w,Q0 is the chamber calibration coefficient (Co-60), k_Q,Q0 is the conventional beam quality correction factor, and k_{Q_msr,Q0}^{f_msr,f_ref} corrects for the difference between the msr field and the conventional reference field. [trs-483][tg-155]
- **M correction factors:** The detector reading M^f_msr_Q_msr must be corrected for temperature/pressure, incomplete charge collection, polarity effect, and electrometer calibration (same as conventional dosimetry). [tg-155]
- **N_D,w,Q_msr option:** Some standards laboratories (e.g., for Gamma Knife) can provide a calibration coefficient directly in the msr field; this is the preferred approach when available. [trs-483]
- **Beam quality specifier for msr:** Conventional %dd(10)_x or TPR_20,10(10) are measured for a 10×10 cm² field; for machines where only smaller fields are achievable, TRS-483 Section 5.3.3 provides methods to derive the equivalent 10×10 quality index from measurements in smaller fields using TPR_20,10(S) extrapolation. [trs-483]
- **k_{Q_msr,Q0}^{f_msr,f_ref} magnitude:** For linacs with 10×10 cm² msr, this factor equals k_Q,Q0 and the two-step formula reduces to the conventional form. For other machines it is machine- and chamber-specific. [trs-483]
- **Machine type-specific correction factors:** A single k_{Q_msr,Q0}^{f_msr,f_ref} value can be used for all machines of the same type (e.g., all Gamma Knife models) with acceptable uncertainty, because beam quality varies little within a machine type. [trs-483]

## Connections

- [[iaea-trs-483]] — TRS-483 Section 5 is the primary COP for reference dosimetry in the msr field
- [[small-field-definition]] — The msr field must satisfy geometric conditions relative to r_LCPE and the detector size
- [[lateral-charged-particle-equilibrium]] — r_LCPE determines the minimum msr field radius relative to the reference ion chamber
- [[reference-dosimetry-kq]] — k_{Q_msr,Q0}^{f_msr,f_ref} is an extension of the conventional k_Q concept to account for field-size differences
- [[small-field-output-correction-factors]] — Clinical field output factors Ω are always measured relative to the msr field; the k_{Q_clin,Q_msr} factor corrects for detector response change between msr and clinical fields
- [[aapm-tg-155]] — TG-155 §2.1 outlines the IAEA-AAPM formalism including the role of f_msr

## Open Questions

- For linacs using a 10×10 cm² msr, is there any practical advantage to defining a smaller msr (e.g., 4×4 cm²) to bridge to very small clinical fields more smoothly?
- What is the uncertainty budget when deriving TPR_20,10(10) from TPR_20,10(S) for a machine that cannot achieve the 10×10 cm² reference?

## Raw Notes

- The notation "msr" is sometimes written as "MSR" in older literature. TRS-483 standardizes on "msr" (lowercase).
- For Varian TrueBeam and other modern linacs, the conventional 10×10 cm² field is achievable, so f_msr = f_ref and the msr correction factor is unity.
