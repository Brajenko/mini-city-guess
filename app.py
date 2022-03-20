from email.mime import image
from tkinter import image_names
from flask import Flask, render_template, redirect
from city_images import CityChecker
import random

from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired


class GuessCityForm(FlaskForm):
    city_name = StringField('Название города', validators=[DataRequired()])
    submit = SubmitField('Подтвердить')


app = Flask(__name__)
app.config['SECRET_KEY'] = '0'
checker = CityChecker()


@app.route('/',  methods=['GET', 'POST'])
def index():
    form = GuessCityForm()
    fail = False

    if form.validate_on_submit():
        print(form.city_name.data)
        if checker.check_city(form.city_name.data):
            city, img = checker.get_new_city()
            
            if not city:
                checker.restart()
                
                return render_template('fin.html')
            
        else:
            fail = True
            city, img = checker.get_curr_city()
    
    else: 
        city, img = checker.get_curr_city()
        print(city, img)

    return render_template('index.html', image_name=img, fail=fail, form=form)


@app.route('/all_cities')
def all_cities():
    return


if __name__ == '__main__':
    app.run(debug=True)