# Reference Dosimetry: Beam Quality Correction Factor k_Q

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-21
**Sources:** [trs-483], [tg-155], [nahum-cavity-theory-2009]

## Summary

The beam quality correction factor k_Q (or k_{Q,Q0}) converts an ionization chamber's absorbed-dose-to-water calibration coefficient N_{D,w,Q0} — determined at a reference quality Q0, typically Co-60 — to the user's beam quality Q. It encapsulates all the physics of how the chamber's response changes with beam quality: differences in water-to-air stopping-power ratios, perturbation correction factors, and photon spectrum. In the small-field context, TRS-483 extends this to k_{Q_msr,Q0}^{f_msr,f_ref}, which additionally corrects for the difference between the machine-specific reference field f_msr and the conventional reference field f_ref.

## Key Facts / Claims

- **Standard definition:** k_Q = (N_{D,w,Q} / N_{D,w,Q0}); the absorbed dose to water in a user beam of quality Q is D_w,Q = M_Q × N_{D,w,Q0} × k_{Q,Q0}. [trs-483]
- **Physical content of k_Q:**
  k_{Q,Q0} ∝ [(s_{w,air})_Q × p_Q] / [(s_{w,air})_{Q0} × p_{Q0}]
  where s_{w,air} is the Spencer–Attix water-to-air stopping-power ratio and p_Q is the overall perturbation correction factor product at quality Q. [nahum-cavity-theory-2009]
- **Conventional reference conditions:** f_ref = 10 cm × 10 cm at SSD = 100 cm; reference depth z_ref = 10 g/cm² (TRS-398, TG-51). [trs-483]
- **Beam quality specifier:** TPR_20,10(10) (TRS-398) or %dd(10)_x (TG-51) — both specify beam quality for the conventional 10×10 cm² field. [trs-483]
- **TRS-483 extension for msr field:** k_{Q_msr,Q0}^{f_msr,f_ref} = k_{Q,Q0} × k_{Q_msr,Q}^{f_msr,f_ref}
  The factor k_{Q_msr,Q}^{f_msr,f_ref} corrects for the change in detector response between the conventional reference field and the msr field at the same beam quality Q. [trs-483]
- **When k_{Q_msr,Q}^{f_msr,f_ref} = 1:** For linacs where f_msr = f_ref (10×10 cm²), this factor is unity and TRS-483 reduces to conventional COP dosimetry. [trs-483]
- **Beam quality index for msr machines:** Machines that cannot establish 10×10 cm² conditions (CyberKnife, Gamma Knife, TomoTherapy) require an alternative procedure to determine the beam quality specifier. TRS-483 §5.3.3 provides methods: (i) extrapolation of TPR_20,10(S) measured at multiple field sizes to S=10 cm; (ii) use of machine-type-specific k_{Q_msr,Q0} values determined for a representative machine of the same type. [trs-483]
- **TPR_20,10(S) extrapolation (TRS-483):** For field sizes S between 4 cm and 12 cm, TPR_20,10(S) depends linearly on field size; the relationship is used to derive the equivalent TPR_20,10(10) for a conventional 10×10 cm² beam. [trs-483]
- **FFF beam quality:** For flattening-filter-free beams, %dd(10)_x and TPR_20,10(10) must be measured with care; the correction for electron contamination is larger for FFF beams. TRS-483 gives specific guidance. [trs-483]
- **k_Q tables:** TRS-483 Appendix I tabulates k_{Q_msr,Q0}^{f_msr,f_ref} for recommended chamber types for Gamma Knife, CyberKnife, TomoTherapy, and linac msr fields, with associated uncertainties. [trs-483]
- **Uncertainty of k_Q:** Typically 0.5–1.5% (1 SD) depending on the chamber type and beam quality; the msr extension adds ~0.3–0.5% additional uncertainty for specialized machines. [trs-483]
- **PSDL calibration preference:** The preferred approach (TRS-483 §5.1) is to obtain N_{D,w,Q_msr}^{f_msr} directly in the msr field from a primary standards laboratory, eliminating the k_{Q_msr,Q0} correction entirely. [trs-483]

## Connections

- [[cavity-theory]] — k_Q is the protocol-level embodiment of Spencer–Attix stopping-power ratios and ion-chamber perturbation factors (P_wall, P_cel, P_fl, P_repl)
- [[stopping-power-ratios]] — The dominant component of k_Q is the change in Spencer–Attix water-to-air stopping-power ratio s_{w,air} with beam quality
- [[machine-specific-reference-field]] — TRS-483 introduces k_{Q_msr,Q0}^{f_msr,f_ref} as the extended beam quality correction factor for msr dosimetry
- [[iaea-trs-483]] — The normative source for k_Q procedures and tabulated values for small-field reference dosimetry
- [[small-field-output-correction-factors]] — k_{Q_clin,Q_msr} is the relative dosimetry analogue of k_Q; both correct for detector response changes, but k_Q is for reference field calibration while k_{Q_clin,Q_msr} is for output factor measurement

## Open Questions

- For FFF beams, what is the achievable uncertainty in beam quality determination when the electron contamination correction to %dd(10)_x is large?
- Are there published experimental k_{Q_msr,Q0} values for the latest CyberKnife M6 and TomoTherapy Radixact systems that supersede the TRS-483 Appendix I tables?

## Raw Notes

- In TG-51, the notation is k_Q and the reference quality Q0 is always Co-60. In TRS-398, the notation is k_{Q,Q0} to make the reference quality explicit. TRS-483 follows TRS-398 notation.
- The distinction between k_Q (beam quality correction, conventional reference) and k_{Q_clin,Q_msr} (output correction, relative dosimetry) is critical: they operate at different points in the dosimetry chain.
