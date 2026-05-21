# Small-Field Detectors

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-21
**Sources:** [tg-155], [trs-483], [linac-small-field-dosimetry-process-tree]

## Summary

Accurate small-field dosimetry demands detectors with small sensitive volumes, near-water-equivalent composition, and well-characterized field output correction factors (k_{Q_clin,Q_msr}). No single detector is universally optimal: ionization chambers are preferred for fields ≥1.5 cm × 1.5 cm; unshielded diodes, microDiamond, and plastic scintillators are preferred for ≤1 cm × 1 cm. The fundamental challenge is that as field size decreases, volume averaging, fluence perturbation, and energy/density effects all grow simultaneously, making correction factors large and uncertain for most conventional detectors. The TG-155 recommendation is to use at least two independent detector types for output factor measurements, cross-checked against MC-calculated correction factors.

## Key Facts / Claims

### Ionization Chambers
- **Preferred for:** fields ≥1.5 cm × 1.5 cm diameter or larger; reference dosimetry in msr fields. [tg-155]
- **Micro-ionization chambers** (e.g., PTW 31014 PinPoint, PTW 31016): small volumes allow use in fields down to ~1 cm × 1 cm with substantial correction factors. [tg-155]
- **High-Z central electrode problem:** Chambers with high-Z (e.g., steel) central electrodes introduce up to 3% perturbation in broad beams and larger in small fields; low-Z (aluminum) central electrodes do not exhibit this. [tg-155]
- **Signal-to-noise:** Small-volume chambers produce very small ionization currents; leakage can cause up to 16% error in absorbed dose if uncorrected; background should be subtracted. [tg-155]
- **Volume averaging:** The detector signal is the mean absorbed dose over its sensitive volume; correction required if beam profile gradient is significant over the detector dimension. [tg-155]
- **Liquid-filled ion chambers:** Near-water equivalence and <0.1 mm spatial resolution; ion recombination issues limit practical use; no longer commercially available. [tg-155]

### Silicon Diodes (Solid-State)
- **Preferred for:** field output factors and profiles in fields ≤1 cm × 1 cm (unshielded/stereotactic diodes). [tg-155]
- **Active volume:** Depletion region 20–80 μm; small dimension reduces volume averaging. [tg-155]
- **Unshielded vs. shielded:**
  - **Shielded diodes** (e.g., PTW 60016): tungsten-epoxy filter reduces low-energy photon response but introduces extra scatter and directional dependence in small fields — NOT recommended for small-field measurements. [tg-155]
  - **Unshielded stereotactic diodes** (e.g., IBA SFD, PTW 60017): preferred; yields similar results to shielded diodes in small fields but without scatter artifacts. [tg-155]
  - **microSilicon** (PTW 60023): 0.032 mm³ active volume, 1.5 mm diameter, epoxy density 1.15 g/cm³; very suitable for both linac and CyberKnife small fields. [tg-155]
- **Additional corrections needed:** dose-rate dependence, accumulated dose dependence (up to 10%), temperature dependence (~0.3%/°C), contact material effects, energy and angular dependence. [tg-155]
- **Over-response in large fields:** Unshielded diodes over-respond in large reference fields because of the large water-to-silicon mass energy-absorption coefficient ratio; this is why they must be normalized to a known field. [tg-155]

### Diamond Detectors
- **Natural diamond:** Nearly tissue equivalent (Z=6, similar to water Z=7.4); dose-rate dependent (up to 5%); large variability between specimens; expensive; correction factors close to unity for natural diamond in most field sizes. [tg-155]
- **Synthetic CVD microDiamond (PTW 60019):** Single crystal; commercially available; very small size; k_{Q_clin,Q_msr} close to unity for fields ≥1 cm × 1 cm; for very small fields (<1 cm), correction factors depend on linac model, energy, and collimation type. [tg-155]
- **microDiamond caution:** Das and Francescon (2018) noted that TRS-483 tabulated correction factors for microDiamond may differ from recent literature; at least one other suitable detector should be used alongside microDiamond. [tg-155]
- **CVD density issue:** Density of 3.5 g/cm³ is higher than water; mass density compensation (mass-density matching) has been proposed but adds complexity. [tg-155]

### Plastic Scintillators (PSD)
- **Key advantages:** Small size, tissue equivalence (density ≈ water), angular independence, stable photon energy response, no dose-rate dependence, near-unity k_{Q_clin,Q_msr} for most field sizes. [tg-155]
- **W1 (Exradin W1, Standard Imaging):** First commercially available PSD; requires correction for Cherenkov radiation in the optical fiber, especially when oriented vertically (perpendicular to beam). k_{Q_clin,Q_msr} ≈ 1.0 for most field sizes per TRS-483 but geometry-dependent Cherenkov correction needed. [tg-155]
- **W2 (Standard Imaging PSD-W2, 2019):** Improved Cherenkov rejection system; can be used in a scanning geometry; characteristics identical to W1 per Galavis et al. (2019). [tg-155]
- **Limitation:** Only one manufacturer (Standard Imaging, Middleton WI); irradiation geometry must use a solid phantom with a specific readout system; calibration procedure is non-trivial. [tg-155]
- **No correction required:** TG-155 states PSDs can be used without correction factors for most clinical small-field measurements, making them the most "correction-free" real-time detector option. [tg-155]

### Radiochromic Film
- **Key advantages:** 2D dose distribution in a single measurement; no volume averaging; spatial resolution limited by scanner (~0.1 mm); no energy dependence problem for MV beams. [tg-155]
- **Types:** GafChromic EBT2, EBT3 — most commonly used. Angular independence; linear dose response. [tg-155]
- **Uncertainty:** ±2–3% in small fields with careful handling; readout/calibration uncertainty dominant. [tg-155]
- **Cautions:** Temporal change in optical density post-irradiation; spatial nonuniformity of emulsion; strict protocol required (TG-55, TG-235). Do not irradiate film parallel to beam axis (Fontanarosa et al. 2009). [tg-155]
- **Uses:** Beam profile measurements, FWHM determination, field output factors in very small fields (<5 mm) where other detectors have large uncertainty. [tg-155]

### TLD / OSLD / RPG (Passive Point Detectors)
- **TLD (thermoluminescent dosimeter):** Energy-independent for MV photons; uncertainty ~3% individually, reducible to ~1% with careful individual sensitivity calibration. Usable for fields down to 0.6×0.6 cm with ~1% correction. [tg-155]
- **OSLD (optically stimulated luminescence dosimeter):** Similar response characteristics to TLD; re-readable (signal decreases ~0.05% per readout for RPG); angular dependence small. High density increases electron fluence perturbation in small fields. [tg-155]
- **Polymer gel / PRESAGE:** 3D dosimetry; ±3% isotropic uncertainty achievable; useful for small-field commissioning but requires specialized readout (MRI or optical-CT). [tg-155]

### Selection Summary (TG-155 §8.1)
- **Fields <1 cm × 1 cm:** Unshielded stereotactic diode, electron diode, plastic scintillator, single-crystal microDiamond.
- **Fields 1–1.5 cm × 1.5 cm:** Also micro-ionization chambers (excluding high-Z electrode types), with stem axis parallel to beam.
- **Fields >1.5 cm × 1.5 cm:** Very small ionization chambers (micro-ion chambers) are suitable.
- **Always:** Use at least two acceptable detector types; compare results; apply TRS-483 or literature k correction factors. [tg-155]

### Selection by Field Size — TRS-483 Process Tree (Conventional Linac)
- **≥ 3 cm:** PTW 31010 Semiflex, IBA CC01 (small ion chambers); standard measurement approach. [linac-small-field-dosimetry-process-tree]
- **1–3 cm:** Intermediate Field Method combining ion chambers with PTW 60019 microDiamond or unshielded diodes; see [[intermediate-field-method]]. [linac-small-field-dosimetry-process-tree]
- **< 1 cm:** PTW 60019 microDiamond preferred; plastic scintillator (W1/W2) as reference standard for comparison. [linac-small-field-dosimetry-process-tree]
- **< 0.5 cm:** Extreme uncertainty (±5–7%); multiple detectors mandatory; considered research-level dosimetry. [linac-small-field-dosimetry-process-tree]

## Connections

- [[small-field-output-correction-factors]] — k_{Q_clin,Q_msr} correction factors are specific to each detector type and are the central quantity linking detector choice to dosimetric accuracy
- [[small-field-definition]] — Detector size relative to field size is the third defining condition; the outer boundary of the sensitive volume must be ≥r_LCPE from the field edge
- [[iaea-trs-483]] — TRS-483 Chapter 4 provides detector characteristics and lists recommended detectors for msr and relative dosimetry
- [[aapm-tg-155]] — TG-155 Section 4 and Section 8.1 provide comprehensive updated guidance on detector selection
- [[cavity-theory]] — Detector response theory (Spencer–Attix B–G cavity theory, Burlin general cavity theory) underlies the interpretation of each detector type's reading
- [[lateral-charged-particle-equilibrium]] — r_LCPE determines the minimum acceptable detector-to-field-edge distance and thus the maximum detector size for a given field
- [[intermediate-field-method]] — For 1–3 cm fields, the daisy-chain cross-calibrates a small detector at the intermediate field before deployment in smaller fields
- [[small-field-commissioning]] — Phase 3 of the commissioning workflow is explicit detector selection by field size; the process tree maps specific detector models to field size ranges

## Open Questions

- Are there commercially available plastic scintillators being developed with even smaller sensing volumes than W1/W2 for sub-5 mm fields?
- Can inorganic scintillator detectors (e.g., Debnath et al. 2020 high-resolution detector) be clinically deployed with acceptable correction factors for ultra-small fields?

## Raw Notes

- TG-155 notes that measurement uncertainty for profiles is dominated by the dose gradient and detector sensitive volume; the total uncertainty increases near the penumbra and is typically largest at the field edge.
- The microSilicon (PTW 60023) was introduced after TRS-483 publication; its k factors are given in recent literature (Weber et al. 2020, Francescon et al. 2020) and should be preferred over older correction factor tables.
