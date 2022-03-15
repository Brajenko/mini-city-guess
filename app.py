from flask import Flask, render_template, redirect
from city_images import get_image_of_city
import random

app = Flask(__name__)
cities = ['Москва', 'Санкт-Петербург']

@app.route('/')
def index():
    img = get_image_of_city(random.choice(cities))
    return render_template('index.html', image_name=img)

@app.route('/all_cities')
def all_cities():
    return


if __name__ == '__main__':
    app.run(debug=True)