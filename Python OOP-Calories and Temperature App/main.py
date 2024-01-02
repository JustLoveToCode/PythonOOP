import requests
from bs4 import BeautifulSoup
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

# Instantiating the Flask:
app = Flask(__name__)


# This is the get method for getting the Website Page:
class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):
    def get(self):
        calories_form = CaloriesForm()
        return render_template("calories_form_page.html",
                               caloriesform=calories_form)

    def post(self):
        # Getting the data for the CaloriesForm class:
        calories_form = CaloriesForm(request.form)

        temperature = Temperature(country=calories_form.country.data,
                                  city=calories_form.city.data).get()

        calorie = Calorie(weight=float(calories_form.weight.data),
                          height=float(calories_form.height.data),
                          age=float(calories_form.age.data),
                          temperature=temperature)

        # Invoking the Calories class calculate method:
        calories = calorie.calculate()

        return render_template('calories_form_page.html',
                               caloriesform=calories_form,
                               calories=calories,
                               result=True)


class Calorie:
    """Represent the Optimal Calories Amount the person
    need to take"""

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        print("Type", type(self.temperature))
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result


class Temperature:
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    base_url = 'https://www.timeanddate.com/weather/'

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        url = f"{self.base_url}{self.country}/{self.city}"
        print(url)
        return url

    def _scrape(self):
        url = self._build_url()
        r = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        # Replacing the Following div and the class to get the Particular element:
        temperature_element = soup.find('div', {'class': 'h2'})
        print("Temperature Element:", temperature_element)
        # List Comprehension here:
        temperature = temperature_element.text.strip() if temperature_element else None
        print("Scraped Temperature:", temperature)
        return temperature

    def get(self):
        scraped_content = self._scrape()
        print(scraped_content)
        if scraped_content:
            float_conversion = float(scraped_content.replace("°C", ""))
            print("Float Conversion", float_conversion)
            return float_conversion
        else:
            return None


class CaloriesForm(Form):
    weight = StringField("Weight:", default=70)
    height = StringField("Height:", default=175)
    age = StringField("Age:", default=32)
    country = StringField("Country:", default="usa")
    city = StringField("City:", default="new york")
    button = SubmitField('Calculate')


if __name__ == "__main__":
    # input_weight = float(input("What is your weight in kg"))
    # input_height = float(input("What is your height in cm"))
    # input_age = float(input("What is your age?"))
    # input_country = input("What country do you live in?").lower()
    # input_city = input("What city do you live in?").lower()
    temperature = Temperature(country="usa", city="new york")
    print(f"Temperature Here: {temperature.get()}°C")

app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form',
                 view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)
