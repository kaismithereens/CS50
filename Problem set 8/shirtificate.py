from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 24)
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)
        #self.set_draw_color(0, 80, 180)
        #self.set_fill_color(230, 230, 0)
        #self.set_text_color(255, 255, 255)
        self.set_line_width(0)
        self.cell(
            width,
            9,
            self.title,
            border=0,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            #fill=True,
        )
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(128)
        #self.cell(0, 10, f"Page {self.page_no()}", align="C")

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

    def chapter_body(self, fname):
        # Reading text file:
        with open(fname, "rb") as fh:
            txt = fh.read().decode("latin-1")
        with self.text_columns(
            ncols=3, gutter=5, text_align="J", line_height=1.19
        ) as cols:
            # Setting font: Times 12
            self.set_font("Times", size=12)
            cols.write(txt)
            cols.ln()
            # Final mention in italics:
            self.set_font(style="I")
            cols.write("(end of excerpt)")

    def print_chapter(self, num, title, fname):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(fname)


pdf = PDF()
pdf.set_title("CS50 Shirtificate")
pdf.add_page()
pdf.image(
    "shirtificate.png", 0, 50, 0, 0,)
pdf.set_xy((210) / 2, (297) / 2)
pdf.set_text_color(255,255,255)

name = input("Your name: ")
#pdf.cell(w=None, h=None, text='TEAs Shirt', align='C', center=True)
pdf.cell(w=None, h=None, text=f'{name} took CS50', align='C', center=True)


pdf.output("shirtificate.pdf")

