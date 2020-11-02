from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from luccigg import api_key
from luccigg.classes import Summoner
import requests
import json

# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators = [DataRequired(), Length(min=2, max=20)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = Password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')

# class InsertSummoner(FlaskForm):
# #     summoner1 = StringField('Summoner 1', validators=[DataRequired(), Length(min=3, max=16)])
# #     summoner2 = StringField('Summoner 2', validators=[DataRequired(), Length(min=3, max=16)])
# #     summoner3 = StringField('Summoner 3', validators=[DataRequired(), Length(min=3, max=16)])
# #     summoner4 = StringField('Summoner 4', validators=[DataRequired(), Length(min=3, max=16)])
# #     summoner5 = StringField('Summoner 5', validators=[DataRequired(), Length(min=3, max=16)])
# #     summoner6 = StringField('Summoner 6', validators=[DataRequired(), Length(min=3, max=16)])
# #     summoner7 = StringField('Summoner 7', validators=[DataRequired(), Length(min=3, max=16)])
# #     summoner8 = StringField('Summoner 8', validators=[DataRequired(), Length(min=3, max=16)])
# #     summoner9 = StringField('Summoner 9', validators=[DataRequired(), Length(min=3, max=16)])
# #     summoner10 = StringField('Summoner 10', validators=[DataRequired(), Length(min=3, max=16)])
# #     submit = SubmitField('Join')

class InsertSummoner(FlaskForm):
    summoner = StringField('Summoner 1', validators=[DataRequired(), Length(min=3, max=16)])
    submit = SubmitField('Add')
    def validate_summoner(self, summoner):
        response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner.data + "?api_key=" + api_key)
        if 'status' in response.json():
            raise ValidationError("Summoner does not exist on NA server.")


