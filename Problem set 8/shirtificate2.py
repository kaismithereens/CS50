from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 16)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(128)

    def chapter_title(self, num, label):
        self.set_font("helvetica", "", 12)
        self.set_fill_color(200, 220, 255)
        self.cell(
            0,
            6,
            f"Chapter {num} : {label}",
            new_x="LMARGIN",
            new_y="NEXT",
            border="L",
            fill=True,
        )
        self.ln(4)




pdf = PDF()
pdf.set_title("CS50 Shirtificate")
pdf.add_page()
pdf.image(
    "shirtificate.png", 0, 50, 0, 0,)
pdf.set_xy((210) / 2, (297) / 2)
pdf.set_text_color(255,255,255)
pdf.cell(w=None, h=None, text='TEAs Shirt', align='C', center=True)


pdf.output("test3.pdf")

