import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contain data about the bill, such as total amount
    and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create the Flatmate person who lived in the flat
    and pay the share of the total bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """Create the PDF File that Contain the
    Data about the Flatmates such as their name
    and the due amount and the period of the bill"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        # Creating the Orientation and the unit in the pdf:
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        # Use the add_page() method here:
        pdf.add_page()
        # Add the Icon Here
        pdf.image(name="house.png", w=50, h=50)
        # Setting the font here:
        # Setting the title:
        pdf.set_font(family="Times", size=24, style="B")
        # Insert Period Label and the Value:
        # This will take the Entire Horizontal Length by setting the
        # width to be 0:
        pdf.cell(w=0, h=80, txt="Flatmate Bill", border=0, align="C", ln=1)

        pdf.set_font(family="Times", size=20, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
        # Insert name and the due amount of the first flatmate:
        pdf.set_font(family="Times", size=20)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=200, h=40, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and the due amount of the first flatmate:
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=200, h=40, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)


bill_amount = float(input("Hey User, Enter the Bill Amount"))
bill_period = input("What is the Bill Period? E.g December 2020.")
print("This Bill Amount is ", bill_amount)
print("The period is", bill_period)

name1 = input("What is your name?")
days_in_house1 = int(input(f"How many days did {name1} stayed in the house"))

name2 = input("What is the name of the other flatmate?")
days_in_house2 = int(input(f"How many days did {name2} stayed in the house"))

# Creation of the Object:
the_bill = Bill(amount=bill_amount, period=bill_period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f" {flatmate1.name} pays", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{flatmate2.name} pays", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
