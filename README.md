# luccigg
A python webapp built upon Flask, Bootstrap, and SQLAlchemy.  Functions as a League of Legends team balancer, where webapp users can search and add 10 existing summoners to their session and matchmake to balance the teams.  Summoner information is gathered via Riot Games api and added into a SQLAlchemy database.

For this app to work, you must set api_key in __init__.py to a valid Riot Games api key.  Session data is removed when a user closes the browser.  Search functionality at the top bar is currently not implemented.

Planned: Graphical improvements to matchmaking button, team layout, etc.  Adding a remove button once a Summoner has been entered.  Add search functionality and summoner profile pages.  Adding role preference.

Enjoy!