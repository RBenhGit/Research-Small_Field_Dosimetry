# SOURCE CAPTURE — Nahum, "Cavity Theory, Stopping-Power Ratios, Correction Factors"

> **Provenance (not part of the source):**
> - **Title:** Cavity Theory, Stopping-Power Ratios, Correction Factors (Chapter/Lecture 3)
> - **Author:** Alan E. Nahum, PhD — Physics Department, Clatterbridge Centre for Oncology, Wirral, UK
> - **Event:** AAPM Summer School, *Clinical Dosimetry for Radiotherapy*, 21–25 June 2009, Colorado College, Colorado Springs, USA
> - **Source URL:** https://www.aapm.org/meetings/09SS/documents/03Nahum-CavityTheorywithCorrections.pdf
> - **Format:** 63-slide PDF lecture deck
> - **Retrieved:** 2026-05-21 via web_fetch (text extraction; original is a binary PDF)
> - **Note:** Text below is an automated extraction from slides; reading order and equation rendering are imperfect. Treat the compiled wiki page `wiki/topics/cavity-theory.md` as the synthesized record.

---

## Extracted text (verbatim, slide order, lightly reflowed)

**Outline (3.1–3.9):** 3.1 Introduction · 3.2 "Large" photon detectors · 3.3 Bragg–Gray cavity theory · 3.4 Stopping-power ratios · 3.5 Thick-walled ion chambers · 3.6 Correction/perturbation factors for ion chambers · 3.7 General cavity theory · 3.8 Practical detectors · 3.9 Summary.

**Introduction.** Accurate knowledge of the (patient) dose in radiation therapy is crucial to clinical outcome (TCP & NTCP / therapeutic ratio vs dose). Detectors almost never measure dose-to-medium directly; therefore the interpretation of a detector reading requires dosimetry theory — "cavity theory" — especially when converting from a calibration at quality Q1 to a measurement at quality Q2. Also underlies the "physics" of depth–dose curves and dose computation in a TPS (TERMA, KERMA).

Two key fluence→dose results:
- Under charged-particle equilibrium (CPE), dose in medium relates to photon energy fluence Ψ via the mass energy-absorption coefficient: D_med = Ψ_med · (μ_en/ρ)_med (monoenergetic), integrated over spectrum otherwise.
- For charged particles (under δ-ray / electron equilibrium): D_med = Φ_med · (S_col/ρ)_med, the (unrestricted) mass collision stopping power; integrated over the electron spectrum otherwise.

**"Large"/photon detectors.** For a detector large enough to establish CPE in it, D_med/D_det = (μ_en/ρ)_med,det. Key assumption: photon energy fluence in the detector ≈ that in the undisturbed medium (Ψ_det = Ψ_med,z). The dependence of the (μ_en/ρ)-ratio on photon energy matters for water/medium.

**Bragg–Gray (B–G) cavity theory.** For a small cavity (sensitive volume small vs electron ranges) that does not disturb the electron fluence, D_med/D_det = (S_col/ρ)_med,det (stopping-power ratio), evaluated over the electron spectrum at the detector position (Eq. 45/48; denoted s_med,det^BG). The problem with δ-rays motivates Spencer–Attix.

**Spencer–Attix.** Extends B–G to account approximately for the finite ranges of delta-rays. A cutoff energy Δ defines a two-component model: electrons above Δ (primary or delta) are part of the fluence spectrum incident on the cavity; energy losses below Δ are local to the cavity (use restricted collision stopping power L_Δ); losses above Δ escape. Gives s_med,det as a ratio of integrals of (L_Δ/ρ) over the slowing-down spectrum plus a track-end term.

**When is a cavity "Bragg–Gray"?** Really one condition: the cavity must not disturb the charged-particle fluence (including its energy distribution) present in the medium in the absence of the cavity. In practice the cavity must be small compared to electron ranges; for photon beams only gas-filled cavities (ion chambers) qualify. Second (corollary) condition: dose in the cavity is deposited entirely by charged particles crossing it (photon interactions in the cavity negligible). A third condition is sometimes ERRONEOUSLY added — that CPE must exist; Greening (1981) said Gray's original theory required it, but CPE is NOT required. What IS required: the stopping-power ratio be evaluated over the electron spectrum in the medium at the detector position (today done with Monte Carlo).

Do air-filled ion chambers act as B–G cavities at kilovoltage x-ray qualities? For typical chamber dimensions at kV, the percentage of cavity-air dose due to photon interactions in the air is far from negligible (Ma C-M and Nahum AE 1991, Phys. Med. Biol. 36:413–428) — so B–G breaks down at kV. The megavoltage air-filled ion chamber is the clearest case of a B–G cavity.

**Stopping-power ratios.** (S_col/ρ) ratios water-to-medium vs electron energy for many media (adipose, bone, graphite, LiF, PMMA, silicon, photo-emulsion). Water/air mass collision stopping-power ratio: unrestricted vs restricted (Δ = 10 keV). Depth variation of the Spencer–Attix water/air stopping-power ratio s_w,air (Δ = 10 keV) from MC electron spectra (Andreo 1990; IAEA 1997b) over depth/energy.

**Thick-walled ion chambers.** D_med/D_air built from wall ratios: D_med/D_wall = (μ_en/ρ)_med,wall (CPE in wall) and D_wall/D_air = (L̄_Δ/ρ)_wall,air (B–G). Thick-walled cavity chamber free-in-air with known air volume (Primary Standards Labs): air kerma K_air from D_air via (μ_en/ρ), wall correction and (1−g).

**Correction / perturbation factors for ion chambers (in phantom).** Are real, practical ion chambers really B–G cavities? Full expression: D_med = M · (L̄_Δ/ρ)_air,med · Π P_i, with perturbation product P = P_repl (replacement: P_fl fluence + P_eff effective point of measurement) · P_wall · P_cel (central electrode) · P_stem. Farmer chamber geometry illustrated.

Wall effect — Almond–Svensson (1977) expression combining wall and medium (L̄_Δ/ρ) and (μ_en/ρ) weighted by α (fraction of cavity dose from wall-generated electrons).

Finite gas-cavity volume → fluence perturbation (electrons): effective point of measurement P_eff shifts upstream; P_fl. Johansson et al.: chambers of 3, 5, 7 mm radius show approximately linear relation between (1−P_fl) and cavity radius at a given energy. For the NE2571 cylindrical chamber, P_fl increases steadily from ≈ 0.955 at mean electron energy Ē_z = 2 MeV, to ≈ 0.980 at 10 MeV, to ≈ 0.997 at 20 MeV.

**General cavity theory (Burlin-type).** Two extremes: (i) detectors large vs electron ranges (CPE established, photon-only) → (μ_en/ρ) ratio; (ii) detectors small vs electron ranges (B–G) → stopping-power ratio. Many real cases fall between, with no exact theory; general/Burlin cavity theory gives an approximation: a weighted mean D_med/D_det = [ d·(L̄_Δ/ρ)_med,det + (1−d)·(μ_en/ρ)_med,det ], where d is the fraction of cavity dose from electrons generated in the medium (the B–G part) and (1−d) is the fraction from photon interactions in the cavity (the large-cavity/photon part). Example: Paul Mobit EGS4 of CaSO₄ TLD discs (0.9 mm thick) in photon beams.

**Summary of key points / practical detectors** — covered in closing slides.
