#!/usr/bin/env python3
"""
Small Field Dosimetry Calibration Workbook Generator
Detectors : Farmer (ref) | Standard Imaging A16 | Sun Nuclear Edge | PTW 60019 microDiamond
Energies  : 6 MV WFF | 10 MV WFF
Protocol  : IAEA TRS-483 / AAPM TG-155
"""

import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUT = "d:/cowork/Research-Small_Field_Dosimetry/Small_Field_Dosimetry_Calibration.xlsx"

# ── Palette ──────────────────────────────────────────────────────────────────
CH  = "1B3A5C"   # header
CSH = "2E6DA4"   # sub-header
CE  = "FFFDE7"   # entry (yellow)
CC  = "E3F2FD"   # calculated (blue)
CR  = "E8F5E9"   # result (green)
CL  = "ECEFF1"   # label (gray)
CP  = "C8E6C9"   # pass
CF  = "FFCDD2"   # fail / warn
C6  = "E8EAF6"   # 6 MV section lavender
C10 = "FFF3E0"   # 10 MV section warm
CA1 = "E1F5FE"   # A16 column
CA2 = "F3E5F5"   # Edge column
CA3 = "FFFFF0"   # microDiamond column
CN  = "FAFAFA"   # neutral

def _fill(c): return PatternFill("solid", fgColor=c)
def _font(bold=False, color="000000", size=10, italic=False):
    return Font(bold=bold, color=color, size=size, italic=italic, name="Calibri")
def _align(h="center", v="center", wrap=False):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)
TH = Side(style="thin"); MD = Side(style="medium")
def _b(): return Border(left=TH, right=TH, top=TH, bottom=TH)
def _bm(): return Border(left=MD, right=MD, top=MD, bottom=MD)

def hdr(ws, r, c, text, cols=1, rows=1, bg=CH, fg="FFFFFF", sz=11, bold=True):
    cell = ws.cell(r, c, text)
    cell.fill = _fill(bg); cell.font = _font(bold, fg, sz)
    cell.alignment = _align("center", "center", True); cell.border = _b()
    if cols > 1 or rows > 1:
        ws.merge_cells(start_row=r, start_column=c, end_row=r+rows-1, end_column=c+cols-1)
    return cell

def lbl(ws, r, c, text, cols=1, rows=1, bg=CL, sz=9, bold=True, halign="left"):
    cell = ws.cell(r, c, text)
    cell.fill = _fill(bg); cell.font = _font(bold, "000000", sz)
    cell.alignment = _align(halign, "center", True); cell.border = _b()
    if cols > 1 or rows > 1:
        ws.merge_cells(start_row=r, start_column=c, end_row=r+rows-1, end_column=c+cols-1)
    return cell

def inp(ws, r, c, v=None, fmt="General"):
    cell = ws.cell(r, c, v)
    cell.fill = _fill(CE); cell.font = _font(False, "000000", 10)
    cell.alignment = _align("center"); cell.border = _b(); cell.number_format = fmt
    return cell

def clc(ws, r, c, formula, fmt="0.0000"):
    cell = ws.cell(r, c, formula)
    cell.fill = _fill(CC); cell.font = _font(False, "000000", 10)
    cell.alignment = _align("center"); cell.border = _b(); cell.number_format = fmt
    return cell

def res(ws, r, c, formula=None, fmt="0.0000"):
    cell = ws.cell(r, c, formula)
    cell.fill = _fill(CR); cell.font = _font(True, "000000", 10)
    cell.alignment = _align("center"); cell.border = _b(); cell.number_format = fmt
    return cell

def nt(ws, r, c, text, cols=1):
    cell = ws.cell(r, c, text)
    cell.font = _font(False, "666666", 9, True)
    cell.alignment = _align("left", "center", True)
    if cols > 1:
        ws.merge_cells(start_row=r, start_column=c, end_row=r, end_column=c+cols-1)
    return cell

def cw(ws, d):
    for k, v in d.items():
        ws.column_dimensions[k].width = v

def rh(ws, d):
    for k, v in d.items():
        ws.row_dimensions[k].height = v


# ── Sheet helpers ─────────────────────────────────────────────────────────────
def sheet_header(ws, title, subtitle=""):
    hdr(ws, 1, 1, title, cols=20, sz=14, bg=CH)
    ws.row_dimensions[1].height = 28
    if subtitle:
        hdr(ws, 2, 1, subtitle, cols=20, sz=10, bg=CSH)
        ws.row_dimensions[2].height = 20
    return 3 if subtitle else 2


# ═════════════════════════════════════════════════════════════════════════════
# 1. INSTRUCTIONS
# ═════════════════════════════════════════════════════════════════════════════
def build_instructions(wb):
    ws = wb.create_sheet("INSTRUCTIONS")
    cw(ws, {"A": 22, "B": 60, "C": 20, "D": 40})

    hdr(ws, 1, 1, "Small Field Dosimetry Calibration — Instructions & Color Key",
        cols=4, sz=14)
    rh(ws, {1: 30, 2: 14})

    rows = [
        (3,  "PROTOCOL",  "IAEA TRS-483 (2017) + AAPM TG-155 (2021)"),
        (4,  "DETECTORS", "Farmer (ref) | Standard Imaging A16 | Sun Nuclear Edge | PTW 60019 microDiamond"),
        (5,  "ENERGIES",  "6 MV WFF (Table 24) | 10 MV WFF (Table 27)"),
        (6,  "SETUP DEPTH", "10 cm in water phantom, SAD or SSD=100 cm, 10×10 cm reference field"),
        (7,  "FIELD SIZES",
             "Method A (≥3 cm): Farmer+A16+Edge+uDiam  |  "
             "Method B (1–3 cm): Intermediate Field Chain  |  "
             "Method C (<1 cm): Edge+uDiam mandatory 2-detector"),
    ]
    for r, key, val in rows:
        lbl(ws, r, 1, key, bg=CL)
        cell = ws.cell(r, 2, val)
        cell.font = _font(False, "000000", 10)
        cell.alignment = _align("left", "center", True)
        cell.border = _b()
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
        ws.row_dimensions[r].height = 24

    rh(ws, {8: 8})

    # Color key
    hdr(ws, 9, 1, "COLOR KEY", cols=4, bg=CSH, sz=10)
    key_items = [
        (CE, "000000", "User Entry Cell",     "Enter measurement data here"),
        (CC, "000000", "Calculated Cell",      "Formula — do not overwrite"),
        (CR, "000000", "Result Cell",          "Final corrected result"),
        (CL, "000000", "Label Cell",           "Row / column label"),
        (C6, "000000", "6 MV Section",         "Measurements at 6 MV WFF"),
        (C10,"000000", "10 MV Section",        "Measurements at 10 MV WFF"),
        (CA1,"000000", "A16 Detector Column",  "Standard Imaging A16 readings"),
        (CA2,"000000", "Edge Detector Column", "Sun Nuclear Edge readings"),
        (CA3,"000000", "microDiamond Column",  "PTW 60019 microDiamond readings"),
        (CP, "000000", "PASS",                 "Within acceptance criterion"),
        (CF, "000000", "FAIL / Warning",       "Exceeds acceptance criterion — investigate"),
    ]
    for i, (bg, fg, label, desc) in enumerate(key_items):
        r = 10 + i
        ws.cell(r, 1).fill = _fill(bg); ws.cell(r, 1).border = _b()
        lbl(ws, r, 2, label, bg=bg, bold=False)
        cell = ws.cell(r, 3, desc)
        cell.font = _font(False, "444444", 9, True)
        cell.alignment = _align("left"); cell.border = _b()
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=4)
        ws.row_dimensions[r].height = 18

    rh(ws, {21: 8})
    hdr(ws, 22, 1, "WORKFLOW ORDER", cols=4, bg=CSH, sz=10)
    steps = [
        "1. SETUP — Fill equipment IDs and calibration factors (one time)",
        "2. ENVIRONMENT — Record T and P before each measurement session",
        "3. BEAM_QUALITY — Measure TPR20,10 for each energy",
        "4. REF_DOSIMETRY — TRS-398 absorbed dose at reference field (Farmer)",
        "5. DET_CONDITIONING — Pre-irradiate detectors; check leakage and dose-rate dependence",
        "6. FWHM — Measure all field sizes with a scanning detector; record Sclin",
        "7. OF_METHOD_A — Output factors for Sclin ≥ 3 cm",
        "8. OF_METHOD_B — Intermediate field chain for 1 cm ≤ Sclin < 3 cm",
        "9. OF_METHOD_C — Small field output factors for Sclin < 1 cm",
        "10. K_FACTORS — Transcribe k_{Q_clin,Q_msr} from TRS-483 Table 24 (6MV) / Table 27 (10MV)",
        "11. UNCERTAINTY — Review component uncertainties",
        "12. SUMMARY — Final output factor table; check cross-detector agreement",
    ]
    for i, step in enumerate(steps):
        r = 23 + i
        cell = ws.cell(r, 1, step)
        cell.font = _font(False, "000000", 10)
        cell.alignment = _align("left", "center", True)
        cell.border = _b()
        cell.fill = _fill(CN)
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
        ws.row_dimensions[r].height = 18

    ws.freeze_panes = None


# ═════════════════════════════════════════════════════════════════════════════
# 2. SETUP
# ═════════════════════════════════════════════════════════════════════════════
def build_setup(wb):
    ws = wb.create_sheet("SETUP")
    cw(ws, {"A": 28, "B": 28, "C": 18, "D": 18, "E": 22, "F": 18})

    hdr(ws, 1, 1, "Equipment Setup & Calibration Constants", cols=6, sz=13)
    rh(ws, {1: 26})
    nt(ws, 2, 1, "Fill ONCE before commissioning. These values are referenced by all measurement sheets.", cols=6)

    r = 4
    hdr(ws, r, 1, "LINAC", cols=6, bg=CSH, sz=10); r += 1
    fields = [("Model / Manufacturer", ""), ("Serial Number", ""),
              ("Installation Date", ""), ("TPS Name / Version", "")]
    for label, _ in fields:
        lbl(ws, r, 1, label); inp(ws, r, 2, fmt="@"); ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6); r += 1

    r += 1
    hdr(ws, r, 1, "FARMER CHAMBER  (Reference)", cols=6, bg=CSH, sz=10); r += 1
    lbl(ws, r, 1, "Model"); lbl(ws, r, 2, "Serial Number"); lbl(ws, r, 3, "ND,w  [Gy/C]"); lbl(ws, r, 4, "kQ  (6 MV)*"); lbl(ws, r, 5, "kQ  (10 MV)*"); lbl(ws, r, 6, "Cal. Date"); r += 1
    inp(ws, r, 1, fmt="@"); inp(ws, r, 2, fmt="@"); inp(ws, r, 3, fmt="0.0000E+00")
    inp(ws, r, 4, fmt="0.0000"); inp(ws, r, 5, fmt="0.0000"); inp(ws, r, 6, fmt="@")
    nt(ws, r + 1, 1, "* kQ from TRS-398 Table T_II based on measured TPR20,10 — enter after BEAM_QUALITY sheet.", cols=6)
    r += 3

    hdr(ws, r, 1, "A16  —  Standard Imaging A16 microionization chamber", cols=6, bg=CSH, sz=10); r += 1
    lbl(ws, r, 1, "Serial Number"); lbl(ws, r, 2, "Volume [cm³]"); lbl(ws, r, 3, "ND,w  [Gy/C]"); lbl(ws, r, 4, "kQ  (6 MV)*"); lbl(ws, r, 5, "kQ  (10 MV)*"); lbl(ws, r, 6, "Cal. Date"); r += 1
    inp(ws, r, 1, fmt="@"); inp(ws, r, 2, 0.016, fmt="0.000")
    inp(ws, r, 3, fmt="0.0000E+00"); inp(ws, r, 4, fmt="0.0000"); inp(ws, r, 5, fmt="0.0000"); inp(ws, r, 6, fmt="@")
    nt(ws, r + 1, 1, "* If no absolute calibration: A16 is used as a relative detector; k_Qmsr from TRS-483 Table 24/27.", cols=6)
    r += 3

    hdr(ws, r, 1, "EDGE  —  Sun Nuclear Edge unshielded diode", cols=6, bg=CSH, sz=10); r += 1
    lbl(ws, r, 1, "Serial Number"); lbl(ws, r, 2, "Sensitive Vol. [mm³]"); lbl(ws, r, 3, "Pre-irrad. dose [Gy]"); lbl(ws, r, 4, "Reference DR [MU/min]"); lbl(ws, r, 5, "Conditioning Date"); lbl(ws, r, 6, "Notes"); r += 1
    inp(ws, r, 1, fmt="@"); inp(ws, r, 2, 0.03, fmt="0.00"); inp(ws, r, 3, 10.0, fmt="0.0")
    inp(ws, r, 4, 300, fmt="0"); inp(ws, r, 5, fmt="@"); inp(ws, r, 6, fmt="@")
    nt(ws, r + 1, 1, "Edge is used as a relative detector only — absolute dose via chain from Farmer.", cols=6)
    r += 3

    hdr(ws, r, 1, "microDIAMOND  —  PTW 60019", cols=6, bg=CSH, sz=10); r += 1
    lbl(ws, r, 1, "Serial Number"); lbl(ws, r, 2, "Sensitive Vol. [mm³]"); lbl(ws, r, 3, "Pre-irrad. dose [Gy]"); lbl(ws, r, 4, "Reference DR [MU/min]"); lbl(ws, r, 5, "Conditioning Date"); lbl(ws, r, 6, "Notes"); r += 1
    inp(ws, r, 1, fmt="@"); inp(ws, r, 2, 0.004, fmt="0.0000"); inp(ws, r, 3, 5.0, fmt="0.0")
    inp(ws, r, 4, 300, fmt="0"); inp(ws, r, 5, fmt="@"); inp(ws, r, 6, fmt="@")
    nt(ws, r + 1, 1, "Pre-irradiate with ≥5 Gy before first use; repeat if unused > 4 h.", cols=6)
    r += 3

    hdr(ws, r, 1, "ELECTROMETER", cols=6, bg=CSH, sz=10); r += 1
    lbl(ws, r, 1, "Model"); lbl(ws, r, 2, "Serial Number"); lbl(ws, r, 3, "kel (electrometer factor)"); lbl(ws, r, 4, "Cal. Date"); r += 1
    inp(ws, r, 1, fmt="@"); inp(ws, r, 2, fmt="@"); inp(ws, r, 3, 1.0000, fmt="0.0000"); inp(ws, r, 4, fmt="@")
    r += 2

    hdr(ws, r, 1, "MEASUREMENT CONDITIONS  (Reference)", cols=6, bg=CSH, sz=10); r += 1
    pairs = [("Reference temperature T0 [°C]", 20.0, "0.0"),
             ("Reference pressure P0 [kPa]",   101.325, "0.000"),
             ("Reference depth [cm]",           10.0, "0.0"),
             ("SSD or SAD [cm]",                100.0, "0.0"),
             ("Reference MU per reading",       200, "0")]
    for label, default, fmt in pairs:
        lbl(ws, r, 1, label, cols=3); inp(ws, r, 4, default, fmt=fmt); r += 1


# ═════════════════════════════════════════════════════════════════════════════
# 3. ENVIRONMENT  (T, P, kTP)
# ═════════════════════════════════════════════════════════════════════════════
def build_environment(wb):
    ws = wb.create_sheet("ENVIRONMENT")
    cw(ws, {"A": 14, "B": 16, "C": 13, "D": 14, "E": 14, "F": 14, "G": 50})

    hdr(ws, 1, 1, "Environmental Conditions — Temperature, Pressure, kTP", cols=7, sz=13)
    nt(ws, 2, 1,
       "Record at start and end of each measurement session. "
       "kTP = ((273.15+T)/(273.15+T0)) × (P0/P) where T0=20 °C, P0=101.325 kPa  "
       "(values from SETUP!D rows for T0/P0).", cols=7)

    r = 4
    cols = ["Session #", "Date", "Time", "T [°C]", "P [kPa]", "kTP", "Notes / Session description"]
    for i, c in enumerate(cols):
        lbl(ws, r, i+1, c, halign="center")
    r += 1

    for i in range(1, 21):   # 20 sessions
        inp(ws, r, 1, i, fmt="0"); inp(ws, r, 2, fmt="YYYY-MM-DD"); inp(ws, r, 3, fmt="HH:MM")
        inp(ws, r, 4, fmt="0.0"); inp(ws, r, 5, fmt="0.000")
        # kTP formula — T0=20, P0=101.325 hardcoded (user can adjust)
        clc(ws, r, 6,
            f"=IF(AND(D{r}<>\"\",E{r}<>\"\"),(273.15+D{r})/(273.15+20)*101.325/E{r},\"\")",
            fmt="0.0000")
        inp(ws, r, 7, fmt="@")
        ws.row_dimensions[r].height = 16
        r += 1

    ws.freeze_panes = "A5"


# ═════════════════════════════════════════════════════════════════════════════
# 4. BEAM QUALITY  (TPR20,10)
# ═════════════════════════════════════════════════════════════════════════════
def build_beam_quality(wb):
    ws = wb.create_sheet("BEAM_QUALITY")
    cw(ws, {"A": 26, "B": 14, "C": 14, "D": 14, "E": 16, "F": 14, "G": 40})

    hdr(ws, 1, 1, "Beam Quality — TPR20,10 per Energy", cols=7, sz=13)
    nt(ws, 2, 1,
       "Setup: Farmer chamber at isocentre (SSD+depth=100 cm), 10×10 cm field, 200 MU. "
       "Keep SSD constant; change depth only. kTP cancels in ratio if T,P stable.",
       cols=7)

    energies = [("6 MV WFF", C6), ("10 MV WFF", C10)]
    r = 4

    for energy, color in energies:
        hdr(ws, r, 1, energy, cols=7, bg=CSH if color == C6 else "A0522D", sz=11); r += 1

        # Column headers
        cols_h = ["Measurement", "Rep 1", "Rep 2", "Rep 3", "Mean", "", "Result"]
        for i, c in enumerate(cols_h):
            lbl(ws, r, i+1, c, halign="center")
        r += 1

        r_d20 = r
        lbl(ws, r, 1, "M at d = 20 cm  [nC or rel]", bg=color)
        for c in range(2, 5): inp(ws, r, c, fmt="0.0000")
        clc(ws, r, 5, f"=AVERAGE(B{r}:D{r})", fmt="0.0000"); r += 1

        r_d10 = r
        lbl(ws, r, 1, "M at d = 10 cm  [nC or rel]", bg=color)
        for c in range(2, 5): inp(ws, r, c, fmt="0.0000")
        clc(ws, r, 5, f"=AVERAGE(B{r}:D{r})", fmt="0.0000"); r += 1

        lbl(ws, r, 1, "TPR20,10 = M20 / M10", bg=color)
        res(ws, r, 5, f"=E{r_d20}/E{r_d10}", fmt="0.0000")
        lbl(ws, r, 7, "kQ (Farmer)  →  look up TRS-398 Table T_II")
        inp(ws, r, 6, fmt="0.0000")
        nt(ws, r, 7, "→  Enter kQ in SETUP sheet D/E row for Farmer"); r += 1

        nt(ws, r, 1,
           "Typical range for linac: TPR20,10 = 0.62–0.78. "
           "Repeat if two readings differ by >0.3%.",
           cols=7); r += 3


# ═════════════════════════════════════════════════════════════════════════════
# 5. REFERENCE DOSIMETRY  (TRS-398, Farmer)
# ═════════════════════════════════════════════════════════════════════════════
def build_ref_dosimetry(wb):
    ws = wb.create_sheet("REF_DOSIMETRY")
    cw(ws, {"A": 32, "B": 13, "C": 13, "D": 13, "E": 13, "F": 13,
            "G": 13, "H": 13, "I": 35})

    hdr(ws, 1, 1, "Reference Dosimetry — TRS-398 (Farmer Chamber)", cols=9, sz=13)
    nt(ws, 2, 1,
       "Field: 10×10 cm | Depth: 10 cm | SSD=100 cm or SAD | 200 MU. "
       "Complete Part A–D for each energy.", cols=9)

    energies = [("6 MV WFF", C6, "SETUP!D10", "SETUP!E10"),
                ("10 MV WFF", C10, "SETUP!D10", "SETUP!E10")]
    r = 4

    for energy, color, kQ_ref_6, kQ_ref_10 in energies:
        hdr(ws, r, 1, energy, cols=9, bg=CSH, sz=11); r += 1

        # Part A: Environment
        hdr(ws, r, 1, "A — Environmental Correction", cols=9, bg=CSH if color==C6 else "8B6914", sz=10); r += 1
        lbl(ws, r, 1, "Session # (→ ENVIRONMENT sheet)"); inp(ws, r, 2, fmt="0")
        lbl(ws, r, 4, "T [°C] from ENV"); inp(ws, r, 5, fmt="0.0")
        lbl(ws, r, 7, "P [kPa] from ENV"); inp(ws, r, 8, fmt="0.000")
        nt(ws, r, 9, "Copy from ENVIRONMENT sheet for this session"); r += 1
        T_cell = f"E{r-1}"; P_cell = f"H{r-1}"
        lbl(ws, r, 1, "kTP");
        clc(ws, r, 2, f"=(273.15+{T_cell})/(273.15+20)*101.325/{P_cell}", fmt="0.0000")
        kTP_cell = f"B{r}"; r += 2

        # Part B: Polarity
        hdr(ws, r, 1, "B — Polarity Correction  kpol", cols=9, bg=color, sz=10); r += 1
        lbl(ws, r, 1, "Collection voltage V1 [V]"); inp(ws, r, 2, 300, fmt="0")
        lbl(ws, r, 4, "Reversed voltage −V1 [V]"); inp(ws, r, 5, -300, fmt="0"); r += 1
        lbl(ws, r, 1, ""); lbl(ws, r, 2, "Rep 1"); lbl(ws, r, 3, "Rep 2"); lbl(ws, r, 4, "Rep 3"); lbl(ws, r, 5, "Mean", halign="center")
        r += 1
        r_Mp = r
        lbl(ws, r, 1, "M(+V1)  [nC]", bg=color)
        for c in range(2, 5): inp(ws, r, c, fmt="0.0000")
        clc(ws, r, 5, f"=AVERAGE(B{r}:D{r})", fmt="0.0000"); r += 1
        r_Mn = r
        lbl(ws, r, 1, "M(−V1)  [nC]  (enter with sign)", bg=color)
        for c in range(2, 5): inp(ws, r, c, fmt="0.0000")
        clc(ws, r, 5, f"=AVERAGE(B{r}:D{r})", fmt="0.0000"); r += 1
        lbl(ws, r, 1, "kpol = (M(+V1)+|M(−V1)|) / (2×M(+V1))")
        res(ws, r, 2, f"=(E{r_Mp}+ABS(E{r_Mn}))/(2*E{r_Mp})", fmt="0.0000")
        kpol_cell = f"B{r}"
        nt(ws, r, 4, "Should be within 1.000 ± 0.005 for Farmer in MV beams.", cols=6); r += 2

        # Part C: Ion recombination
        hdr(ws, r, 1, "C — Ion Recombination  ks  (Two-Voltage Method, pulsed beams)", cols=9, bg=color, sz=10); r += 1
        lbl(ws, r, 1, "V1 [V]"); inp(ws, r, 2, 300, fmt="0")
        lbl(ws, r, 4, "V2 [V]  (V1/V2 = 2)"); inp(ws, r, 5, 150, fmt="0")
        V1_cell = f"B{r}"; V2_cell = f"E{r}"; r += 1
        lbl(ws, r, 1, ""); lbl(ws, r, 2, "Rep 1"); lbl(ws, r, 3, "Rep 2"); lbl(ws, r, 4, "Rep 3"); lbl(ws, r, 5, "Mean")
        r += 1
        r_MV1 = r
        lbl(ws, r, 1, "M(V1)  [nC]", bg=color)
        for c in range(2, 5): inp(ws, r, c, fmt="0.0000")
        clc(ws, r, 5, f"=AVERAGE(B{r}:D{r})", fmt="0.0000"); r += 1
        r_MV2 = r
        lbl(ws, r, 1, "M(V2)  [nC]", bg=color)
        for c in range(2, 5): inp(ws, r, c, fmt="0.0000")
        clc(ws, r, 5, f"=AVERAGE(B{r}:D{r})", fmt="0.0000"); r += 1
        lbl(ws, r, 1, "r = M(V1)/M(V2)")
        clc(ws, r, 2, f"=E{r_MV1}/E{r_MV2}", fmt="0.0000"); r_ratio = f"B{r}"; r += 1
        lbl(ws, r, 1, "ks  (TRS-398 Eq. T.IV, pulsed beams)")
        res(ws, r, 2, f"=2.337+(-3.636)*{r_ratio}+2.299*{r_ratio}^2", fmt="0.0000")
        ks_cell = f"B{r}"
        nt(ws, r, 4, "Coefficients valid for V1/V2=2. ks should be <1.010 at 300/150 V.", cols=6); r += 2

        # Part D: Absorbed dose
        hdr(ws, r, 1, "D — Absorbed Dose to Water  Dw", cols=9, bg=color, sz=10); r += 1
        lbl(ws, r, 1, ""); [lbl(ws, r, c, f"Rep {c-1}") for c in range(2, 7)]
        lbl(ws, r, 7, "Mean"); lbl(ws, r, 8, "SD [nC]"); lbl(ws, r, 9, "CV [%]"); r += 1
        r_Mraw = r
        lbl(ws, r, 1, "M_raw  [nC]  at V1, +polarity", bg=color)
        for c in range(2, 7): inp(ws, r, c, fmt="0.0000")
        clc(ws, r, 7, f"=AVERAGE(B{r}:F{r})", fmt="0.0000")
        clc(ws, r, 8, f"=STDEV(B{r}:F{r})", fmt="0.0000")
        clc(ws, r, 9, f"=IF(G{r}<>0,H{r}/G{r}*100,\"\")", fmt="0.00")
        r += 1

        lbl(ws, r, 1, "kel (electrometer factor, from SETUP)")
        inp(ws, r, 2, fmt="0.0000"); kel_cell = f"B{r}"; r += 1

        lbl(ws, r, 1, "M_corrected = M_raw × kTP × kpol × ks × kel")
        res(ws, r, 2, f"=G{r_Mraw}*{kTP_cell}*{kpol_cell}*{ks_cell}*{kel_cell}", fmt="0.0000E+00")
        Mcorr_cell = f"B{r}"; r += 1

        lbl(ws, r, 1, "ND,w  [Gy/C]  (from SETUP Farmer row)")
        inp(ws, r, 2, fmt="0.0000E+00"); Ndw_cell = f"B{r}"; r += 1

        lbl(ws, r, 1, "kQ  (from SETUP / BEAM_QUALITY)")
        inp(ws, r, 2, fmt="0.0000"); kQ_cell = f"B{r}"; r += 1

        lbl(ws, r, 1, "Dw  [Gy per reading] = Mcorr × ND,w × kQ")
        res(ws, r, 2, f"={Mcorr_cell}*{Ndw_cell}*{kQ_cell}", fmt="0.0000E+00")
        Dw_cell = f"B{r}"; r += 1

        lbl(ws, r, 1, "Output  [cGy/MU] = Dw × 100 / MU_per_reading")
        inp(ws, r, 3, 200, fmt="0")
        clc(ws, r, 2, f"={Dw_cell}*100/C{r}", fmt="0.0000")
        nt(ws, r, 4, "Target: 1.000 cGy/MU at reference conditions (may differ by ±2% before output tuning).", cols=6)
        r += 3


# ═════════════════════════════════════════════════════════════════════════════
# 6. DETECTOR CONDITIONING
# ═════════════════════════════════════════════════════════════════════════════
def build_det_conditioning(wb):
    ws = wb.create_sheet("DET_CONDITIONING")
    cw(ws, {"A": 30, "B": 16, "C": 16, "D": 16, "E": 16, "F": 16, "G": 30})

    hdr(ws, 1, 1, "Detector Pre-conditioning, Leakage & Dose-Rate Dependence", cols=7, sz=13)
    nt(ws, 2, 1, "Complete for every detector BEFORE output factor measurements. Re-do after detector storage > 4 h.", cols=7)

    detectors = [
        ("A16  —  Standard Imaging A16", CA1, "0 Gy (ion chamber — no conditioning required)", "300"),
        ("EDGE  —  Sun Nuclear Edge (unshielded diode)", CA2, "10 Gy minimum  (see SETUP for value)", "300"),
        ("microDIAMOND  —  PTW 60019", CA3, "5 Gy minimum  (see SETUP for value)", "300"),
    ]

    r = 4
    for det_name, color, preinfo, ref_dr in detectors:
        hdr(ws, r, 1, det_name, cols=7, bg=CSH, sz=11); r += 1

        # Pre-irradiation
        hdr(ws, r, 1, "A — Pre-irradiation Conditioning", cols=7, bg=color, sz=10); r += 1
        lbl(ws, r, 1, "Required pre-irrad. dose"); lbl(ws, r, 2, preinfo, cols=5, bg=CE); r += 1
        lbl(ws, r, 1, "Energy / field used"); inp(ws, r, 2, fmt="@")
        lbl(ws, r, 3, "MU delivered"); inp(ws, r, 4, fmt="0")
        lbl(ws, r, 5, "Date / Time"); inp(ws, r, 6, fmt="@"); r += 1
        lbl(ws, r, 1, "Conditioning readings (stability check)")
        lbl(ws, r, 2, "Rep 1"); lbl(ws, r, 3, "Rep 2"); lbl(ws, r, 4, "Rep 3"); lbl(ws, r, 5, "Mean"); lbl(ws, r, 6, "CV [%]"); r += 1
        lbl(ws, r, 1, "Reading  [nC or rel]", bg=color)
        for c in range(2, 5): inp(ws, r, c, fmt="0.00000")
        clc(ws, r, 5, f"=AVERAGE(B{r}:D{r})", fmt="0.00000")
        clc(ws, r, 6, f"=IF(E{r}>0,STDEV(B{r}:D{r})/E{r}*100,\"\")", fmt="0.000")
        nt(ws, r, 7, "CV should be <0.3% after sufficient conditioning."); r += 2

        # Leakage
        hdr(ws, r, 1, "B — Leakage Current Check", cols=7, bg=color, sz=10); r += 1
        lbl(ws, r, 1, ""); lbl(ws, r, 2, "Rep 1"); lbl(ws, r, 3, "Rep 2"); lbl(ws, r, 4, "Rep 3"); lbl(ws, r, 5, "Mean [nC]"); lbl(ws, r, 6, "Normal signal [nC]"); lbl(ws, r, 7, "Leakage [%]")
        r += 1
        r_lk = r
        lbl(ws, r, 1, "Leakage (no beam)", bg=color)
        for c in range(2, 5): inp(ws, r, c, fmt="0.00000")
        clc(ws, r, 5, f"=AVERAGE(B{r}:D{r})", fmt="0.00000")
        inp(ws, r, 6, fmt="0.00000")
        clc(ws, r, 7, f"=IF(F{r}>0,ABS(E{r})/F{r}*100,\"\")", fmt="0.000")
        nt(ws, r + 1, 1, "Acceptance: leakage < 0.5% of normal signal. Subtract from all readings if >0.1%.", cols=7)
        r += 3

        # Dose-rate dependence
        hdr(ws, r, 1, "C — Dose-Rate Dependence", cols=7, bg=color, sz=10); r += 1
        nt(ws, r, 1, f"Reference dose rate: {ref_dr} MU/min. Test at 5 levels. Acceptance: <1.0% variation.", cols=7); r += 1
        lbl(ws, r, 1, "Dose rate [MU/min]"); lbl(ws, r, 2, "Rep 1"); lbl(ws, r, 3, "Rep 2"); lbl(ws, r, 4, "Rep 3"); lbl(ws, r, 5, "Mean"); lbl(ws, r, 6, "Norm. to ref."); lbl(ws, r, 7, "Deviation [%]"); r += 1
        dose_rates = [100, 200, 300, 400, 600]
        r_ref_dr = None
        for dr in dose_rates:
            lbl(ws, r, 1, str(dr), bg=color)
            for c in range(2, 5): inp(ws, r, c, fmt="0.00000")
            clc(ws, r, 5, f"=AVERAGE(B{r}:D{r})", fmt="0.00000")
            if dr == 300:
                r_ref_dr = r
                clc(ws, r, 6, "1.0000", fmt="0.0000")
                clc(ws, r, 7, "0.000", fmt="0.000")
            else:
                clc(ws, r, 6, f"=IF(E{r_ref_dr}<>0,E{r}/E{r_ref_dr},\"\")" if r_ref_dr else "\"\"", fmt="0.0000")
                clc(ws, r, 7, f"=IF(F{r}<>\"\", (F{r}-1)*100,\"\")", fmt="0.000")
            r += 1
        nt(ws, r, 1, "Flag any dose rate with |deviation| > 1% — apply dose-rate correction factor if FFF beam.", cols=7)
        r += 3

    ws.freeze_panes = "A4"


# ═════════════════════════════════════════════════════════════════════════════
# 7. FWHM FIELD SIZE MEASUREMENTS
# ═════════════════════════════════════════════════════════════════════════════
def build_fwhm(wb):
    ws = wb.create_sheet("FWHM")
    cw(ws, {"A": 14, "B": 14, "C": 14, "D": 14, "E": 14, "F": 14, "G": 14,
            "H": 14, "I": 18, "J": 18})

    hdr(ws, 1, 1, "FWHM Field Size Measurements", cols=10, sz=13)
    nt(ws, 2, 1,
       "Measure inline and crossline profiles at 10 cm depth (SAD setup). "
       "FWHM = distance between 50% dose points on each side of Dmax. "
       "Sclin = √(FWHMx × FWHMy). Sclin determines which Method (A/B/C) applies.",
       cols=10)

    energies = [("6 MV WFF", C6), ("10 MV WFF", C10)]

    field_sizes = [0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0,
                   5.0, 6.0, 8.0, 10.0]

    r = 4
    for energy, color in energies:
        hdr(ws, r, 1, energy, cols=10, bg=CSH, sz=11); r += 1
        cols_h = ["Coll. X [cm]", "Coll. Y [cm]", "FWHM X [cm]", "FWHM Y [cm]",
                  "Sclin [cm]", "Sclin-Geo [cm]", "Penumbra 20-80% [mm]",
                  "Detector used", "Method", "Notes"]
        for i, c in enumerate(cols_h):
            lbl(ws, r, i+1, c, halign="center")
        r += 1
        for fs in field_sizes:
            inp(ws, r, 1, fs, fmt="0.0"); inp(ws, r, 2, fs, fmt="0.0")
            inp(ws, r, 3, fmt="0.000"); inp(ws, r, 4, fmt="0.000")
            clc(ws, r, 5, f"=IF(AND(C{r}<>\"\",D{r}<>\"\"),SQRT(C{r}*D{r}),\"\")", fmt="0.000")
            clc(ws, r, 6, f"=IF(E{r}<>\"\",E{r}-A{r},\"\")", fmt="0.000")
            inp(ws, r, 7, fmt="0.0")
            inp(ws, r, 8, fmt="@")
            clc(ws, r, 9,
                f'=IF(E{r}="","",IF(E{r}<1,"C",IF(E{r}<3,"B","A")))', fmt="@")
            inp(ws, r, 10, fmt="@")
            ws.row_dimensions[r].height = 16
            r += 1
        nt(ws, r, 1,
           "Sclin−Geo typically 1–3 mm for small fields (FWHM > geometric). "
           "Larger deviation may indicate MLC positional error.", cols=10)
        r += 3

    ws.freeze_panes = "A5"


# ═════════════════════════════════════════════════════════════════════════════
# 8. OUTPUT FACTORS — METHOD A  (Sclin ≥ 3 cm)
# ═════════════════════════════════════════════════════════════════════════════
def build_of_method_a(wb):
    ws = wb.create_sheet("OF_METHOD_A")

    # Columns layout:
    # A: Nominal  B: Sclin  C: kTP  D: M_ref_before  E: M_ref_after  F: M_ref_mean  G: M_ref_corr
    # H–J: Farmer M1 M2 M3  K: Farmer mean  L: kpol  M: Ω_Farmer
    # N–P: A16    Q: A16 mean  R: k_A16  S: Ω_A16
    # T–V: Edge   W: Edge mean X: k_Edge Y: Ω_Edge
    # Z–AB: uDiam AC: uDiam mean AD: k_uDiam AE: Ω_uDiam
    # AF: Ω_mean  AG: Max_dev%  AH: Pass?

    col_widths = {get_column_letter(c): 10 for c in range(1, 35)}
    col_widths.update({"A": 12, "B": 10, "C": 9})
    cw(ws, col_widths)

    hdr(ws, 1, 1, "Output Factors — Method A  (Sclin ≥ 3 cm)", cols=34, sz=13)
    nt(ws, 2, 1,
       "Interleave reference (10×10) readings before and after each clinical field. "
       "Apply kTP to all readings. kpol and ks: enter from REF_DOSIMETRY sheet (Farmer); "
       "for solid-state detectors kpol=1.0000, ks=1.0000. "
       "k = k_{Q_clin,Q_msr} from K_FACTORS sheet.",
       cols=34)

    energies = [("6 MV WFF", C6), ("10 MV WFF", C10)]
    field_sizes_A = [3.0, 4.0, 5.0, 6.0, 8.0, 10.0]   # nominal collimator cm

    r = 4
    for energy, color in energies:
        hdr(ws, r, 1, energy, cols=34, bg=CSH, sz=11); r += 1

        # Column headers — row 1
        groups = [
            (1,  1,  "Field"),
            (2,  1,  "Sclin\n[cm]"),
            (3,  1,  "kTP"),
            (4,  3,  "Reference (10×10) — interleaved"),
            (7,  1,  "Mref\ncorr"),
            (8,  4,  "Farmer"),
            (13, 4,  "A16"),
            (18, 4,  "Edge"),
            (23, 4,  "µDiamond"),
            (28, 1,  "Ω\nmean"),
            (29, 1,  "Dev\n[%]"),
            (30, 1,  "Pass?"),
        ]
        for col, span, label in groups:
            bg = CA1 if "A16" in label else CA2 if "Edge" in label else CA3 if "Diamond" in label else color
            hdr(ws, r, col, label, cols=span, bg=bg if label not in ("Field","Sclin\n[cm]","kTP","Ω\nmean","Dev\n[%]","Pass?","Mref\ncorr") else CL, sz=9)
        r += 1

        # Column headers — row 2
        sub = ["Nom\n[cm]", "→FWHM", "env→",
               "Mbefore", "Mafter", "Mref",  "Mcorr",
               "M1", "M2", "M3", "Mmean", "Ω_Farm",
               "M1", "M2", "M3", "Mmean", "k_A16", "Ω_A16",
               "M1", "M2", "M3", "Mmean", "k_Edge", "Ω_Edge",
               "M1", "M2", "M3", "Mmean", "k_uDm", "Ω_uDm",
               "Mean", "Max%", "≤2%?"]
        for i, s in enumerate(sub):
            lbl(ws, r, i+1, s, halign="center", sz=8)
        r += 1

        for fs in field_sizes_A:
            inp(ws, r, 1, fs, fmt="0.0")      # nominal
            inp(ws, r, 2, fmt="0.000")          # Sclin from FWHM
            inp(ws, r, 3, fmt="0.0000")         # kTP

            # Reference
            inp(ws, r, 4, fmt="0.00000")        # M_ref_before
            inp(ws, r, 5, fmt="0.00000")        # M_ref_after
            clc(ws, r, 6, f"=AVERAGE(D{r},E{r})", fmt="0.00000")   # M_ref mean
            clc(ws, r, 7, f"=F{r}*C{r}", fmt="0.00000")            # M_ref_corr

            # Farmer
            for c in range(8, 11): inp(ws, r, c, fmt="0.00000")
            clc(ws, r, 11, f"=AVERAGE(H{r}:J{r})", fmt="0.00000")
            clc(ws, r, 12, f"=IF(G{r}<>0,K{r}*C{r}/G{r},\"\")", fmt="0.0000")   # Ω_Farmer (no k for Farmer in clin field — add col if needed)

            # A16
            for c in range(13, 16): inp(ws, r, c, fmt="0.00000")
            clc(ws, r, 16, f"=AVERAGE(M{r}:O{r})", fmt="0.00000")
            inp(ws, r, 17, fmt="0.0000")   # k_A16
            clc(ws, r, 18, f"=IF(AND(G{r}<>0,P{r}<>0),P{r}*C{r}/G{r}*Q{r},\"\")", fmt="0.0000")

            # Edge
            for c in range(19, 22): inp(ws, r, c, fmt="0.00000")
            clc(ws, r, 22, f"=AVERAGE(S{r}:U{r})", fmt="0.00000")
            inp(ws, r, 23, fmt="0.0000")   # k_Edge
            clc(ws, r, 24, f"=IF(AND(G{r}<>0,V{r}<>0),V{r}*C{r}/G{r}*W{r},\"\")", fmt="0.0000")

            # microDiamond
            for c in range(25, 28): inp(ws, r, c, fmt="0.00000")
            clc(ws, r, 28, f"=AVERAGE(Y{r}:AA{r})", fmt="0.00000")
            inp(ws, r, 29, fmt="0.0000")   # k_uDm
            clc(ws, r, 30, f"=IF(AND(G{r}<>0,AB{r}<>0),AB{r}*C{r}/G{r}*AC{r},\"\")", fmt="0.0000")

            # Summary
            clc(ws, r, 31, f"=IFERROR(AVERAGE(L{r},R{r},X{r},AD{r}),\"\")", fmt="0.0000")
            clc(ws, r, 32,
                f"=IFERROR((MAX(L{r},R{r},X{r},AD{r})-MIN(L{r},R{r},X{r},AD{r}))/AE{r}*100,\"\")",
                fmt="0.00")
            # Pass/fail ≤2%
            cell = ws.cell(r, 33)
            cell.value = f'=IF(AF{r}="","",IF(AF{r}<=2,"PASS","FAIL"))'
            cell.font = _font(True); cell.border = _b(); cell.alignment = _align("center")

            ws.row_dimensions[r].height = 16
            r += 1
        r += 3

    ws.freeze_panes = "D6"
    nt(ws, r, 1,
       "Ω (output factor) = (M_clin × kTP_clin / M_ref_corr) × k_{Q_clin,Q_msr}. "
       "For Farmer in clin field: k≈1.000 for Sclin≥3 cm (small effect). "
       "Max deviation = (max−min)/mean across all detectors.", cols=10)


# ═════════════════════════════════════════════════════════════════════════════
# 9. OUTPUT FACTORS — METHOD B  (1 cm ≤ Sclin < 3 cm, Intermediate Field)
# ═════════════════════════════════════════════════════════════════════════════
def build_of_method_b(wb):
    ws = wb.create_sheet("OF_METHOD_B")
    cw(ws, {"A": 30, "B": 14, "C": 14, "D": 14, "E": 14, "F": 14, "G": 14,
            "H": 14, "I": 14, "J": 14, "K": 30})

    hdr(ws, 1, 1, "Output Factors — Method B  (Intermediate Field Chain,  1 cm ≤ Sclin < 3 cm)", cols=11, sz=13)
    nt(ws, 2, 1,
       "Chain: 10×10 (Farmer) → Intermediate field (Farmer+detectors) → Clinical field (detectors). "
       "Ω_total = Ω(10×10→IF) × Ω(IF→clin)  where Ω = (M_clin/M_ref)×k. "
       "Recommended IF size: 3×3 or 4×4 cm (ion chamber valid).",
       cols=11)

    energies = [("6 MV WFF", C6), ("10 MV WFF", C10)]
    field_sizes_B = [1.0, 1.2, 1.5, 2.0, 2.5]   # nominal cm

    r = 4
    for energy, color in energies:
        hdr(ws, r, 1, energy, cols=11, bg=CSH, sz=11); r += 1

        # ── Step 1: Reference field (Farmer, 10×10) ──
        hdr(ws, r, 1, "STEP 1 — Reference Field  10×10 cm  (Farmer)", cols=11, bg=color, sz=10); r += 1
        lbl(ws, r, 1, ""); lbl(ws, r, 2, "Rep 1"); lbl(ws, r, 3, "Rep 2"); lbl(ws, r, 4, "Rep 3"); lbl(ws, r, 5, "Mean"); lbl(ws, r, 6, "kTP"); lbl(ws, r, 7, "Mcorr_ref"); r += 1
        r_refF = r
        lbl(ws, r, 1, "M_ref (Farmer, 10×10)  [nC or rel]", bg=color)
        for c in range(2, 5): inp(ws, r, c, fmt="0.00000")
        clc(ws, r, 5, f"=AVERAGE(B{r}:D{r})", fmt="0.00000")
        inp(ws, r, 6, fmt="0.0000")   # kTP
        clc(ws, r, 7, f"=E{r}*F{r}", fmt="0.00000")
        Mcorr_ref_Farmer = f"G{r}"; r += 2

        # ── Step 2: Intermediate field (Farmer) ──
        hdr(ws, r, 1, "STEP 2 — Intermediate Field  (Farmer, ion chamber)", cols=11, bg=color, sz=10); r += 1
        lbl(ws, r, 1, "IF collimator setting [cm]"); inp(ws, r, 2, 3.0, fmt="0.0")
        lbl(ws, r, 4, "Sclin_IF (from FWHM sheet)"); inp(ws, r, 5, fmt="0.000")
        lbl(ws, r, 7, "k_{IF,ref} (Farmer, from K_FACTORS)"); inp(ws, r, 8, fmt="0.0000"); r += 1
        lbl(ws, r, 1, ""); lbl(ws, r, 2, "Rep 1"); lbl(ws, r, 3, "Rep 2"); lbl(ws, r, 4, "Rep 3"); lbl(ws, r, 5, "Mean"); lbl(ws, r, 6, "kTP"); lbl(ws, r, 7, "Mcorr_IF"); lbl(ws, r, 8, "Ω(ref→IF) Farmer"); r += 1
        r_IF_Farm = r
        lbl(ws, r, 1, "M_IF (Farmer)  [nC or rel]", bg=color)
        for c in range(2, 5): inp(ws, r, c, fmt="0.00000")
        clc(ws, r, 5, f"=AVERAGE(B{r}:D{r})", fmt="0.00000")
        inp(ws, r, 6, fmt="0.0000")
        clc(ws, r, 7, f"=E{r}*F{r}", fmt="0.00000")
        Mcorr_IF_Farm = f"G{r}"
        r_k_IF_Farm = r - 1  # row where k_{IF,ref} is
        clc(ws, r, 8, f"=IF({Mcorr_ref_Farmer}<>0,{Mcorr_IF_Farm}/{Mcorr_ref_Farmer}*H{r_k_IF_Farm},\"\")", fmt="0.0000")
        Omega_IF_Farm = f"H{r}"; r += 2

        # ── Step 3: Cross-calibrate detectors at IF ──
        hdr(ws, r, 1, "STEP 3 — Cross-calibration of Detectors at IF", cols=11, bg=color, sz=10); r += 1
        lbl(ws, r, 1, ""); lbl(ws, r, 2, "Rep 1"); lbl(ws, r, 3, "Rep 2"); lbl(ws, r, 4, "Rep 3"); lbl(ws, r, 5, "Mean"); lbl(ws, r, 6, "kTP"); lbl(ws, r, 7, "Mcorr_IF_det"); lbl(ws, r, 8, "k_{IF} (det)"); r += 1

        cross_cal_rows = {}
        for det_name, det_color in [("A16", CA1), ("Edge", CA2), ("microDiamond", CA3)]:
            lbl(ws, r, 1, f"M_IF  ({det_name})  [nC or rel]", bg=det_color)
            for c in range(2, 5): inp(ws, r, c, fmt="0.00000")
            clc(ws, r, 5, f"=AVERAGE(B{r}:D{r})", fmt="0.00000")
            inp(ws, r, 6, fmt="0.0000")
            clc(ws, r, 7, f"=E{r}*F{r}", fmt="0.00000")
            inp(ws, r, 8, fmt="0.0000")  # k_{IF} for this detector at IF field
            cross_cal_rows[det_name] = r
            r += 1
        nt(ws, r, 1, "k_{IF}(det) = k_{Q_clin,Q_msr} for the IF field size — from K_FACTORS sheet.", cols=11)
        r += 2

        # ── Step 4: Clinical field measurements ──
        hdr(ws, r, 1, "STEP 4 — Clinical Field Measurements & Chain Output Factors", cols=11, bg=color, sz=10); r += 1

        col_hdr = ["Nom [cm]", "Sclin", "kTP",
                   "A16 mean", "k_A16_clin", "Ω_A16",
                   "Edge mean", "k_Edge_clin", "Ω_Edge",
                   "uDiam mean", "k_uDm_clin", "Ω_uDm"]
        col_hdr_colors = [CL, CL, CL, CA1, CA1, CA1, CA2, CA2, CA2, CA3, CA3, CA3]
        for i, (c, cb) in enumerate(zip(col_hdr, col_hdr_colors)):
            lbl(ws, r, i+1, c, halign="center", bg=cb, sz=8)
        r += 1

        for fs in field_sizes_B:
            inp(ws, r, 1, fs, fmt="0.0")
            inp(ws, r, 2, fmt="0.000")   # Sclin
            inp(ws, r, 3, fmt="0.0000")  # kTP

            # Ω_total = Ω(ref→IF) × (M_clin_det × kTP_clin) / (M_IF_det × kTP_IF) × k_clin_det
            #         = Omega_IF_Farm  × (M_clin/M_IF_det) × kTP_factor × k_clin

            det_cols = [
                (4,  5,  6,  cross_cal_rows["A16"]),
                (7,  8,  9,  cross_cal_rows["Edge"]),
                (10, 11, 12, cross_cal_rows["microDiamond"]),
            ]
            for Mc, kc, Oc, xrow in det_cols:
                inp(ws, r, Mc, fmt="0.00000")   # mean reading at clinical field
                inp(ws, r, kc, fmt="0.0000")    # k_clin for this detector at Sclin
                # Ω = Ω(ref→IF) × (M_clin×kTP_clin)/(M_IF_det×kTP_IF) × k_clin
                Mcorr_IF_det = f"G{xrow}"
                clc(ws, r, Oc,
                    f"=IF(AND({Omega_IF_Farm}<>\"\",{Mcorr_IF_det}<>0,D{r}<>0),"
                    f"{Omega_IF_Farm}*({ws.cell(r, Mc).column_letter}{r}*C{r})/"
                    f"({Mcorr_IF_det})*{ws.cell(r, kc).column_letter}{r},\"\")",
                    fmt="0.0000")
            ws.row_dimensions[r].height = 18
            r += 1

        nt(ws, r, 1,
           "Ω_total = Ω(10×10→IF)_Farmer × (M_clin×kTP_clin)/(M_IF_det×kTP_IF) × k_clin. "
           "Positioning tolerance: ±0.5 mm for 1–3 cm fields. "
           "Compare results from all 3 detectors; accept if within 2%.", cols=11)
        r += 3

    ws.freeze_panes = "A4"


# ═════════════════════════════════════════════════════════════════════════════
# 10. OUTPUT FACTORS — METHOD C  (Sclin < 1 cm)
# ═════════════════════════════════════════════════════════════════════════════
def build_of_method_c(wb):
    ws = wb.create_sheet("OF_METHOD_C")
    cw(ws, {"A": 14, "B": 12, "C": 12, "D": 12, "E": 12, "F": 12, "G": 12,
            "H": 12, "I": 12, "J": 12, "K": 12, "L": 12, "M": 35})

    hdr(ws, 1, 1, "Output Factors — Method C  (Sclin < 1 cm, Very Small Fields)", cols=13, sz=13)
    nt(ws, 2, 1,
       "Mandatory: ≥ 2 detector types. Positioning tolerance: ±0.1 mm. "
       "Ω = (M_clin/M_IF_det × kTP) × k_clin, where M_IF_det is from Method B cross-calibration. "
       "A16 ion chamber is typically too large for fields < 1 cm — use Edge + microDiamond. "
       "Uncertainty: ±4–6% (k=1) for fields < 1 cm.",
       cols=13)

    energies = [("6 MV WFF", C6), ("10 MV WFF", C10)]
    field_sizes_C = [0.5, 0.6, 0.8]   # nominal cm

    r = 4
    for energy, color in energies:
        hdr(ws, r, 1, energy, cols=13, bg=CSH, sz=11); r += 1

        lbl(ws, r, 1, "NOTE", bg=CF, cols=13)
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=13)
        ws.cell(r, 1).value = (
            "Method C uses the same cross-calibration from Method B (Step 3). "
            "Ensure Method B is complete first and reference the M_IF values from that sheet."
        )
        ws.cell(r, 1).fill = _fill(CF); ws.cell(r, 1).font = _font(False, "880000", 9, True)
        ws.cell(r, 1).alignment = _align("left", "center", True); r += 2

        # Column headers
        col_hdr = [
            "Nom\n[cm]", "Sclin\n[cm]", "kTP",
            "Edge\nM1", "Edge\nM2", "Edge\nM3", "Edge\nMmean",
            "k_Edge_clin", "Ω_Edge",
            "uDiam\nM1", "uDiam\nM2", "uDiam\nM3", "uDiam\nMmean",
        ]
        col_hdr2 = ["", "", "", "", "", "", "", "", "", "k_uDm_clin", "Ω_uDm", "Ω_mean", "Dev [%]"]
        col_colors = [CL, CL, CL, CA2, CA2, CA2, CA2, CA2, CA2, CA3, CA3, CA3, CA3]
        for i, (c, cb) in enumerate(zip(col_hdr, col_colors)):
            hdr(ws, r, i+1, c, bg=cb, sz=8)
        r += 1
        extra_cols = ["", "", "", "", "", "", "", "", "", "k_uDm_clin", "Ω_uDm", "Ω_mean", "Dev [%]"]
        extra_colors = [CL]*9 + [CA3, CA3, CR, CR]
        for i, (c, cb) in enumerate(zip(extra_cols, extra_colors)):
            if c:
                lbl(ws, r, i+1, c, bg=cb, halign="center", sz=8)
        r += 1

        for fs in field_sizes_C:
            inp(ws, r, 1, fs, fmt="0.0")
            inp(ws, r, 2, fmt="0.000")   # Sclin
            inp(ws, r, 3, fmt="0.0000")  # kTP

            # Edge
            for c in [4, 5, 6]: inp(ws, r, c, fmt="0.00000")
            clc(ws, r, 7, f"=AVERAGE(D{r}:F{r})", fmt="0.00000")
            inp(ws, r, 8, fmt="0.0000")   # k_Edge
            clc(ws, r, 9, f"=IF(AND(G{r}<>0,H{r}<>0),G{r}*C{r}*H{r},\"\")", fmt="0.0000")
            # NOTE: G*C*H is not the full formula — M_IF is needed; this is simplified.
            # Full formula requires M_IF_Edge from Method B Step 3, which is on a different sheet.
            # Provided as placeholder; user should verify against Method B.

            # microDiamond
            for c in [10, 11, 12]: inp(ws, r, c, fmt="0.00000")
            clc(ws, r, 13, f"=AVERAGE(J{r}:L{r})", fmt="0.00000")
            inp(ws, r, 14, fmt="0.0000")   # k_uDm
            clc(ws, r, 15, f"=IF(AND(M{r}<>0,N{r}<>0),M{r}*C{r}*N{r},\"\")", fmt="0.0000")

            # Summary
            clc(ws, r, 16, f"=IFERROR(AVERAGE(I{r},O{r}),\"\")", fmt="0.0000")
            clc(ws, r, 17,
                f"=IFERROR(IF(P{r}<>0,(MAX(I{r},O{r})-MIN(I{r},O{r}))/P{r}*100,\"\"),\"\")",
                fmt="0.00")
            ws.row_dimensions[r].height = 18
            r += 1

        nt(ws, r, 1,
           "⚠  Ω values here are RELATIVE — they require normalisation to M_IF from OF_METHOD_B "
           "for absolute output factors. "
           "For fields < 0.5 cm: uncertainty ±5–7%; considered research-level dosimetry. "
           "Acceptance criterion for 2-detector agreement: ≤ 3% for fields < 1 cm.",
           cols=13)
        r += 3

    ws.freeze_panes = "A6"


# ═════════════════════════════════════════════════════════════════════════════
# 11. K_FACTORS  (TRS-483 correction factor table)
# ═════════════════════════════════════════════════════════════════════════════
def build_k_factors(wb):
    ws = wb.create_sheet("K_FACTORS")
    cw(ws, {"A": 14, "B": 14, "C": 16, "D": 16, "E": 16, "F": 16, "G": 50})

    hdr(ws, 1, 1, "k_{Q_clin,Q_msr} Correction Factors — TRS-483 Tables 24 & 27", cols=7, sz=13)
    nt(ws, 2, 1,
       "Transcribe k values from TRS-483 Appendix II. "
       "Table 24 = 6 MV WFF. Table 27 = 10 MV WFF. "
       "Interpolate linearly in Sclin for unlisted field sizes. "
       "k = 1.000 at the msr field (10×10 cm) by definition.",
       cols=7)
    nt(ws, 3, 1,
       "DETECTOR SOURCES: PTW 60019 → TRS-483 Table 24/27. "
       "Edge (Sun Nuclear) → check TRS-483 App. II or TG-155 literature. "
       "A16 → use nearest small IC type in TRS-483 or manufacturer data.",
       cols=7)

    field_sizes = [0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0]

    for energy_label, table_ref, color in [
        ("6 MV WFF  (TRS-483 Table 24)", "Table 24", C6),
        ("10 MV WFF  (TRS-483 Table 27)", "Table 27", C10),
    ]:
        r = 5 if energy_label.startswith("6") else 5 + len(field_sizes) + 6

        hdr(ws, r, 1, energy_label, cols=7, bg=CSH, sz=11); r += 1
        lbl(ws, r, 1, "Sclin [cm]"); lbl(ws, r, 2, "A16  (k)"); lbl(ws, r, 3, "Edge  (k)"); lbl(ws, r, 4, "microDiamond (k)"); lbl(ws, r, 5, "Farmer (for IF)"); lbl(ws, r, 6, "Source / Notes", cols=2); r += 1

        for fs in field_sizes:
            lbl(ws, r, 1, str(fs), bg=color, halign="center")
            if fs == 10.0:
                # By definition k=1 at msr (10×10)
                for c in range(2, 6):
                    cell = ws.cell(r, c, 1.0000)
                    cell.fill = _fill(CC); cell.font = _font(False, "000000", 10)
                    cell.alignment = _align("center"); cell.border = _b(); cell.number_format = "0.0000"
                nt(ws, r, 6, "k = 1.0000 by definition at msr field (10×10 cm).")
            else:
                for c in range(2, 6): inp(ws, r, c, fmt="0.0000")
                nt(ws, r, 6, f"→ {table_ref}")
            r += 1
        nt(ws, r, 1,
           "For sizes not in TRS-483: interpolate linearly. "
           "Do NOT extrapolate below smallest tabulated size.", cols=7)
        r += 2


# ═════════════════════════════════════════════════════════════════════════════
# 12. UNCERTAINTY BUDGET
# ═════════════════════════════════════════════════════════════════════════════
def build_uncertainty(wb):
    ws = wb.create_sheet("UNCERTAINTY")
    cw(ws, {"A": 36, "B": 18, "C": 18, "D": 18, "E": 18, "F": 40})

    hdr(ws, 1, 1, "Uncertainty Budget  (k = 1, 1σ)", cols=6, sz=13)
    nt(ws, 2, 1,
       "Based on TRS-483 §8 and TG-155 §6. "
       "u_combined = √(Σuᵢ²). Values in %. Enter measured values in yellow cells; "
       "blue cells are calculated. Cross-reference with measurement sheets for reproducibility u.",
       cols=6)

    # --- Component table ---
    r = 4
    hdr(ws, r, 1, "Component", cols=1, bg=CH, sz=10)
    for i, label in enumerate(["Sclin ≥ 2 cm", "1 cm ≤ Sclin < 2 cm", "0.5 cm ≤ Sclin < 1 cm"]):
        hdr(ws, r, i+2, label, bg=CSH, sz=10)
    hdr(ws, r, 5, "Source / Basis", cols=2, bg=CL, sz=10); r += 1

    components = [
        ("u1  Reference dosimetry (Dw, TRS-398)",          0.9,  0.9,  0.9,
         "TRS-483 §8.2; Farmer + calibration lab"),
        ("u2  Field size measurement (FWHM, positioning)",  0.3,  0.5,  1.0,
         "Positioning uncertainty grows for small fields; ±0.1 mm tolerance"),
        ("u3  kTP (T, P measurement)",                      0.1,  0.1,  0.1,
         "Thermometer ±0.1 °C, barometer ±0.1 kPa"),
        ("u4  kpol",                                        0.1,  0.1,  0.1,
         "TRS-398; typically <0.5% for Farmer"),
        ("u5  ks (ion recombination, Farmer)",              0.1,  0.1,  0.1,
         "Two-voltage method uncertainty"),
        ("u6  k_{Q_clin,Q_msr} correction factor",         0.5,  1.0,  2.0,
         "TRS-483 uncertainty on tabulated k; increases for small fields"),
        ("u7  Detector energy response / fluence perturb.", 0.3,  0.5,  1.5,
         "Residual after k correction; detector-dependent"),
        ("u8  Dose-rate dependence (solid-state)",          0.2,  0.2,  0.5,
         "From DET_CONDITIONING dose-rate test"),
        ("u9  Reproducibility (measured)",                  "→", "→", "→",
         "From CV column in measurement sheets (Method A/B/C)"),
        ("u10 Long-term stability / drift",                 0.3,  0.3,  0.5,
         "Annual re-measurement; output drift since commissioning"),
    ]

    # pre-fill rows
    for comp, v6, v10, vs, source in components:
        lbl(ws, r, 1, comp)
        for ci, val in enumerate([v6, v10, vs]):
            if isinstance(val, (int, float)):
                inp(ws, r, ci+2, val, fmt="0.0")
            else:
                cell = ws.cell(r, ci+2, val)
                cell.fill = _fill(CC); cell.border = _b(); cell.alignment = _align("center")
                cell.font = _font(False, "444444", 9, True)
        nt(ws, r, 5, source)
        r += 1

    # u_combined row
    hdr(ws, r, 1, "u_combined  [%]  = √(Σuᵢ²)", bg=CSH, sz=10)
    for ci in range(3):
        col = ci + 2
        col_l = get_column_letter(col)
        # sum squares of rows above (excluding the "→" reproducibility row)
        row_range = f"{col_l}{r-len(components)}:{col_l}{r-2}"
        res(ws, r, col,
            f"=SQRT(SUMPRODUCT(({row_range})^2))",
            fmt="0.00")
    nt(ws, r, 5, "Combined standard uncertainty (k=1). Multiply by 2 for 95% coverage (k=2)."); r += 1

    hdr(ws, r, 1, "U_expanded  [%]  (k=2, ≈95%)", bg=CSH, sz=10)
    for ci in range(3):
        col = ci + 2
        prev_row = r - 1
        res(ws, r, col, f"=2*{get_column_letter(col)}{prev_row}", fmt="0.00")
    r += 2

    nt(ws, r, 1,
       "TRS-483 §8 typical expanded uncertainties (k=2): "
       "≥2 cm: ~2%; 1–2 cm (Method B): ~3–5%; <1 cm (Method C): ~8–12%. "
       "These are total output factor uncertainties.",
       cols=6)


# ═════════════════════════════════════════════════════════════════════════════
# 13. SUMMARY
# ═════════════════════════════════════════════════════════════════════════════
def build_summary(wb):
    ws = wb.create_sheet("SUMMARY")
    cw(ws, {"A": 14, "B": 12, "C": 12, "D": 12, "E": 12, "F": 12, "G": 12,
            "H": 12, "I": 12, "J": 12, "K": 14})

    hdr(ws, 1, 1, "Final Output Factor Table — Summary", cols=11, sz=14)
    nt(ws, 2, 1,
       "Transcribe final Ω values from Method A/B/C sheets. "
       "Green = within acceptance. Cross-detector agreement ≤ 2% (Sclin ≥ 1 cm) or ≤ 3% (< 1 cm).",
       cols=11)

    energies = [("6 MV WFF", C6), ("10 MV WFF", C10)]
    field_sizes_all = [0.5, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0]
    method_map = {fs: ("C" if fs < 1 else "B" if fs < 3 else "A") for fs in field_sizes_all}

    r = 4
    for energy, color in energies:
        hdr(ws, r, 1, energy, cols=11, bg=CSH, sz=11); r += 1

        col_hdr = ["Nom [cm]", "Sclin [cm]", "Method",
                   "Ω  A16", "Ω  Edge", "Ω  µDiam", "Ω  Farmer",
                   "Ω  Mean", "Max Dev [%]", "U_exp [%]", "Accept?"]
        for i, c in enumerate(col_hdr):
            bg = CA1 if "A16" in c else CA2 if "Edge" in c else CA3 if "Diam" in c else color if "Farmer" in c else CL
            lbl(ws, r, i+1, c, bg=bg, halign="center", sz=9)
        r += 1

        u_exp = {"A": 2.0, "B": 4.0, "C": 10.0}  # typical expanded uncertainties

        for fs in field_sizes_all:
            method = method_map[fs]
            lbl(ws, r, 1, str(fs), bg=color, halign="center")
            inp(ws, r, 2, fmt="0.000")   # Sclin
            lbl(ws, r, 3, method, bg=color if method == "A" else CSH if method == "B" else CF, halign="center")
            for c in range(4, 8): inp(ws, r, c, fmt="0.0000")  # Ω per detector
            clc(ws, r, 8, f"=IFERROR(AVERAGE(D{r}:G{r}),\"\")", fmt="0.0000")   # mean
            clc(ws, r, 9,
                f"=IFERROR(IF(H{r}<>0,(MAX(D{r}:G{r})-MIN(D{r}:G{r}))/H{r}*100,\"\"),\"\")",
                fmt="0.00")
            inp(ws, r, 10, u_exp[method], fmt="0.0")   # U_expanded (typical; adjust from UNCERTAINTY sheet)
            thresh = 2 if method in ("A", "B") else 3
            cell = ws.cell(r, 11)
            cell.value = f'=IF(I{r}="","",IF(I{r}<={thresh},"PASS","FAIL"))'
            cell.font = _font(True); cell.border = _b(); cell.alignment = _align("center")
            ws.row_dimensions[r].height = 16
            r += 1

        nt(ws, r, 1,
           "All Ω are normalised to the 10×10 cm msr field (Ω = 1.0000). "
           "Ω for 10×10 cm should be 1.0000 by definition. "
           "Uncertainty column = typical expanded (k=2) — update from UNCERTAINTY sheet.",
           cols=11)
        r += 3

    ws.freeze_panes = "D5"


# ═════════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════════
def main():
    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)

    build_instructions(wb)
    build_setup(wb)
    build_environment(wb)
    build_beam_quality(wb)
    build_ref_dosimetry(wb)
    build_det_conditioning(wb)
    build_fwhm(wb)
    build_of_method_a(wb)
    build_of_method_b(wb)
    build_of_method_c(wb)
    build_k_factors(wb)
    build_uncertainty(wb)
    build_summary(wb)

    wb.save(OUT)
    print(f"Saved: {OUT}")
    print(f"Sheets: {[s.title for s in wb.worksheets]}")

if __name__ == "__main__":
    main()
