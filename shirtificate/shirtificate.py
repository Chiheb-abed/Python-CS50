from fpdf import FPDF


def main():
    name= input ("Name: ")
    pdf = FPDF(orientation='portrait', format='A4')
    pdf.add_page()
    pdf.set_font("helvetica", "B", 50)
    pdf.cell(80)
    pdf.cell(30, 10, "CS50 Shirtificate", align="C")
    pdf.ln(50)
    pdf.image("shirtificate.png",x="c")
    pdf.set_y(130)
    pdf.set_text_color(255,255,255)
    pdf.set_font("helvetica", "B", 25)
    pdf.cell(10,10,text=name+" took CS50", align="C",center=True)
    name+=".pdf"
    pdf.output("shirtificate.pdf")
if __name__=="__main__":
    main()
