from bill import Bill
from pdfreport import PDFReport
from flatmate import Flatmate

print()
amount = float(input("Hey user, Enter the bill amount: "))
period = input("Enter the bill period, i.e., (Feb 2022): ")
bill = Bill(amount, period)

print()
flatmate1_name = input("Enter first flatmate's name: ")
flatmate1_days_in_house = int(
    input("Enter the days he/she lived in the house during the bill period: "))

print()
flatmate2_name = input("Enter second flatmate's name: ")
flatmate2_days_in_house = int(
    input("Enter the days he/she lived in the house during the bill period: "))

flatmate1 = Flatmate(flatmate1_name, flatmate1_days_in_house)
flatmate2 = Flatmate(flatmate2_name, flatmate2_days_in_house)

pdf_report = PDFReport()
pdf_report.generate(flatmate1, flatmate2, bill)

print()
print("Bill report has been generated...")
