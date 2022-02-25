from fpdf import FPDF
import webbrowser

class PDFReport:
    """
    Creates a pdf report about the each flatmate has to pay for given period.
    """

    def __init__(self):
        self.filename = "files/bill-report.pdf"

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')

        flatmate1_pays = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pays = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf.add_page()
        pdf.image("files/house.png", w=40, h=40)

        pdf.set_font(family="Times", size=24, style='B')

        pdf.cell(w=0, h=100, txt="Flatmates Bill", align="C", ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=25, txt="Period: ")
        pdf.cell(w=150, h=25, txt=bill.period, ln=1)
        pdf.cell(w=100, h=25, txt="Total Bill: ")
        pdf.cell(w=150, h=25, txt=str(bill.amount),ln=1)

        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=25, txt=flatmate1.name + ':')
        pdf.cell(w=100, h=25, txt=flatmate1_pays, ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name + ':')
        pdf.cell(w=100, h=25, txt=flatmate2_pays)

        pdf.output(self.filename)
        webbrowser.open(self.filename)
