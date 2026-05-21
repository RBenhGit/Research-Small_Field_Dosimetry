# AAPM TG-155

**Type:** Entity
**Status:** mature
**Last updated:** 2026-05-21
**Sources:** [tg-155]

## Summary

AAPM Task Group 155 report — *Megavoltage photon beam dosimetry in small fields and non-equilibrium conditions* (Das IJ et al., *Medical Physics* 2021;48:e886–e921, DOI: 10.1002/mp.15030) — is the AAPM's companion guidance to IAEA TRS-483. While TRS-483 formalizes reference dosimetry of the msr field and provides tabulated correction factors, TG-155 focuses on the practical aspects of relative dose measurements: detector selection, beam profile acquisition, PDD/TMR/TPR measurement methodology, field output factor measurement, TPS beam modeling in small fields, and a summary of key recommendations.

## Key Facts / Claims

- **Authors:** Indra J. Das, Paolo Francescon, Jean M. Moran, Anders Ahnesjö, Maria M. Aspradakis, Chee-Wai Cheng, George X. Ding, John D. Fenwick, M. Saiful Huq, Mark Oldham, Chester S. Reft, Otto A. Sauer. [tg-155]
- **Publication:** *Medical Physics* 2021;48:e886–e921. Received 2 April 2021; accepted 2 June 2021. [tg-155]
- **Scope:** Relative dosimetry of megavoltage photon beams in small and non-equilibrium fields ≤6 MV focus; guidance for beams from accelerating potential ≤6 MV (most relevant for SRS/SBRT). Does not address kilovoltage beams for animal irradiation or composite fields. [tg-155]
- **Key contribution over TRS-483:** Detailed discussion of TPS dose modeling for small fields (source models, collimator geometry, MLC leaf tip leakage, dosimetric leaf gap); expanded guidance on measurement uncertainty; updated detector correction factor data beyond TRS-483 publication date. [tg-155]
- **Three-condition definition of small field:** (a) LCPE lost on beam axis; (b) collimating devices partially occlude primary photon source; (c) detector size similar to or larger than beam dimensions. Fields ≤3 cm × 3 cm are generally small for 6 MV. [tg-155]
- **Recommended detectors for ≤1 cm × 1 cm:** Unshielded stereotactic diode, electron diode, plastic scintillator (W1/W2), single-crystal microDiamond. [tg-155]
- **Recommended detectors for 1–1.5 cm × 1.5 cm:** Microchambers (excluding high-Z electrode types) are also suitable. [tg-155]
- **TPS beam modeling:** Pencil beam convolution (PBC) algorithms are inadequate for small fields; Monte Carlo, Boltzmann solvers, or point-kernel convolution/superposition are recommended; grid size ≤1 mm for MC, 2 mm for non-MC. [tg-155]
- **Uncertainty summary:** Field output factor measurement uncertainty ≈0.75% (1 SD) achievable with careful setup; increases significantly for fields <0.5 cm × 0.5 cm; main uncertainty source is MLC mechanical reproducibility. [tg-155]
- **Independent checks:** Small-field measurements should be independently verified (external audit such as IROC-Houston) and end-to-end phantom tests are recommended. [tg-155]
- **Daisy-chain method:** Can determine field output factors for the full range of clinical field sizes by linking diode measurements in small fields to ion chamber measurements in large fields — but does not account for fluence perturbation effects. [tg-155]

## Connections

- [[iaea-trs-483]] — TG-155 is explicitly complementary to TRS-483; recommends using TRS-483 tabulated k factors
- [[small-field-definition]] — Provides r_LCPE-based equations and a practical 3-cm threshold for 6 MV
- [[lateral-charged-particle-equilibrium]] — Provides r_LCPE values by energy and practical estimation equations
- [[small-field-detectors]] — Main source for detector characteristics, correction factors, and selection criteria
- [[small-field-output-correction-factors]] — Provides updated k factor data and recommends detectors with near-unity k
- [[reference-dosimetry-kq]] — Section 2.1 outlines the IAEA-AAPM formalism for reference dosimetry
- [[cavity-theory]] — Section 2.2 discusses detector response theory in small fields including Spencer-Attix-based k factor expressions

## Open Questions

- How should TPS beam models be validated specifically for FFF beams with very small fields (<1 cm)?
- What is the clinical impact on dosimetric accuracy when using an inappropriately large detector for PDD measurements in sub-cm fields?

## Raw Notes

- TG-155 references the AAPM 2009 Proceedings (Das et al., same authors as the nahum-cavity-theory-2009 source) as a comprehensive discussion on detectors for small fields.
- The report notes several high-profile radiation incidents (Bogdanich NYT 2010; Derreumaux et al. 2011 Vienna) that motivated the work.
