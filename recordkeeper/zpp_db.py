import gspread
from oauth2client.service_account import ServiceAccountCredentials

from db_helpers import getGamesDict, getUserDict, getMatchesDict

class ZPPDB: 
  def __init__(self):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('zpp_secret.json', scope)
    self.client = gspread.authorize(creds)
    self.users = getUserDict(self)
    self.games = getGamesDict(self)
    self.matches = getMatchesDict(self)
    


def main(): ## tester
  theDB = ZPPDB()
  print(theDB.users)
  print(theDB.games)
  print(theDB.matches)

main()