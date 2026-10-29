import io
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    """Set the background color of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
    """Set inner padding for a table cell in twips."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def generate_pocket_cram_sheet(specialty="All Specialties", questions_list=None, missed_only=False):
    """
    Generate an ultra-compact, professional 2-page Pocket Viva Cram Sheet (.docx)
    containing high-yield clinical rules, examiner keywords, and model answers.
    Returns bytes of the docx file.
    """
    doc = docx.Document()
    
    # Page setup - Compact 0.45 in margins for pocket cheat-sheet layout
    for section in doc.sections:
        section.top_margin = Inches(0.45)
        section.bottom_margin = Inches(0.45)
        section.left_margin = Inches(0.45)
        section.right_margin = Inches(0.45)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)
    
    # Header Banner Table
    banner_table = doc.add_table(rows=1, cols=1)
    banner_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    banner_table.autofit = False
    banner_cell = banner_table.rows[0].cells[0]
    banner_cell.width = Inches(7.6)
    set_cell_background(banner_cell, "0F172A")
    set_cell_margins(banner_cell, top=140, bottom=140, left=180, right=180)
    
    p_b = banner_cell.paragraphs[0]
    p_b.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_b.paragraph_format.space_before = Pt(0)
    p_b.paragraph_format.space_after = Pt(2)
    
    r_b1 = p_b.add_run("🩺 MEDSKILL AI — POCKET VIVA CRAM SHEET")
    r_b1.bold = True
    r_b1.font.size = Pt(13)
    r_b1.font.color.rgb = RGBColor(255, 255, 255)
    r_b1.font.name = "Arial"
    
    p_b2 = banner_cell.add_paragraph()
    p_b2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_b2.paragraph_format.space_before = Pt(0)
    p_b2.paragraph_format.space_after = Pt(0)
    mode_text = "Targeted Missed-Question Drill" if missed_only else f"High-Yield Practical Viva Revision ({specialty})"
    r_b2 = p_b2.add_run(f"Academic Practical Exam Companion | {mode_text} | Allied Health Technology")
    r_b2.font.size = Pt(8.5)
    r_b2.font.color.rgb = RGBColor(186, 230, 253)
    r_b2.font.name = "Arial"

    # Add quick metadata strip
    doc.add_paragraph()
    p_meta = doc.paragraphs[-1]
    p_meta.paragraph_format.space_before = Pt(4)
    p_meta.paragraph_format.space_after = Pt(6)
    r_meta = p_meta.add_run("📌 EXAMINER INSTRUCTIONS: Memorize these 1-line physiological principles, equipment cutoff values, and emergency protocols before entering your practical oral examination room.")
    r_meta.bold = True
    r_meta.font.size = Pt(8.5)
    r_meta.font.color.rgb = RGBColor(185, 28, 28)
    r_meta.font.name = "Arial"

    # If no questions provided, show fallback
    if not questions_list:
        p_empty = doc.add_paragraph("No specific questions selected. Complete a viva session to populate personalized missed items.")
        p_empty.font.size = Pt(9)
        output = io.BytesIO()
        doc.save(output)
        return output.getvalue()

    # Limit to top 20 questions for an authentic 2-3 page compact cram sheet
    selected_items = questions_list[:24]

    # Two-column key points table for ultra-dense high-yield layout
    table = doc.add_table(rows=len(selected_items) + 1, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    # Header Row
    headers = ["ID & Topic", "Examiner Core Question & Physiological Rationale", "High-Yield Keywords & Rules"]
    col_widths = [Inches(1.5), Inches(3.6), Inches(2.5)]
    
    for c_idx, h_text in enumerate(headers):
        cell = table.rows[0].cells[c_idx]
        cell.width = col_widths[c_idx]
        set_cell_background(cell, "1E293B")
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h_text)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.name = "Arial"

    # Populate Data Rows
    for r_idx, q in enumerate(selected_items):
        row = table.rows[r_idx + 1]
        bg_color = "F8FAFC" if (r_idx % 2 == 0) else "FFFFFF"
        
        # Cell 0: ID & Topic
        cell_0 = row.cells[0]
        cell_0.width = col_widths[0]
        set_cell_background(cell_0, bg_color)
        set_cell_margins(cell_0, top=70, bottom=70, left=90, right=90)
        p0 = cell_0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(2)
        r0_id = p0.add_run(f"[{q['id']}]\n")
        r0_id.bold = True
        r0_id.font.size = Pt(8)
        r0_id.font.color.rgb = RGBColor(2, 132, 199)
        r0_id.font.name = "Arial"
        
        r0_top = p0.add_run(f"{q['topic']}\n({q['difficulty']})")
        r0_top.font.size = Pt(7.5)
        r0_top.font.color.rgb = RGBColor(71, 85, 105)
        r0_top.font.name = "Arial"

        # Cell 1: Question & Explanation
        cell_1 = row.cells[1]
        cell_1.width = col_widths[1]
        set_cell_background(cell_1, bg_color)
        set_cell_margins(cell_1, top=70, bottom=70, left=90, right=90)
        p1 = cell_1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(2)
        r1_q = p1.add_run(f"Q: {q['question']}\n")
        r1_q.bold = True
        r1_q.font.size = Pt(8)
        r1_q.font.color.rgb = RGBColor(15, 23, 42)
        r1_q.font.name = "Arial"
        
        r1_exp = p1.add_run(f"Rationale: {q['explanation']}")
        r1_exp.font.size = Pt(7.5)
        r1_exp.font.color.rgb = RGBColor(51, 65, 85)
        r1_exp.font.name = "Arial"

        # Cell 2: Key Points / Examiner Buzzwords
        cell_2 = row.cells[2]
        cell_2.width = col_widths[2]
        set_cell_background(cell_2, bg_color)
        set_cell_margins(cell_2, top=70, bottom=70, left=90, right=90)
        p2 = cell_2.paragraphs[0]
        p2.paragraph_format.space_before = Pt(0)
        p2.paragraph_format.space_after = Pt(0)
        
        pts = q.get("key_points", [])
        for pt in pts:
            r2_pt = p2.add_run(f"• {pt}\n")
            r2_pt.font.size = Pt(7.5)
            r2_pt.font.color.rgb = RGBColor(15, 23, 42)
            r2_pt.font.name = "Arial"
            
        r2_ans = p2.add_run(f"Key: {q['options'][q['correct_index']]}")
        r2_ans.bold = True
        r2_ans.font.size = Pt(7.5)
        r2_ans.font.color.rgb = RGBColor(22, 163, 74)
        r2_ans.font.name = "Arial"

    # Footer note
    p_ft = doc.add_paragraph()
    p_ft.paragraph_format.space_before = Pt(8)
    p_ft.paragraph_format.space_after = Pt(0)
    p_ft.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_ft = p_ft.add_run("MedSkill AI Academic Prototype | Deployed at medskill-ai.streamlit.app | Verified with 8 Student Stakeholders")
    r_ft.font.size = Pt(7)
    r_ft.font.color.rgb = RGBColor(148, 163, 184)
    r_ft.font.name = "Arial"

    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()
