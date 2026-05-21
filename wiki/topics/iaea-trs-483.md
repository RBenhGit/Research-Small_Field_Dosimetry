# IAEA TRS-483

**Type:** Entity
**Status:** mature
**Last updated:** 2026-05-21
**Sources:** [trs-483], [tg-155]

## Summary

IAEA Technical Reports Series No. 483 — *Dosimetry of Small Static Fields Used in External Beam Radiotherapy: An International Code of Practice for Reference and Relative Dose Determination* — is the first internationally adopted code of practice dedicated exclusively to small static field dosimetry. Published jointly by the IAEA and AAPM in 2017, it formalizes the Alfonso et al. (2008) dosimetry framework and provides reference and relative dosimetry procedures for photon beams up to 10 MV, including machines that cannot establish a conventional 10 cm × 10 cm reference field.

## Key Facts / Claims

- **Document identity:** IAEA Technical Reports Series No. 483; STI/DOC/010/483; ISBN 978-92-0-105916-1; published November 2017. [trs-483]
- **Scope:** Reference and relative dosimetry of small static photon fields up to 10 MV nominal accelerating potential. Does not cover electron, proton, or orthovoltage beams. [trs-483]
- **Motivation:** Conventional COPs (TRS-398, TG-51) are based on 10 cm × 10 cm reference conditions that cannot be realized on Gamma Knife, CyberKnife, TomoTherapy, and MLC-equipped linacs for SRS/SBRT, leading to dosimetric errors and patient-harm incidents. [trs-483]
- **Theoretical basis:** Alfonso et al. (2008) formalism introducing the *machine-specific reference* (msr) field concept and the *plan class specific reference* field. TRS-483 implements the static-field part only. [trs-483]
- **Two codes of practice:**
  1. **Section 5** — Reference dosimetry of msr fields (both WFF and FFF beams).
  2. **Section 6** — Relative dosimetry of small fields (field output factors, beam profiles, PDD). [trs-483]
- **Field size definition:** Uses the FWHM of the lateral dose profile at the measurement depth (irradiation field size), NOT the collimator setting (geometrical field size). [trs-483]
- **Tabulated data:** Appendix I — beam quality correction factors k_Q and uncertainties; Appendix II — field output correction factors k_{Q_clin,Q_msr}^{f_clin,f_msr} for many detector–linac combinations, with uncertainties. [trs-483]
- **Data cap:** Correction factors >5% in magnitude are not tabulated (excluded from this COP). [trs-483]
- **Uncertainty method:** GUM-based uncertainty analysis throughout. [trs-483]
- **Energy limit rationale:** ~80% of linacs installed post-2000 use ≤10 MV; 96.4% of SRS lung beams are 6 MV. Higher energies complicate small-field dosimetry via increased electron ranges and neutron production. [trs-483]
- **Summary paper:** Palmans et al., *Med Phys* 2018;45:e1123–e1145 provides a concise summary of TRS-483 methodology. [tg-155]
- **Corrections note for microDiamond:** Das and Francescon (2018) highlighted differences between TRS-483 tabulated microDiamond correction factors and more recent literature values. [tg-155]

## Connections

- [[small-field-definition]] — TRS-483 defines field size by FWHM and specifies the three physical conditions that make a field "small"
- [[machine-specific-reference-field]] — The msr field concept is the cornerstone of TRS-483's reference dosimetry formalism
- [[small-field-output-correction-factors]] — TRS-483 Appendix II provides the primary tabulated source of k_{Q_clin,Q_msr}^{f_clin,f_msr} values
- [[reference-dosimetry-kq]] — TRS-483 Section 5 provides beam quality correction factors for msr reference dosimetry
- [[lateral-charged-particle-equilibrium]] — r_LCPE is the physical parameter TRS-483 uses to quantify when small-field conditions exist
- [[small-field-detectors]] — TRS-483 Chapter 4 characterizes detectors for msr and relative small-field dosimetry
- [[cavity-theory]] — The k_{Q_clin,Q_msr} factors are grounded in Spencer–Attix cavity theory with perturbation corrections
- [[aapm-tg-155]] — TG-155 is the complementary AAPM report covering relative dosimetry aspects not fully addressed in TRS-483

## Open Questions

- When will TRS-483 tabulated correction factors be updated? Some data (especially for microDiamond) have been superseded by post-2017 publications.
- TRS-483 covers only static fields; the plan-class specific reference field formalism (for composite/IMRT fields) was deferred — is a Part 2 planned?

## Raw Notes

- TRS-483 is freely available from IAEA publications.
- The msr field for Gamma Knife is 1.6 cm or 1.8 cm diameter cone; for CyberKnife 6.0 cm diameter; for TomoTherapy 5 cm × 20 cm; for linac IMRT/VMAT the 10×10 cm² conventional field applies. [trs-483]
