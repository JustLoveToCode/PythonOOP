from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmate import Bill
from flatmate import Flatmate

# It contains the string of the Current file:
# Instantiate the Flask class:
app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        # This is the template to render:
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)


class ResultsPage(MethodView):
    def post(self):
        billform = BillForm(request.form)
        amount = float(billform.amount.data)
        period = billform.period.data

        name1 = billform.name1.data
        day_in_house1 = float(billform.days_in_house1.data)

        name2 = billform.name2.data
        day_in_house2 = float(billform.days_in_house2.data)

        the_bill = Bill(amount, period)
        flatmate1 = Flatmate(name1, day_in_house1)
        flatmate2 = Flatmate(name2, day_in_house2)
        return render_template('results.html', name1=flatmate1.name,
                               amount1=flatmate1.pays(the_bill, flatmate2),
                               name2=flatmate2.name,
                               amount2=flatmate2.pays(the_bill, flatmate1))


class BillForm(Form):
    # Use the billform.amount.label:
    amount = StringField("Bill Amount:", default="100")
    # Use the billform.amount.label:
    period = StringField("Bill Period:", default="December 2020")

    name1 = StringField("Name:", default="John")
    days_in_house1 = StringField("Days in the House:", default=20)

    name2 = StringField("Name:", default="Mary")
    days_in_house2 = StringField("Days in the House:", default=12)

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))
app.run()
