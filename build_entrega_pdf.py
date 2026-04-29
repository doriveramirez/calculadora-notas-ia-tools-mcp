from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import List

from PIL import Image as PILImage, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, StyleSheet1, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
EVIDENCES = ROOT / "evidencias"
OUTPUT = ROOT / "ENTREGA_CALCULADORA_NOTAS_TOOLS_MCP.pdf"


def register_fonts() -> None:
    candidates = {
        "body": [Path(r"C:\Windows\Fonts\calibri.ttf"), Path(r"C:\Windows\Fonts\arial.ttf")],
        "bold": [Path(r"C:\Windows\Fonts\calibrib.ttf"), Path(r"C:\Windows\Fonts\arialbd.ttf")],
        "mono": [Path(r"C:\Windows\Fonts\consola.ttf"), Path(r"C:\Windows\Fonts\cour.ttf")],
    }

    selected = {}
    for key, paths in candidates.items():
        selected[key] = next((path for path in paths if path.exists()), None)

    if all(selected.values()):
        pdfmetrics.registerFont(TTFont("EntregaBody", str(selected["body"])))
        pdfmetrics.registerFont(TTFont("EntregaBold", str(selected["bold"])))
        pdfmetrics.registerFont(TTFont("EntregaMono", str(selected["mono"])))


def build_styles() -> StyleSheet1:
    register_fonts()
    styles = getSampleStyleSheet()
    body = "EntregaBody" if "EntregaBody" in pdfmetrics.getRegisteredFontNames() else "Helvetica"
    bold = "EntregaBold" if "EntregaBold" in pdfmetrics.getRegisteredFontNames() else "Helvetica-Bold"
    mono = "EntregaMono" if "EntregaMono" in pdfmetrics.getRegisteredFontNames() else "Courier"

    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            parent=styles["Title"],
            fontName=bold,
            fontSize=22,
            leading=28,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#0f172a"),
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSubtitle",
            parent=styles["BodyText"],
            fontName=body,
            fontSize=12,
            leading=17,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#334155"),
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionTitle",
            parent=styles["Heading1"],
            fontName=bold,
            fontSize=17,
            leading=21,
            textColor=colors.HexColor("#0f172a"),
            spaceBefore=6,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SubTitle",
            parent=styles["Heading2"],
            fontName=bold,
            fontSize=12.5,
            leading=16,
            textColor=colors.HexColor("#1d4ed8"),
            spaceBefore=6,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyCopy",
            parent=styles["BodyText"],
            fontName=body,
            fontSize=10.8,
            leading=15.5,
            textColor=colors.HexColor("#111827"),
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeStyle",
            parent=styles["Code"],
            fontName=mono,
            fontSize=8.4,
            leading=10.8,
            leftIndent=8,
            rightIndent=8,
            borderPadding=8,
            borderWidth=0.5,
            borderColor=colors.HexColor("#cbd5e1"),
            backColor=colors.HexColor("#f8fafc"),
            spaceAfter=10,
        )
    )
    return styles


def escape_html(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def page_number(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.HexColor("#64748b"))
    canvas.drawRightString(A4[0] - 1.6 * cm, 1.1 * cm, f"{doc.page}")
    canvas.restoreState()


def bullet_list(items: List[str], styles: StyleSheet1) -> ListFlowable:
    return ListFlowable(
        [ListItem(Paragraph(escape_html(item), styles["BodyCopy"])) for item in items],
        bulletType="bullet",
        leftIndent=18,
    )


def md_flowables(text: str, styles: StyleSheet1, skip_first_heading: bool = False) -> list:
    flowables = []
    lines = text.replace("\r\n", "\n").split("\n")
    list_items: List[str] = []
    code_lines: List[str] = []
    in_code = False
    heading_skipped = False

    def flush_list() -> None:
        nonlocal list_items
        if list_items:
            flowables.append(bullet_list([item[2:].strip() for item in list_items], styles))
            flowables.append(Spacer(1, 0.12 * cm))
            list_items = []

    def flush_code() -> None:
        nonlocal code_lines
        if code_lines:
            flowables.append(Preformatted("\n".join(code_lines), styles["CodeStyle"]))
            code_lines = []

    for raw_line in lines:
        line = raw_line.rstrip()

        if line.startswith("```"):
            flush_list()
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_lines.append(raw_line)
            continue

        if not line.strip():
            flush_list()
            flowables.append(Spacer(1, 0.08 * cm))
            continue

        if line.startswith("- "):
            list_items.append(line)
            continue

        flush_list()

        if line.startswith("# "):
            if skip_first_heading and not heading_skipped:
                heading_skipped = True
                continue
            flowables.append(Paragraph(escape_html(line[2:]), styles["SectionTitle"]))
            continue
        if line.startswith("## "):
            flowables.append(Paragraph(escape_html(line[3:]), styles["SubTitle"]))
            continue
        if line.startswith("### "):
            flowables.append(Paragraph(escape_html(line[4:]), styles["SubTitle"]))
            continue

        flowables.append(Paragraph(escape_html(line), styles["BodyCopy"]))

    flush_list()
    flush_code()
    return flowables


def code_block(path: Path, styles: StyleSheet1) -> Preformatted:
    return Preformatted(path.read_text(encoding="utf-8"), styles["CodeStyle"])


def image_sources() -> list[tuple[Path, Path, str, str]]:
    return [
        (ROOT / "PRD.md", EVIDENCES / "01_prd.png", "#0b1220", "#dbeafe"),
        (ROOT / "SPEC.md", EVIDENCES / "02_spec.png", "#111827", "#e5e7eb"),
        (ROOT / "AGENTS.md", EVIDENCES / "03_agents.png", "#0f172a", "#e2e8f0"),
        (ROOT / "tools_notas.py", EVIDENCES / "04_tools_notas.png", "#13233b", "#dcfce7"),
        (EVIDENCES / "tool_specialist_interaccion.md", EVIDENCES / "05_tool_specialist.png", "#172554", "#eff6ff"),
        (EVIDENCES / "builder_interaccion.md", EVIDENCES / "06_builder.png", "#1e293b", "#f8fafc"),
        (EVIDENCES / "ejecucion_media.txt", EVIDENCES / "07_programa_media.png", "#111827", "#d1fae5"),
        (EVIDENCES / "ejecucion_mediana.txt", EVIDENCES / "08_programa_mediana.png", "#111827", "#fde68a"),
        (EVIDENCES / "tester_interaccion.md", EVIDENCES / "09_tester.png", "#1f2937", "#f9fafb"),
        (EVIDENCES / "publisher_interaccion.md", EVIDENCES / "10_publisher.png", "#0f172a", "#e0f2fe"),
        (EVIDENCES / "mcp_intento.md", EVIDENCES / "11_mcp_intento.png", "#1c1917", "#fae8ff"),
        (ROOT / "README.md", EVIDENCES / "12_readme.png", "#13111c", "#f3f4f6"),
        (EVIDENCES / "revision_archivos_publisher.txt", EVIDENCES / "13_revision_archivos_publisher.png", "#0c1426", "#dbeafe"),
        (EVIDENCES / "pruebas_unitarias.txt", EVIDENCES / "14_pruebas_unitarias.png", "#0b1220", "#dcfce7"),
        (EVIDENCES / "github_publicacion_y_issue.txt", EVIDENCES / "15_github_publicacion_issue.png", "#102a43", "#d9f99d"),
    ]


def build_png_evidences() -> None:
    font_candidates = [Path(r"C:\Windows\Fonts\consola.ttf"), Path(r"C:\Windows\Fonts\cour.ttf")]
    font_path = next((path for path in font_candidates if path.exists()), None)
    if font_path:
        font = ImageFont.truetype(str(font_path), 26)
        title_font = ImageFont.truetype(str(font_path), 24)
    else:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()

    for src, dest, bg, fg in image_sources():
        text = src.read_text(encoding="utf-8")
        wrapped_lines: List[str] = []
        for raw_line in text.splitlines() or [""]:
            if not raw_line:
                wrapped_lines.append("")
                continue
            start = 0
            while start < len(raw_line):
                wrapped_lines.append(raw_line[start:start + 88])
                start += 88

        width = 1600
        pad_x = 36
        pad_y = 32
        bar_height = 64
        gap = 12
        radius = 14

        dummy = PILImage.new("RGB", (width, 200), bg)
        draw = ImageDraw.Draw(dummy)
        left, top, right, bottom = draw.textbbox((0, 0), "Ag", font=font)
        line_height = (bottom - top) + gap
        height = bar_height + pad_y * 2 + max(1, len(wrapped_lines)) * line_height

        image = PILImage.new("RGB", (width, height), bg)
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle((18, 14, width - 18, height - 14), radius=radius, fill=bg, outline="#334155", width=2)
        draw.rounded_rectangle((18, 14, width - 18, 14 + bar_height), radius=radius, fill="#020617")
        draw.text((pad_x, 28), src.name, font=title_font, fill="#93c5fd")

        y = bar_height + pad_y
        for line in wrapped_lines:
            draw.text((pad_x, y), line, font=font, fill=fg)
            y += line_height

        image.save(dest)


def screenshot_image(path: Path, max_width: float, max_height: float) -> Image:
    image = Image(str(path))
    scale = min(max_width / image.imageWidth, max_height / image.imageHeight)
    image.drawWidth = image.imageWidth * scale
    image.drawHeight = image.imageHeight * scale
    return image


def summary_table(styles: StyleSheet1) -> Table:
    rows = [
        ["Apartado", "Contenido"],
        ["Planificación", "PRD, SPEC y definición de agentes."],
        ["Tools", "Separación del cálculo en `tools_notas.py`."],
        ["Desarrollo", "Adaptación de `main.py` y pruebas unitarias."],
        ["Verificación", "Ejecuciones reales de media y mediana."],
        ["Publisher", "Publicación real en GitHub y creación del issue de mejoras."],
    ]
    table = Table(rows, colWidths=[4.2 * cm, 11.0 * cm], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e2e8f0")),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#0f172a")),
                ("FONTNAME", (0, 0), (-1, 0), styles["SubTitle"].fontName),
                ("FONTNAME", (0, 1), (-1, -1), styles["BodyCopy"].fontName),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cbd5e1")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


def build_story(styles: StyleSheet1) -> list:
    prd = (ROOT / "PRD.md").read_text(encoding="utf-8")
    spec = (ROOT / "SPEC.md").read_text(encoding="utf-8")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    reflection = (ROOT / "REFLEXION.md").read_text(encoding="utf-8")
    tool_specialist = (EVIDENCES / "tool_specialist_interaccion.md").read_text(encoding="utf-8")
    builder = (EVIDENCES / "builder_interaccion.md").read_text(encoding="utf-8")
    tester = (EVIDENCES / "tester_interaccion.md").read_text(encoding="utf-8")
    publisher = (EVIDENCES / "publisher_interaccion.md").read_text(encoding="utf-8")
    mcp = (EVIDENCES / "mcp_intento.md").read_text(encoding="utf-8")
    run_media = (EVIDENCES / "ejecucion_media.txt").read_text(encoding="utf-8")
    run_mediana = (EVIDENCES / "ejecucion_mediana.txt").read_text(encoding="utf-8")
    tests = (EVIDENCES / "pruebas_unitarias.txt").read_text(encoding="utf-8")
    publisher_review = (EVIDENCES / "revision_archivos_publisher.txt").read_text(encoding="utf-8")
    github_publication = (EVIDENCES / "github_publicacion_y_issue.txt").read_text(encoding="utf-8")

    story = []
    story.append(Spacer(1, 2.8 * cm))
    story.append(Paragraph("Práctica: Desarrollo con agentes", styles["CoverTitle"]))
    story.append(Paragraph("Parte 2 y Parte 3", styles["CoverTitle"]))
    story.append(Paragraph("Calculadora de notas con tools y preparación para GitHub", styles["CoverSubtitle"]))
    story.append(Paragraph(f"Fecha: {datetime.now().strftime('%d/%m/%Y')}", styles["CoverSubtitle"]))
    story.append(Spacer(1, 0.8 * cm))
    story.append(summary_table(styles))
    story.append(Spacer(1, 0.7 * cm))
    story.append(
        Paragraph(
            "En esta práctica se amplía la calculadora de notas para separar la lógica de cálculo "
            "en funciones externas y documentar la preparación del proyecto para GitHub.",
            styles["BodyCopy"],
        )
    )
    story.append(PageBreak())

    story.append(Paragraph("1. Introducción", styles["SectionTitle"]))
    story.append(
        Paragraph(
            "La aplicación sigue siendo sencilla: pide el nombre del alumno, tres notas y el tipo de cálculo. "
            "La diferencia principal está en que la media y la mediana ya no se resuelven dentro del programa principal, "
            "sino mediante una tool externa en Python.",
            styles["BodyCopy"],
        )
    )
    story.append(
        bullet_list(
            [
                "Se separa la lógica de cálculo en `tools_notas.py`.",
                "El usuario puede elegir entre media o mediana.",
                "La entrega documenta la publicación real en GitHub y el issue creado.",
            ],
            styles,
        )
    )
    story.append(PageBreak())

    story.append(Paragraph("2. PRD", styles["SectionTitle"]))
    story.extend(md_flowables(prd, styles, skip_first_heading=True))
    story.append(PageBreak())

    story.append(Paragraph("3. SPEC", styles["SectionTitle"]))
    story.extend(md_flowables(spec, styles, skip_first_heading=True))
    story.append(PageBreak())

    story.append(Paragraph("4. Organización del trabajo", styles["SectionTitle"]))
    story.extend(md_flowables(agents, styles, skip_first_heading=True))
    story.append(PageBreak())

    story.append(Paragraph("5. Tool Specialist y desarrollo", styles["SectionTitle"]))
    story.append(
        Paragraph(
            "Primero se definió la lógica del cálculo en una tool externa y después se integró en `main.py`.",
            styles["BodyCopy"],
        )
    )
    story.append(Paragraph("5.1. Evidencia del Tool Specialist", styles["SubTitle"]))
    story.extend(md_flowables(tool_specialist, styles, skip_first_heading=True))
    story.append(Paragraph("5.2. Archivo tools_notas.py", styles["SubTitle"]))
    story.append(code_block(ROOT / "tools_notas.py", styles))
    story.append(Paragraph("5.3. Evidencia del Builder", styles["SubTitle"]))
    story.extend(md_flowables(builder, styles, skip_first_heading=True))
    story.append(PageBreak())

    story.append(Paragraph("6. Código principal y pruebas", styles["SectionTitle"]))
    story.append(Paragraph("6.1. Archivo main.py", styles["SubTitle"]))
    story.append(code_block(ROOT / "main.py", styles))
    story.append(Paragraph("6.2. Archivo test_main.py", styles["SubTitle"]))
    story.append(code_block(ROOT / "test_main.py", styles))
    story.append(PageBreak())

    story.append(Paragraph("7. Verificación", styles["SectionTitle"]))
    story.extend(md_flowables(tester, styles, skip_first_heading=True))
    story.append(Paragraph("7.1. Ejecución calculando media", styles["SubTitle"]))
    story.append(Preformatted(run_media, styles["CodeStyle"]))
    story.append(Paragraph("7.2. Ejecución calculando mediana", styles["SubTitle"]))
    story.append(Preformatted(run_mediana, styles["CodeStyle"]))
    story.append(Paragraph("7.3. Resultado de las pruebas unitarias", styles["SubTitle"]))
    story.append(Preformatted(tests, styles["CodeStyle"]))
    story.append(PageBreak())

    story.append(Paragraph("8. Publisher y preparación para GitHub", styles["SectionTitle"]))
    story.extend(md_flowables(publisher, styles, skip_first_heading=True))
    story.append(Paragraph("8.1. Revisión local del proyecto", styles["SubTitle"]))
    story.append(Preformatted(publisher_review, styles["CodeStyle"]))
    story.append(Paragraph("8.2. Publicación e issue en GitHub", styles["SubTitle"]))
    story.append(Preformatted(github_publication, styles["CodeStyle"]))
    story.append(Paragraph("8.3. Registro de la publicación", styles["SubTitle"]))
    story.extend(md_flowables(mcp, styles, skip_first_heading=True))
    story.append(PageBreak())

    story.append(Paragraph("9. Documentación final", styles["SectionTitle"]))
    story.append(Paragraph("9.1. README", styles["SubTitle"]))
    story.extend(md_flowables(readme, styles, skip_first_heading=True))
    story.append(Paragraph("9.2. Reflexión final", styles["SubTitle"]))
    story.extend(md_flowables(reflection, styles, skip_first_heading=True))
    story.append(PageBreak())

    story.append(Paragraph("10. Anexo de capturas", styles["SectionTitle"]))
    story.append(
        Paragraph(
            "En las páginas siguientes se incluyen las capturas completas de los documentos y evidencias de la práctica.",
            styles["BodyCopy"],
        )
    )
    story.append(PageBreak())
    return story


def build_pdf() -> Path:
    build_png_evidences()
    styles = build_styles()
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=1.7 * cm,
        rightMargin=1.7 * cm,
        topMargin=1.7 * cm,
        bottomMargin=1.5 * cm,
        title="Práctica: Desarrollo con agentes - Parte 2 y Parte 3",
        author="",
    )

    story = build_story(styles)

    max_width = A4[0] - doc.leftMargin - doc.rightMargin
    max_height = A4[1] - doc.topMargin - doc.bottomMargin - 1.2 * cm
    for _, image_path, _, _ in image_sources():
        story.append(Paragraph(image_path.name, styles["SubTitle"]))
        story.append(screenshot_image(image_path, max_width, max_height))
        story.append(PageBreak())

    doc.build(story, onFirstPage=page_number, onLaterPages=page_number)
    return OUTPUT


if __name__ == "__main__":
    print(build_pdf())
