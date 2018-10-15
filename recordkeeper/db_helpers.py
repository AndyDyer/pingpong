from user import User
from game import Game
from match import Match

def getUserDict(db):
    users = {}
    user_table = db.client.open("ZPP DB").get_worksheet(0)
    user_records = user_table.get_all_records()

    for user in user_records:
      users[user['phone']] = User(user['phone'], 
                               user['name'],
                               user['elo'],
                               user['wins'],
                               user['losses'],
                               user['history'])

    return users

def getGamesDict(db):
  games = {}
  game_table = db.client.open("ZPP DB").get_worksheet(1)
  game_records = game_table.get_all_records()

  for game in game_records:
    games[str(game['id'])] = Game(game['id'],
                             game['player1'],
                             game['player2'],
                             game['result'],
                             game['score'])

  return games

def getMatchesDict(db):
  gamesDict = db.games
  matches = {}
  match_table = db.client.open("ZPP DB").get_worksheet(2)
  match_records = match_table.get_all_records()

  for match in match_records:
    games = []
    games_played = match['games'].split(',')
    for gameId in games_played:
      games.append(gamesDict[gameId])
    matches[match['id']] = Match(match['id'], games, match['league'])
  return matches