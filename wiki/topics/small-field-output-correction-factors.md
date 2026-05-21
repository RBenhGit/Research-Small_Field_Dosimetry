# Small-Field Output Correction Factors

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-22
**Sources:** [trs-483], [tg-155], [nahum-cavity-theory-2009], [linac-small-field-dosimetry-process-tree], [small-field-output-factor-tps-entry]

## Summary

The small-field output correction factor k_{Q_clin,Q_msr}^{f_clin,f_msr} (also written k_{Q_clin,Q_msr}) is a detector-specific correction factor that accounts for the difference in a detector's response between the clinical non-reference field (f_clin) and the machine-specific reference field (f_msr). It is the key quantity distinguishing small-field dosimetry from conventional dosimetry, and its value deviates from unity — sometimes by more than 10% — when a detector is used in a non-equilibrium small field. TRS-483 provides tabulated values for many detector/linac combinations; TG-155 provides updated data and detector selection guidance.

## Key Facts / Claims

- **Physical definition:** k_{Q_clin,Q_msr}^{f_clin,f_msr} = (D_w,Q_clin^f_clin / M^f_clin_Q_clin) / (D_w,Q_msr^f_msr / M^f_msr_Q_msr) — the ratio of dose-to-water per detector reading in the clinical field to the same ratio in the msr field. [trs-483]
- **Role in the dosimetry chain:** The absorbed dose to water in the absence of the detector in clinical field f_clin is given by:
  D_w,Q_clin^f_clin = D_w,Q_msr^f_msr × Ω_{Q_clin,Q_msr}^{f_clin,f_msr}
  where the field output factor Ω = (M^f_clin_Q_clin / M^f_msr_Q_msr) × k_{Q_clin,Q_msr}^{f_clin,f_msr} [tg-155]
- **Theoretical expression (Spencer–Attix + perturbation):**
  k_{Q_clin,Q_msr} = [(L/ρ)^w_air × P_fl × P_gr × P_stem × P_cel × P_wall]_{f_clin} / same_{f_msr}
  where P_gr ≡ P_ρ × P_vol accounts for mass density and volume effects. [tg-155]
- **Preferred calculation method:** Direct Monte Carlo computation of the double ratio (Eq. 4 in TG-155), because the individual perturbation factor contributions are not independent in non-equilibrium small fields. [tg-155]
- **Wide variation between detectors:** At field size 5×5 mm², k factors for different detectors span a range of ~±15% around unity. Recommended detectors (plastic scintillator, microDiamond, microSilicon) have k close to 1.0; PTW PinPoint microchamber can deviate by >10%; shielded diodes over-respond in small fields. [tg-155]
- **Field size dependence:** k factors are predominantly determined by the field size (FWHM-based S_clin), not by linac model or energy for a given nominal MV; a single curve can be used across linac types for most detectors. [tg-155]
- **TRS-483 tabulation:** Appendix II of TRS-483 provides k_{Q_clin,Q_msr}^{f_clin,f_msr} tables for ~15 detector types across CyberKnife, Gamma Knife, Varian, Elekta, and Siemens linacs, with uncertainty estimates. Correction factors >5% in magnitude are excluded. [trs-483]
- **TRS-483 linac-specific tables:** **Table 24** (6 MV) and **Table 27** (10 MV) provide detector-specific k factors for conventional linacs; linear interpolation in field size space is used for field sizes not explicitly listed. [linac-small-field-dosimetry-process-tree]
- **WFF/FFF correction factor equivalence:** Tables 24 and 27 show no significant difference between flattened (WFF) and unflattened (FFF) beams at the same nominal energy; the same tables apply to both beam types. FFF-specific effects (dose-rate dependence, higher recombination) require separate checks but do not alter the tabulated k values. [linac-small-field-dosimetry-process-tree]
- **5×5 mm² field:** For this very small field, for fields <1×1 cm², accurate results require an appropriate correction factor; for fields ≥1×1 cm² the 0.8% variation across most detectors is manageable. [tg-155]
- **Detectors with near-unity k (recommended):** Plastic scintillators (PSD W1/W2), unshielded stereotactic silicon diode, single-crystal microDiamond (>1×1 cm²), microSilicon. [tg-155]
- **Detectors to avoid in very small fields:** Large-volume ionization chambers (Farmer type), shielded diodes (tungsten filter introduces extra scatter and directional dependence), PinPoint chambers (oriented perpendicular). [tg-155]
- **Uncertainty budget:** k factor can be provided by MC with overall uncertainty <0.7% (1 SD) for the largest contributing terms; total field output factor uncertainty is ~0.75–1% (1 SD) for careful measurements in a homogeneous water medium. [tg-155]
- **Source slug for field size:** Field size parameter S_clin = √(FWHM_x × FWHM_y); k is determined experimentally as a function of S_clin, the depth of measurement, and detector type. [tg-155]
- **TPS entry uses nominal jaw as index:** When applying the corrected Ω to a TPS beam model, the table is indexed by the nominal jaw setting (e.g., "1×1 cm²"), not by the FWHM-based S_clin. The k factor is looked up at the actual measured S_clin (which may be 1–3 mm larger than the jaw setting), but the resulting Ω is stored under the nominal jaw label. Extrapolating Ω to match an exact FWHM introduces systematic TPS error. [small-field-output-factor-tps-entry]

## Connections

- [[iaea-trs-483]] — Primary normative source of tabulated k_{Q_clin,Q_msr} values (Appendix II)
- [[aapm-tg-155]] — Provides updated data, detailed detector comparisons (Figures 9–11), and key recommendations
- [[machine-specific-reference-field]] — k factors are defined relative to the msr field; their value is 1.0 at f_msr by definition
- [[small-field-definition]] — k deviates increasingly from unity as the field size drops below the small-field threshold (~2×r_LCPE)
- [[lateral-charged-particle-equilibrium]] — Loss of LCPE is the primary physical driver of k ≠ 1 in small fields
- [[small-field-detectors]] — Detector choice determines the magnitude of k; near-unity k detectors reduce the correction burden
- [[cavity-theory]] — Spencer–Attix stopping-power ratios and perturbation factors (P_fl, P_gr, P_wall, etc.) from cavity theory are the theoretical components of k_{Q_clin,Q_msr}
- [[intermediate-field-method]] — The daisy-chain method reduces the size of correction required at each step by cross-calibrating detectors at an intermediate field; k factors are still needed for the small-field segment
- [[small-field-commissioning]] — Phases 5–6 of the commissioning workflow apply the k factors from Tables 24/27 to measured output readings
- [[tps-beam-configuration]] — The corrected Ω from this page is entered into TPS indexed by nominal jaw setting; the nominal/physical distinction is critical for correct TPS commissioning

## Open Questions

- How transferable are TRS-483-tabulated k values to newly commissioned linac models not included in the original dataset?
- For sub-5 mm fields (e.g., Gamma Knife 4 mm cone), what is the achievable measurement uncertainty and which detector is most reliable?
- Can the daisy-chain normalization method substitute for explicit MC-calculated k factors in clinical practice for fields between 3 mm and 10 mm?

## Raw Notes

- The TG-155 figure 9 shows that even among "good" detectors (microDiamond, microSilicon, PSD), the spread is up to ±1.5% at 5×5 mm² fields; this is the floor of what can be achieved with a single detector correction.
- An important caveat from TG-155: the daisy-chain (intermediate field) technique normalizes out the large-field fluence perturbation enhancement but does NOT account for small-field fluence perturbation effects; better detectors make this method less necessary.
