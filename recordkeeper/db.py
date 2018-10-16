import gspread
from oauth2client.service_account import ServiceAccountCredentials

from db_helpers import getUserDict, getMatchesDict

class ZPPDB: 
  def __init__(self):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('zpp_secret.json', scope)
    self.client = gspread.authorize(creds)
    self.users = getUserDict(self)
    self.matches = getMatchesDict(self)
    
  #def registerUser(id):
    #register user with name 'UNKNOWN' 1000

    #make an update user function
    # 







# def main(): ## tester
#   theDB = ZPPDB()
#   print(theDB.users)
#   print(theDB.matches)

# main()

# TODO add 
