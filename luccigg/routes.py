from flask import render_template, url_for, flash, redirect, request
from luccigg import app, db, api_key
from luccigg.forms import InsertSummoner
from luccigg.classes import Summoner
import requests
import json


def mmrconvert1(rank):
    # assume unranked mmr is equivalent to silver
    if rank == "IRON":
        return 100
    elif rank == "BRONZE":
        return 200
    elif rank == "SILVER":
        return 300
    elif rank == "GOLD":
        return 400
    elif rank == "PLATINUM":
        return 500
    elif rank == "DIAMOND":
        return 600
    elif rank == "MASTER":
        return 700
    elif rank == "GRANDMASTER":
        return 750
    elif rank == "CHALLENGER":
        return 800
    else:
        return 300 # unranked players are treated as silver

def mmrconvert2(division):
    if division == "I":
        return 80
    elif division == "II":
        return 60
    elif division == "III":
        return 40
    elif division == "IV":
        return 20
    else:
        return 0

def addSummoner(form_data):
    summoner = Summoner.query.filter_by(username=form_data).first()
    if not summoner:
        response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str(form_data) + "?api_key=" + api_key)
        sname = form_data
        eid = response.json()['id']
        pid = response.json()['profileIconId']
        picture = str(pid) + ".png"
        response2 = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + eid + "?api_key=" + api_key)
        if (response2.json()):
            mmr = 0
            for d in response2.json():
                sum = mmrconvert1(d['tier'])
                if d['tier'] != 'MASTER' and d['tier'] != 'GRANDMASTER' and d['tier'] != 'CHALLENGER':
                    sum += mmrconvert2(d['rank'])
                    if sum > mmr:
                        mmr = sum
                        rank = d['tier'] + " " + d['rank']
                else:
                    if sum > mmr:
                        mmr = sum
                        rank = d['tier']
        else:
            mmr = 300
            rank = "UNRANKED"
        summoner = Summoner(eid=eid, username=sname, pid=pid, summoner_icon=picture, rank=rank, mmr=mmr)
        db.session.add(summoner)
        db.session.commit()
    flash('Summoner added!', 'success')
    return summoner


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home(s1=None, s2=None, s3=None, s4=None, s5=None, s6=None, s7=None, s8=None, s9=None, s10=None, i1=None, i2=None, i3=None, i4=None, i5=None, i6 =None, i7=None, i8=None, i9=None, i10=None):
    if not s1:
        form1 = InsertSummoner()
    else:
        form1 = None
    # form2 = InsertSummoner()
    # form3 = InsertSummoner()
    # form4 = InsertSummoner()
    # form5 = InsertSummoner()
    # form6 = InsertSummoner()
    # form7 = InsertSummoner()
    # form8 = InsertSummoner()
    # form9 = InsertSummoner()
    # form10 = InsertSummoner()
    if form1.validate_on_submit():
        s1 = addSummoner(form1.summoner.data)
        i1 = url_for('static', filename='profile_pics/' + s1.summoner_icon)
        return home(s1=s1, i1=i1)
    # if form1.validate_on_submit():
    #     s2 = addSummoner(form1.summoner.data)
    # if form1.validate_on_submit():
    #     s3 = addSummoner(form1.summoner.data)
    # if form1.validate_on_submit():
    #     s4 = addSummoner(form1.summoner.data)
    # if form1.validate_on_submit():
    #     s5 = addSummoner(form1.summoner.data)
    # if form1.validate_on_submit():
    #     s6 = addSummoner(form1.summoner.data)
    # if form1.validate_on_submit():
    #     s7 = addSummoner(form1.summoner.data)
    # if form1.validate_on_submit():
    #     s8 = addSummoner(form1.summoner.data)
    # if form1.validate_on_submit():
    #     s9 = addSummoner(form1.summoner.data)
    # if form1.validate_on_submit():
    #     s10 = addSummoner(form1.summoner.data)
    # return render_template('home.html', form1=form1, form2=form2, form3=form3, form4=form4, form5=form5, form6=form6, form7=form7, form8=form8, form9=form9, form10=form10, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10)
    if not i1:
        i1 = url_for('static', filename='profile_pics/0.png')
    if not i2:
        i2 = url_for('static', filename='profile_pics/0.png')
    if not i3:
        i3 = url_for('static', filename='profile_pics/0.png')
    if not i4:
        i4 = url_for('static', filename='profile_pics/0.png')
    if not i5:
        i5 = url_for('static', filename='profile_pics/0.png')
    if not i6:
        i6 = url_for('static', filename='profile_pics/0.png')
    if not i7:
        i7 = url_for('static', filename='profile_pics/0.png')
    if not i8:
        i8 = url_for('static', filename='profile_pics/0.png')
    if not i9:
        i9 = url_for('static', filename='profile_pics/0.png')
    if not i10:
        i10 = url_for('static', filename='profile_pics/0.png')
    if s1:
        print("yay")
    return render_template('home.html', form1=form1, s1=s1, i1=i1)
