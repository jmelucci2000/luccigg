from flask import render_template, url_for, flash, redirect, request, session
from luccigg import app, db, api_key
from luccigg.forms import InsertSummoner, MatchmakeForm
from luccigg.classes import Summoner
import requests


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

def addSummonerDB(form_data):
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
    return summoner

@app.route("/add-summoner/<s>")
def addSumm(s):
    if "summoner1" not in session:
        session['summoner1'] = s
    elif "summoner2" not in session:
        session['summoner2'] = s
    elif "summoner3" not in session:
        session['summoner3'] = s
    elif "summoner4" not in session:
        session['summoner4'] = s
    elif "summoner5" not in session:
        session['summoner5'] = s
    elif "summoner6" not in session:
        session['summoner6'] = s
    elif "summoner7" not in session:
        session['summoner7'] = s
    elif "summoner8" not in session:
        session['summoner8'] = s
    elif "summoner9" not in session:
        session['summoner9'] = s
    elif "summoner10" not in session:
        session['summoner10'] = s
    return redirect(url_for('home'))

@app.route("/matchmake")
def matchmake():
    #sort players from highest to lowest.  Add highest to team 1, then add each next player to the team with the lowest rating.
    summoners = []
    summoners.append(Summoner.query.filter_by(eid=session['summoner1']).first())
    summoners.append(Summoner.query.filter_by(eid=session['summoner2']).first())
    summoners.append(Summoner.query.filter_by(eid=session['summoner3']).first())
    summoners.append(Summoner.query.filter_by(eid=session['summoner4']).first())
    summoners.append(Summoner.query.filter_by(eid=session['summoner5']).first())
    summoners.append(Summoner.query.filter_by(eid=session['summoner6']).first())
    summoners.append(Summoner.query.filter_by(eid=session['summoner7']).first())
    summoners.append(Summoner.query.filter_by(eid=session['summoner8']).first())
    summoners.append(Summoner.query.filter_by(eid=session['summoner9']).first())
    summoners.append(Summoner.query.filter_by(eid=session['summoner10']).first())
    summoners.sort(key=lambda summoner: summoner.mmr, reverse=True)
    Team1 = []
    Team2 = []
    Team1.append(summoners.pop(0))
    Team1mmr = Team1[0].mmr
    Team2mmr = 0
    while (len(summoners)>0):
        if len(Team2) < 5 and Team2mmr <= Team1mmr:
            Team2.append(summoners.pop(0))
            Team2mmr += Team2[-1].mmr
        elif len(Team1) < 5:
            Team1.append(summoners.pop(0))
            Team1mmr += Team1[-1].mmr
        else:
            Team2.append(summoners.pop(0))
            Team2mmr += Team2[-1].mmr
    summoners.clear()
    for i in range(0,5):
        summoners.append(Team1.pop(0))
        summoners.append(Team2.pop(0))
    return render_template('matchmake.html', summoners=summoners)

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    basei = url_for('static', filename='profile_pics/0.png')
    summoners = []
    if "summoner1" in session:
        summ = Summoner.query.filter_by(eid=session['summoner1']).first()
        summoners.append(summ)
    if "summoner2" in session:
        summ = Summoner.query.filter_by(eid=session['summoner2']).first()
        summoners.append(summ)
    if "summoner3" in session:
        summ = Summoner.query.filter_by(eid=session['summoner3']).first()
        summoners.append(summ)
    if "summoner4" in session:
        summ = Summoner.query.filter_by(eid=session['summoner4']).first()
        summoners.append(summ)
    if "summoner5" in session:
        summ = Summoner.query.filter_by(eid=session['summoner5']).first()
        summoners.append(summ)
    if "summoner6" in session:
        summ = Summoner.query.filter_by(eid=session['summoner6']).first()
        summoners.append(summ)
    if "summoner7" in session:
        summ = Summoner.query.filter_by(eid=session['summoner7']).first()
        summoners.append(summ)
    if "summoner8" in session:
        summ = Summoner.query.filter_by(eid=session['summoner8']).first()
        summoners.append(summ)
    if "summoner9" in session:
        summ = Summoner.query.filter_by(eid=session['summoner9']).first()
        summoners.append(summ)
    if "summoner10" in session:
        summ = Summoner.query.filter_by(eid=session['summoner10']).first()
        summoners.append(summ)
    if len(summoners) == 10:
        matchmakeform = MatchmakeForm()
        if matchmakeform.validate_on_submit():
            return redirect(url_for('matchmake'))
        return render_template('home.html', form=matchmakeform, basei=basei, summoners=summoners, size=len(summoners))
    form = InsertSummoner()
    if form.validate_on_submit():
        s = addSummonerDB(form.summoner.data)
        return redirect(url_for('addSumm', s=s.eid))
    return render_template('home.html', form=form, basei=basei, summoners=summoners, size=len(summoners))


