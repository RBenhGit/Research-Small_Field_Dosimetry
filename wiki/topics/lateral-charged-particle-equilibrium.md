# Lateral Charged Particle Equilibrium (LCPE)

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-21
**Sources:** [trs-483], [tg-155]

## Summary

Lateral charged particle equilibrium (LCPE) is the condition in which the secondary electrons exiting a volume element laterally are exactly replaced by electrons entering laterally with the same energy spectrum. LCPE is established in a radiation field when the beam radius exceeds the maximum lateral range of secondary electrons (the LCPE range, r_LCPE). Its absence is the primary physical reason why small photon fields require a dedicated dosimetry formalism: without LCPE, the on-axis dose falls below what would be expected from the photon fluence alone, and conventional stopping-power-ratio-based cavity theory requires modification.

## Key Facts / Claims

- **Definition of r_LCPE:** The minimum radius of a circular photon field for which the collision kerma in water equals the absorbed dose to water at the field center (aside from a small correction for the centre of electron production in TCPE conditions). [trs-483]
- **r_LCPE values by beam quality (MC-derived, Li et al.):**

| Beam | TPR_20,10 | %dd(10 cm)_x | r_LCPE (cm) |
|------|-----------|--------------|-------------|
| Co-60 | 0.579 | 58.7 | 0.5 |
| 6 MV | 0.670 | 66.2 | 1.2 |
| 10 MV | 0.732 | 73.5 | 1.7 |
| 15 MV | 0.765 | 77.9 | 2.0 |
| 24 MV | 0.805 | 83.0 | 2.4 |

[tg-155]

- **Empirical equations for r_LCPE (TG-155):**
  - r_LCPE (cm) = 8.369 × TPR_20,10 − 4.382 (Eq. 7)
  - r_LCPE (cm) = 77.97 × 10^−3 × %dd(10)_x − 4.112 (Eq. 8)
  - These are based on flattened beams; use with caution for FFF beams. [tg-155]
- **Simplified practical estimate:** r_LCPE ≈ 0.67 × d_max ± 0.2 cm, where d_max is the depth of maximum dose (cm) for the 10×10 cm² reference field. [tg-155]
- **LCPE vs. CPE distinction:** LCPE concerns the lateral equilibrium; transient charged particle equilibrium (TCPE) concerns the forward/depth direction. CPE (complete) is rarely established in MV photon beams at depth. [trs-483]
- **Clinical implication:** For 6 MV, r_LCPE ≈ 1.2 cm, meaning a 6 MV beam is in small-field regime when its radius is <1.2 cm (diameter <2.4 cm), regardless of collimator setting. [tg-155]
- **Effect of losing LCPE on output:** Beam output (dose per MU) decreases steeply as field size drops below 2×r_LCPE; this is exacerbated when source occlusion also contributes. [trs-483]
- **Effect on stopping-power ratios:** Despite LCPE loss changing the photon spectrum, the water-to-air collision stopping-power ratio changes by <0.5% from the 10×10 cm² reference field down to 0.3×0.3 cm² for 6 MV. The main dosimetric uncertainty comes from perturbation correction factors, not the stopping-power ratio. [trs-483]
- **FFF beams:** For FFF beams, the %dd and TPR values are substantially lower than for WFF beams at the same nominal MV, but r_LCPE is similar to that of a WFF beam at the same accelerating potential. [tg-155]
- **Low-density media:** r_LCPE increases substantially in low-density media (lung, air); LCPE loss occurs at larger field sizes in heterogeneous regions. This is a particular concern for SBRT lung treatments. [tg-155]
- **TPS implication:** In inhomogeneous media, especially lung, the lateral range of secondary electrons and its relation to LCPE becomes more prominent — pencil beam convolution algorithms fail under these conditions. [tg-155]

## Connections

- [[small-field-definition]] — r_LCPE defines the energy-dependent threshold below which a field is "small"; the three small-field conditions all relate to this range
- [[machine-specific-reference-field]] — The msr field must extend at least r_LCPE beyond the reference ion chamber's outer boundaries
- [[small-field-output-correction-factors]] — Perturbation effects that grow as field size drops below r_LCPE are the physical origin of k_{Q_clin,Q_msr} deviating from unity
- [[cavity-theory]] — LCPE loss means B–G cavity theory conditions degrade; Spencer–Attix stopping-power ratios remain nearly constant but perturbation factors do not
- [[stopping-power-ratios]] — Despite LCPE loss, water-to-air stopping-power ratios are surprisingly stable (<0.5%) across small field sizes
- [[iaea-trs-483]] — TRS-483 uses r_LCPE as the fundamental parameter for characterizing small fields and selecting appropriate detectors

## Open Questions

- What are the r_LCPE values for FFF beams computed by the more recent Papaconstadopoulos MC calculations (TRS-483) versus the Li et al. values used in TG-155 Table 2?
- How does r_LCPE change in practical clinical scenarios involving air gaps and lung tissue within the beam path for SBRT?

## Raw Notes

- TG-155 notes that values in Table 2 may differ by ~1 mm from TRS-483 values (Papaconstadopoulos equation) due to different defining equations (one in terms of TPR_20,10, another in terms of %dd(10)_x).
- r_LCPE was earlier referred to in the literature as the "lateral electronic equilibrium" range (LEE) — the term LCPE is now standard.
