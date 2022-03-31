from app import myapp_obj
from flask import render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
class LoginForm(FlaskForm):
	City_Name= StringField('City Name', validators=[DataRequired()])
	submit = SubmitField('Submit')
name = "Lisa"
city_names = ["Paris", "Rome", "London", "Tahiti"]
@myapp_obj.route("/", methods = ['POST' , 'GET'])
def home():
	form = LoginForm()
	if request.method == 'POST':
		result = request.form['City_Name']
		flash(result)
		return render_template('home.html', name = name,city_names = city_names,form=form, result = result)

	if request.method == 'GET':
		return render_template('home.html', name = name,city_names = city_names,form=form)

