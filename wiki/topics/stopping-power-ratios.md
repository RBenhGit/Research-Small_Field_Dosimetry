# Stopping-Power Ratios

**Type:** Topic
**Status:** stub
**Last updated:** 2026-05-21
**Sources:** [nahum-cavity-theory-2009], [trs-483], [tg-155]

## Summary

The Spencer–Attix water-to-air mass collision stopping-power ratio s_{w,air} is the central quantity in Bragg–Gray cavity theory as applied to MV photon beam dosimetry: it converts an air-cavity ionization measurement to absorbed dose to water. For conventional (broad-beam, 10×10 cm²) reference conditions, s_{w,air} is well characterized by Monte Carlo as a function of beam quality (TPR or %dd). For small fields, the key finding from both TRS-483 and TG-155 is that s_{w,air} changes by less than 0.5% across all clinically relevant small field sizes, confirming that energy-spectral changes with field size do not significantly perturb the stopping-power ratio component of dosimetry.

## Key Facts / Claims

- **Spencer–Attix formulation:** s_{w,air} = ∫Φ_E (L_Δ/ρ)_{w} dE / ∫Φ_E (L_Δ/ρ)_{air} dE, where Φ_E is the electron energy fluence spectrum at the measurement point and Δ = 10 keV is the conventional cutoff energy. [nahum-cavity-theory-2009]
- **Stability in small fields:** Monte Carlo calculations show that the water-to-air stopping-power ratio changes by ≤0.5% from the 10×10 cm² reference field down to 0.3×0.3 cm² for a 6 MV beam, even a range of depths from z_max to 30 cm. [trs-483]
- **Why stable despite LCPE loss:** Although LCPE is lost, the photon fluence spectrum change is small (hardening, ~3–4% diode effect), and the charged particle spectrum in water is much less affected than the photon fluence. The water-to-air stopping-power ratio is governed by electron kinetics, not directly by photon spectrum. [trs-483]
- **Energy dependence:** s_{w,air} is tabulated as a function of beam quality for conventional reference fields; it increases from ~1.130 at Co-60 to ~1.120 at 6 MV and ~1.108 at 18 MV (illustrative values; see TRS-398 tables). [nahum-cavity-theory-2009]
- **Consequence for k_{Q_clin,Q_msr}:** Because s_{w,air} changes negligibly with field size, the deviations of k_{Q_clin,Q_msr} from unity in small fields arise almost entirely from the perturbation correction factor components (P_fl, P_gr, P_vol, P_wall), not from stopping-power ratio changes. [tg-155]
- **Silicon diodes:** The water-to-silicon stopping-power ratio is NOT stable with field size, because silicon's higher density and higher mass energy-absorption coefficient for low-energy photons causes the ratio to vary by 3–4% across field sizes. This is the primary correction needed for silicon diode detectors. [trs-483]

## Connections

- [[cavity-theory]] — Spencer–Attix theory is the B–G extension from which s_{w,air} is derived; the cutoff Δ = 10 keV is standard
- [[reference-dosimetry-kq]] — s_{w,air} is the dominant physical component of the beam quality correction factor k_Q
- [[small-field-output-correction-factors]] — Despite LCPE loss, s_{w,air} stability confirms that k_{Q_clin,Q_msr} deviations are perturbation-dominated, not stopping-power-ratio-dominated
- [[lateral-charged-particle-equilibrium]] — LCPE loss changes the photon spectrum but has minimal effect on the electron stopping-power ratio; this is a subtle but important fact

## Open Questions

- What is the quantitative variation of s_{w,air} for FFF beams at very small field sizes (<5 mm), where the hardening effect may be slightly larger than for WFF beams?
- Are there published Spencer–Attix s_{w,air} tables specifically for the msr fields of CyberKnife and Gamma Knife?

## Raw Notes

- This stub should be expanded when a dedicated source on stopping-power ratio calculations (e.g., Andreo et al. or IAEA TECDOC-1455) is ingested.
- The 0.5% stability finding is critical: it justifies the use of TRS-398 k_Q values for small-field reference dosimetry without field-size-dependent stopping-power corrections.
