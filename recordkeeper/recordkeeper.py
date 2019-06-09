from flask import request, Flask, jsonify
from flask_cors import CORS, cross_origin
import json

import db

app = Flask(__name__)
CORS(app)

@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
@app.route("/start-game", methods=["GET"])
# http://127.0.0.1:5000/start-game?player1ID=123&player2ID=321
def startGame():
    zpp_db = db.ZPPDB()

    player1id = request.args.get("player1ID")
    player2id = request.args.get("player2ID")

    player1 = zpp_db.users[player1id]
    player2 = zpp_db.users[player2id]

    return jsonify({
        "player1": player1.toDict(),
        "player2": player2.toDict(),
    })


@app.route("/matches", methods=["GET"])
def getMatches():
    zpp_db = db.ZPPDB()
    matches = []
    for match in zpp_db.matches:
        matches.append(match.toDict())
    return jsonify(matches)


@app.route("/users", methods=["GET"])
def getUsers():
    zpp_db = db.ZPPDB()
    users = []
    for user in zpp_db.users.values():
        users.append(user.toDict())
    return jsonify(users)


@app.route(
    "/record-game", methods=["post"]
)  # TODO change to post later for semantic reasons
# http://127.0.0.1:5000/record-game?player1id=123&player2id=321&games=%5B%2711%3A2%27%2C%20%2711%3A4%27%2C%20%273%3A11%27%2C%20%2711%3A10%27%5D
def recordGame():
    zpp_db = db.ZPPDB()

    id_1 = request.args.get("player1id")
    id_2 = request.args.get("player2id")
    games = request.args.get("games").split(",")

    return jsonify(
        zpp_db.recordMatch(
            player1_id=id_1, player2_id=id_2, games=games
        )
    )

