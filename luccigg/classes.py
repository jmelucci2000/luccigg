# Compute the average rating of the players, avg = mean(pool)
# Compute the target score for a team of 5: team_target = 5*avg
# Find the combination of 5 players whose ratings have a sum closest to team_target (solved in several other postings). Make that team1.
# Compute total rating of the team: team1_rating = sum(team1)
# Remove those five players from the pool. Put the remaining pool players onto team2.
# Compute the rating of this remaining team of 4: team2_rating = sum(team2)
# Subtract the ratings to get the rating of the needed 10th player: player_target = team1_rating - team2_rating
# Grab the next 10 players in the queue; this is the new pool.
# Find the pool player with the rating closest to player_target.
# Put that player onto team2 and post the match **team1 vs team2*.
# There are 9 players left in the pool; go back to step 1. Iterate as necessary.
#
from luccigg import db


class Summoner(db.Model):
    eid = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    pid = db.Column(db.Integer, nullable=False)
    summoner_icon = db.Column(db.String(20), nullable=False, default='default.jpg')
    rank = db.Column(db.String(60), nullable=False)
    mmr = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"Summoner('{self.username}')"
    def to_json(self):
        return {
            "eid": self.eid,
            "username": self.username,
            "pid": int(self.pid),
            "summoner_icon": self.summoner_icon,
            "rank": self.rank,
            "mmr": int(self.mmr),
        }












