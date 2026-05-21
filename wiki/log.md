# Activity Log

Append-only chronological record of all wiki operations.

---

## 2026-05-20 — Initial setup

**Operation:** Repository initialized
**Sources processed:** (none — schema and seed page created manually)
**Pages created:** `llm-wiki-pattern`
**Pages updated:** `index.md`
**Notes:** Bootstrapped from Karpathy's LLM Wiki pattern (April 2026 gist)

---

## 2026-05-21 — Ingest: TRS-483 and TG-155

**Operation:** Ingest
**Sources processed:**
- `trs-483` — IAEA Technical Reports Series No. 483, *Dosimetry of Small Static Fields Used in External Beam Radiotherapy* (IAEA/AAPM, 2017). PDF read via pages 1–36.
- `tg-155` — Das IJ et al., *Report of AAPM Task Group 155: Megavoltage photon beam dosimetry in small fields and non-equilibrium conditions*, Medical Physics 2021;48:e886–e921. PDF read via pages 1–36.

**Pages created:**
- `iaea-trs-483` (Entity — mature)
- `aapm-tg-155` (Entity — mature)
- `small-field-definition` (Topic — developing)
- `lateral-charged-particle-equilibrium` (Topic — developing)
- `machine-specific-reference-field` (Topic — developing)
- `small-field-output-correction-factors` (Topic — developing; fills the forward-link stub from `cavity-theory`)
- `small-field-detectors` (Topic — developing)
- `reference-dosimetry-kq` (Topic — developing; fills the forward-link stub from `cavity-theory`)
- `stopping-power-ratios` (Topic — stub; fills the forward-link stub from `cavity-theory`)

**Pages updated:**
- `cavity-theory` — Sources extended to [trs-483][tg-155]; new fact on s_w,air stability in small fields; Connections upgraded from "*(to create)*" stubs to active links; three new back-links added (iaea-trs-483, lateral-charged-particle-equilibrium, small-field-detectors); new open question added.
- `index.md` — Added 9 new rows; total pages 2 → 11; last-updated date bumped.

**Notes:** Both sources are large PDFs (TRS-483 ≈ 215 pages; TG-155 ≈ 36 pages). Pages 1–36 of each were read, covering: full table of contents, introduction, physics of small field dosimetry, concepts and formalism (TRS-483) and sections on small-field definition, detectors, relative dose parameters, TPS modeling, uncertainty, and key recommendations (TG-155). Appendix II tabulated correction factor data from TRS-483 was noted by reference (not enumerated in detail — a future query or dedicated lookup is advised for specific k factor values). The `ion-chamber-perturbation-factors` forward link in cavity-theory remains unresolved; flagged for the next relevant source ingest.

---

## 2026-05-21 — Ingest: Artifact sources (linac process tree, small-field criteria, intermediate field method)

**Operation:** Ingest
**Sources processed:**
- `linac-small-field-dosimetry-process-tree` — Process tree document for output factor determination on conventional linacs (6 MV, 10 MV) per IAEA TRS-483; nine-phase workflow, detector selection by field size, WFF/FFF equivalence, uncertainty budget. (Claude artifact bec02402)
- `small-field-determination-criteria` — Technical document on quantitative criteria for small-field classification; FWHM method, r_LCPE ≈ 1.2 cm for 6 MV, patient safety incident data. (Claude artifact de458e9e)
- `intermediate-field-method` — Document on the daisy-chain calibration method; six implementation steps, strengths, limitations, TRS-483/TG-155 references. (Claude artifact 665a239b)
- *(Artifact 1e83af45 could not be fetched — WebFetch returned truncated empty content on all attempts; not processed)*

**Pages created:**
- `intermediate-field-method` (Topic — developing)
- `small-field-commissioning` (Topic — developing)

**Pages updated:**
- `small-field-definition` — Added: FWHM-exceeds-geometric detail (1–3 mm), 6 MV quantified threshold (2.4 cm × 2.4 cm, r_LCPE ≈ 1.2 cm), patient safety 15% discrepancy fact; new connection to [[small-field-commissioning]]
- `small-field-output-correction-factors` — Added: TRS-483 Table 24/27 specific identifiers, linear interpolation procedure, WFF/FFF equivalence; new connections to [[intermediate-field-method]] and [[small-field-commissioning]]
- `small-field-detectors` — Added: TRS-483 process-tree detector selection subsection (PTW 31010, IBA CC01, PTW 60019 by field size range), sub-0.5 cm extreme uncertainty note; new connections to [[intermediate-field-method]] and [[small-field-commissioning]]
- `index.md` — Added 2 new rows; total pages 11 → 13; last-updated date confirmed

---

## 2026-05-21 — Ingest: Nahum cavity theory

**Operation:** Ingest
**Sources processed:** `nahum-cavity-theory-2009` (AAPM 2009 Summer School deck, "Cavity Theory, Stopping-Power Ratios, Correction Factors"; fetched from aapm.org and saved to `raw/nahum-cavity-theory-2009.md`)
**Pages created:** `cavity-theory`
**Pages updated:** `index.md` (added row; total pages 1 → 2; last-updated date bumped)
**Notes:** Source is a slide deck; text extracted via web_fetch (original binary PDF could not be stored directly). Connections added as forward-links to not-yet-created pages (`stopping-power-ratios`, `ion-chamber-perturbation-factors`, `reference-dosimetry-kq`, `small-field-output-correction-factors`) — expect /lint to surface these as missing-page gaps, which is intended. Cross-doc pointer noted to the external project knowledge source (TRS-483/TG-155).
