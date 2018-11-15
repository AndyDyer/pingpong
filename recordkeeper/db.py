import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json


class ZPPDB:
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('zpp_secret.json', scope)
        self.client = gspread.authorize(creds)
        self.users = self._get_zpp_worksheet(0).get_all_records()
        self.games = self._get_zpp_worksheet(1).get_all_records()


    # All of our "tables" are worksheets within the same spreadsheet. This is
    # boilerplate for getting a worksheet.
    # Worksheet 0 is users-sheet
    # WWorksheet 1 is games-sheet
    def _get_zpp_worksheet(self, worksheet_index):
        FILE_ID = '1bu2InCVsjRLolpSQoMoT8c5rBu-gWowIG6GWKJw9PeM'
        spreadsheet = self.client.open_by_key(FILE_ID)
        worksheet = spreadsheet.get_worksheet(worksheet_index)
        return worksheet


    # We add two to account for discrepancy between list and
    # spreadsheet indexing as well as our header row.
    def _find_empty_row(self, worksheet):
        return len(worksheet) + 2


    def register_user(self, user_id):
        first_empty_row = self._find_empty_row(self.users)
        new_user_values = [user_id, "UNKNOWN", 0, 0, 0, 0]
        user_sheet = self._get_zpp_worksheet(0)
        user_sheet.insert_row(new_user_values, first_empty_row)
        self.users = user_sheet.get_all_records()   # Update class property to reflect changes
        return


    def record_game(self, game_dict):
        first_empty_row = self._find_empty_row(self.games)
        game_sheet = self._get_zpp_worksheet(1)
        finished_game_values = [first_empty_row - 1,    # Game index
                                json.dumps(game_dict.get("games")),    # List of Matches in Game
                                game_dict.get("league") ]
        game_sheet.insert_row(finished_game_values, first_empty_row)
        self.games = game_sheet.get_all_records()   # Update class property to reflect changes
        pass


    def update_players_post_game(self, player_1_data, player_2_data):
        user_sheet = self._get_zpp_worksheet(0)
        headers = user_sheet.row_values(1)

        player_1_row_index = user_sheet.find(str(player_1_data["id"])).row
        player_2_row_index = user_sheet.find(str(player_2_data["id"])).row

        player_1_range_string = "A{}:F{}".format(player_1_row_index, player_1_row_index)
        player_2_range_string = "A{}:F{}".format(player_2_row_index, player_2_row_index)

        player_1_cell_list = user_sheet.range(player_1_range_string)
        player_2_cell_list = user_sheet.range(player_2_range_string)

        for index in range(len(headers)):
            col_name = headers[index]
            player_1_cell = player_1_cell_list[index]
            player_1_cell.value = player_1_data.get(col_name)
            player_2_cell = player_2_cell_list[index]
            player_2_cell.value = player_2_data.get(col_name)

        user_sheet.update_cells(player_1_cell_list)
        user_sheet.update_cells(player_2_cell_list)
        return
