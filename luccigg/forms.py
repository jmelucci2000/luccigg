from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from luccigg import api_key
import requests


class InsertSummoner(FlaskForm):
    summoner = StringField('Summoner', validators=[DataRequired(), Length(min=3, max=16)])
    submit = SubmitField('Add')
    def validate_summoner(self, summoner):
        response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner.data + "?api_key=" + api_key)
        if 'status' in response.json():
            raise ValidationError("Summoner does not exist on NA server.")

class MatchmakeForm(FlaskForm):
    msubmit = SubmitField('Matchmake!')


