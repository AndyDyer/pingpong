from flask import request, Flask, jsonify
import json

from elo import rate_1vs1

import db
app = Flask(__name__)


# TODO:
#   * Add ids to the match data?
#   * Fix issue of id coming back as int. We have to cast it as string
#        everywhere and it is annoying and dangerous
#   * ELO library is questionable.... doesn't seem to be giving expected
#       results and seems like a lot for a simple calculation
#   * Error handling and messages
#   * Schema validation and legimate schemas
#   * Tests? Nah...
#   * Wrap up users and games in Classes?


@app.route('/start-game', methods=['GET'])
def start_game():
    player_1_id = request.args.get('player_1_id')
    player_2_id = request.args.get('player_2_id')

    zpDB = db.ZPPDB()
    users = zpDB.users

    if not verify_player(player_1_id, users):
        zpDB.register_user(player_1_id)
        users = zpDB.users
    if not verify_player(player_2_id, users):
        zpDB.register_user(player_2_id)
        users = zpDB.users

    player_data = {
        "player_1": [player for player in users if str(player["id"]) == player_1_id][0],
        "player_2": [player for player in users if str(player["id"]) == player_2_id][0]
    }

    return jsonify(player_data)


@app.route('/record-game', methods=['POST'])
def record_game():
    zpDB = db.ZPPDB()
    game_json = request.get_json()

    winner_id = str(determine_winner(game_json))
    winner_data, loser_data = update_player_data(game_json, winner_id)

    zpDB.update_players_post_game(winner_data, loser_data)
    zpDB.record_game(game_json)
    return


def verify_player(player_id, users):
    for user in users:
        if str(user["id"]) == player_id:
            return True
    return False


def determine_winner(match_json):
    player_1_wins = 0
    player_2_wins = 0

    games = match_json["games"]

    for game in games:
        if game["player_1_score"] > game["player_2_score"]:
            player_1_wins += 1
        else:
            player_2_wins += 1

    return (match_json["participants"]["player_1"]["id"]
            if player_1_wins > player_2_wins
            else match_json["participants"]["player_2"]["id"])


def update_player_data(match_json, winner_id):
    participants = match_json.get("participants")
    for key, value in participants.items():
        if str(value["id"]) == winner_id:
            winner_dict = value
        else:
            loser_dict = value

    winner_elo, loser_elo = rate_1vs1(winner_dict["elo"], loser_dict["elo"], drawn=False)

    winner_dict["history"] += 1
    loser_dict["history"] += 1

    winner_dict["wins"] += 1
    loser_dict["losses"] += 1

    winner_dict["elo"] = round(winner_elo)
    loser_dict["elo"] = round(loser_elo)

    return (winner_dict, loser_dict)
