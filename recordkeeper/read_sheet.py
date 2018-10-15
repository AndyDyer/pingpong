import gspread
from oauth2client.service_account import ServiceAccountCredentials

from user import User

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('zpp_secret.json', scope)

client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
user_table = client.open("ZPP DB").get_worksheet(0)
game_table = client.open("ZPP DB").get_worksheet(1)

# Extract and print all of the values
list_of_user_hashes = user_table.get_all_records()
list_of_game_hases = game_table.get_all_records()


# for user in list_of_user_hashes:
#   player1 = User(user['phone'], user['name'], user['elo'], user['wins'], user['losses'], user['history'])

print(list_of_user_hashes)
print(list_of_game_hases)