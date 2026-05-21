# Cavity Theory

**Type:** Topic
**Status:** developing
**Last updated:** 2026-05-21
**Sources:** [nahum-cavity-theory-2009], [trs-483], [tg-155]

## Summary

Cavity theory is the body of dosimetry theory that converts what a detector *reads* into absorbed **dose-to-medium**, since detectors almost never measure dose to the medium directly. It spans a spectrum defined by detector size relative to secondary-electron ranges: a **"large"/photon detector** (CPE established inside it) is governed by the **mass energy-absorption coefficient ratio** (μ_en/ρ)_med,det; a small, non-perturbing **Bragg–Gray cavity** (e.g. an air-filled ion chamber at MV) is governed by the **mass collision stopping-power ratio** (S/ρ)_med,det; and real chambers in between require **perturbation/correction factors** and, for intermediate sizes, **general (Burlin) cavity theory**. This is the theoretical foundation under reference-dosimetry protocols (TG-51, TRS-398) and the small-field output-correction factors of TRS-483. [nahum-cavity-theory-2009]

## Key Facts / Claims

- **Why it exists:** a detector reading must be interpreted via cavity theory, especially when converting a chamber's response from its calibration quality Q1 to a measurement quality Q2; the same physics underlies depth-dose curves and TPS dose computation. [nahum-cavity-theory-2009]
- **Two base fluence→dose relations:** under CPE, D_med = Ψ·(μ_en/ρ)_med (photon energy fluence × mass energy-absorption coefficient); under electron/δ-ray equilibrium, D_med = Φ·(S_col/ρ)_med (electron fluence × mass collision stopping power). [nahum-cavity-theory-2009]
- **Large/photon detector:** D_med/D_det = (μ_en/ρ)_med,det, assuming the photon energy fluence in the detector equals that in the undisturbed medium. [nahum-cavity-theory-2009]
- **Bragg–Gray cavity:** D_med/D_det = (S_col/ρ)_med,det, the stopping-power ratio evaluated over the electron spectrum *at the detector position*. [nahum-cavity-theory-2009]
- **The single B–G condition:** the cavity must not disturb the charged-particle fluence (including its energy distribution) present in the medium without the cavity → in practice the cavity must be small vs electron ranges; for photon beams only gas-filled cavities (ion chambers) qualify. Corollary: cavity dose is deposited entirely by crossing charged particles (negligible photon interaction in the cavity). [nahum-cavity-theory-2009]
- **Common misconception:** CPE is *not* a required B–G condition (Greening 1981 attributed it to Gray's original theory). What is required is that the stopping-power ratio be evaluated over the medium's electron spectrum at the detector — now done with Monte Carlo. [nahum-cavity-theory-2009]
- **Spencer–Attix** extends B–G to handle delta-rays via a cutoff energy Δ: a two-component model where electrons above Δ are part of the spectrum incident on the cavity, energy losses below Δ are deposited locally using the **restricted** stopping power L_Δ, and losses above Δ escape. The standard water/air value uses **Δ = 10 keV**. [nahum-cavity-theory-2009]
- **kV breakdown:** for typical chamber dimensions at kilovoltage x-ray qualities, the fraction of cavity-air dose from photon interactions in the air is far from negligible, so B–G fails (Ma & Nahum 1991, *Phys. Med. Biol.* 36:413–428). The MV air-filled ion chamber is the clearest B–G case. [nahum-cavity-theory-2009]
- **Thick-walled chamber chain:** D_med/D_air = (μ_en/ρ)_med,wall × (L̄_Δ/ρ)_wall,air; standards labs derive air kerma from free-in-air chambers of known volume with wall and (1−g) corrections. [nahum-cavity-theory-2009]
- **Ion-chamber perturbation product:** D_med = M·(L̄_Δ/ρ)_air,med·ΠP_i, with P = **P_repl** (replacement = fluence **P_fl** + effective point **P_eff**) × **P_wall** × **P_cel** (central electrode) × **P_stem**. The Almond–Svensson (1977) expression handles the wall via an α-weighted blend of stopping-power and (μ_en/ρ) ratios. [nahum-cavity-theory-2009]
- **P_fl is energy-dependent:** for the NE2571 cylindrical chamber, P_fl ≈ 0.955 at mean electron energy 2 MeV, ≈ 0.980 at 10 MeV, ≈ 0.997 at 20 MeV (Johansson et al.; (1−P_fl) ≈ linear in cavity radius at fixed energy). [nahum-cavity-theory-2009]
- **Spencer–Attix s_w,air stability in small fields:** Monte Carlo calculations confirm the water-to-air stopping-power ratio changes by ≤0.5% from the 10×10 cm² reference field down to 0.3×0.3 cm² for 6 MV — therefore deviations of k_{Q_clin,Q_msr} from unity are almost entirely due to perturbation factors, not stopping-power ratios. [trs-483]
- **General (Burlin) cavity theory** for intermediate detectors: D_med/D_det = d·(L̄_Δ/ρ)_med,det + (1−d)·(μ_en/ρ)_med,det, where d is the fraction of cavity dose from medium-generated electrons (B–G part) and (1−d) from photon interactions in the cavity (large-cavity part). [nahum-cavity-theory-2009]

## Connections

- [[stopping-power-ratios]] — the Spencer–Attix water/air ratio s_w,air and its depth/energy dependence is the quantitative core of B–G dosimetry; stable to <0.5% across small field sizes.
- [[ion-chamber-perturbation-factors]] *(to create)* — P_wall, P_cel, P_repl/P_fl, P_eff expand the correction product summarized here.
- [[reference-dosimetry-kq]] — TG-51 / TRS-398 beam-quality correction k_Q is the protocol-level embodiment of these stopping-power-ratio + perturbation arguments; extended to msr fields by TRS-483.
- [[small-field-output-correction-factors]] — TRS-483's k_{Qclin,Qmsr} is cavity theory pushed into the small-field regime, where B–G assumptions degrade (volume averaging, fluence perturbation).
- [[iaea-trs-483]] — applies cavity-theory formalism to practical small-field dosimetry procedures; tabulates k factors.
- [[lateral-charged-particle-equilibrium]] — LCPE loss is the physical condition that forces departure from standard B–G cavity theory in small fields.
- [[small-field-detectors]] — detector composition and density determine which cavity-theory limit (B–G, large-cavity, or Burlin intermediate) applies.

## Open Questions

- How do general-cavity-theory weighting factors (d) behave for modern small-field solid-state detectors (diodes, microdiamond) versus the TLD example given?
- Quantitatively, how do Spencer–Attix s_w,air values shift between broad-beam reference fields and sub-centimetre small fields? (TRS-483 states the water/air ratio is stable to ≤0.5% — worth a dedicated page.)
- Where exactly does the B–G approximation start to fail as field size shrinks, and how is that captured by TRS-483 perturbation/output-correction factors?
- For synthetic CVD diamond (microDiamond), general cavity theory intermediate behavior may apply — how do the Burlin d-weighting factors change with field size?

## Raw Notes

- Source: 63-slide AAPM 2009 Summer School lecture by Alan E. Nahum (Clatterbridge). Verbatim extraction stored at `raw/nahum-cavity-theory-2009.md`.
- This page is the theoretical backbone for the project's applied work. See also (external to this repo): the project knowledge source `Small-Field-Dosimetry-Knowledge-Source.md` in the *Research Small Fields Dosimetry* folder, which applies these ideas to linac calibration and TPS beam configuration (TRS-483 / TG-155).
- Equation rendering in the source extraction is imperfect (slide text); symbols here were reconstructed from standard cavity-theory notation and should be sanity-checked against a clean copy of the deck before being treated as authoritative.
