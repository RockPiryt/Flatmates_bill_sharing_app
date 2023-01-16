import webbrowser
from fpdf import FPDF
import os 
from filestack import Client


class PDF_Report():
    '''
    Creates a PDF file that contains data about the flatmates 
    such as their names, their due amount and the period of the bill.
    '''

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay=str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pay=str(round(flatmate2.pays(bill, flatmate1),2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #add image
        pdf.image("files/house.png", w=30, h=30)

        #Insert title
        pdf.set_font(family="Arial", size=24, style="B")
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        #insert period label and value
        # pdf.add_font('Arial', '', 'c:/windows/fonts/arial.ttf', uni=True)
        pdf.set_font(family="Arial", size=14, style="B")
        pdf.cell(w=100, h=40, txt='Period:', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        #insert name and due amount of the flatmate1
        # pdf.add_font('Arial', '', 'c:/windows/fonts/arial.ttf', uni=True)
        pdf.set_font(family="Arial", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=1, ln=1)

        #insert name and due amount of the flatmate2
        # pdf.add_font('Arial', '', 'c:/windows/fonts/arial.ttf', uni=True)
        pdf.set_font(family="Arial", size=12)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=1, ln=1)




        #change directory to files, generate and open the PDF
        os.chdir("files")#change working directory from flatmates_bill_sharing_app (the same as reports.py) to 
        # new directory flatmates_bill_sharing_app/files

        pdf.output(self.filename)
        # pdf.output(f"files/{self.filename}")

        #auto open pdf file
        webbrowser.open(self.filename)


class FileSharer():
    '''
    Uploud PDF to cloud Filestack python. It return url to PDF file.
    '''

    def __init__(self, filepath, api_key="AcQvJqywtQRO10tNKuodvz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url