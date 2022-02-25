from turtle import color
import webbrowser
from fpdf import FPDF


class Bill:
    """
      Class Bill represents a bill for each flatmate containing amount and the period
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Class Flatmate represents the person that live in a flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate):
        weight = self.days_in_house / \
            (self.days_in_house + flatmate.days_in_house)
        return bill.amount * weight


class PDFReport:
    """
    Creates a pdf report about the each flatmate has to pay for given period.
    """

    def __init__(self, filename="pdfreport.pdf"):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')

        flatmate1_pays = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pays = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf.add_page()
        pdf.image("house.png", w=40, h=40)

        pdf.set_font(family="Times", size=24, style='B')

        pdf.cell(w=0, h=100, txt="Flatmates Bill", align="C", ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period: ")
        pdf.cell(w=150, h=40, txt=bill.period, ln=1)

        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=25, txt=flatmate1.name + ':')
        pdf.cell(w=100, h=25, txt=flatmate1_pays, ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name + ':')
        pdf.cell(w=100, h=25, txt=flatmate2_pays)

        pdf.output(self.filename)
        webbrowser.open(self.filename)


bill = Bill(amount=100, period="Feb 2022")
lory = Flatmate(name="Lory", days_in_house=10)
john = Flatmate(name="John", days_in_house=20)

pdf_report = PDFReport()
pdf_report.generate(john, lory, bill)
