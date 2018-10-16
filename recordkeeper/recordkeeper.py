from flask import request, Flask, jsonify
import json 

import db
app = Flask(__name__)

@app.route('/start-game', methods=['GET'])
# http://127.0.0.1:5000/start-game?player1id=123&player2id=321
def startGame():
  zpDB = db.ZPPDB()
  player1id = request.args.get('player1id')
  player2id = request.args.get('player2id')

  player1 = zpDB.users[player1id]
  player2 = zpDB.users[player2id]

  #if key error register user with blank elo and name as UNKNOWN
  # on client if name === UNKNOWN show a message to have them dm andy dyer to update

  data = {
    'player1': player1.toDict(),
    'player2': player2.toDict(),
  }
  return jsonify(data)