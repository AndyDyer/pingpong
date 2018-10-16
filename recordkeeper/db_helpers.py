from user import User
from match import Match

def getUserDict(db):
    users = {}
    user_table = db.client.open("ZPP DB").get_worksheet(0)
    user_records = user_table.get_all_records()

    for user in user_records:
      users[str(user['phone'])] = User(user['phone'], 
                                      user['name'],
                                      user['elo'],
                                      user['wins'],
                                      user['losses'],
                                      user['history'])
    return users

def getMatchesDict(db):
  matches = {}
  match_table = db.client.open("ZPP DB").get_worksheet(1)
  match_records = match_table.get_all_records()

  
  return match_records
