
from flat import Bill, Flatmate
from reports import PDF_Report, FileSharer




#client se interface
amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. December 2022:  ")


name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days {name1} did stay in the house during the bill period? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days {name2} did stay in the house during the bill period? "))

the_bill = Bill(amount=amount, period=period)
flatmate1=  Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f"{flatmate1.name}: ",flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{flatmate2.name}: ",flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PDF_Report(filename=f'{the_bill.period}.pdf')# give filename to pdf.output
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

# Get url to PDF file in cloud
file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())


