from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
 
myobj = Flask(__name__)
myobj.config['SECRET_KEY'] = 'Password' 
from app import routes
