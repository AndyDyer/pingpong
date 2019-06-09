import gspread
from elo import rate_1vs1
from oauth2client.service_account import (
    ServiceAccountCredentials,
)
from user import User
from match import Match

scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "zpp_secret.json", scope
)


class ZPPDB:
    def __init__(self):
        self.client = gspread.authorize(creds) 
        self.user_sheet = self.client.open("zpp_db").get_worksheet(0)
        self.match_sheet = self.client.open("zpp_db").get_worksheet(1)
        self.users = self.getUserDict()
        self.matches = self.getMatchesList()

    def recordMatch(self, **kwargs):
        match = Match(
            player1_id=kwargs.get("player1_id"),
            player2_id=kwargs.get("player2_id"),
            games=kwargs.get("games"),
        )
        # 2 to preserve headers
        self.match_sheet.insert_row(match.toRow(), 2)
        self.settleScore(match)
        return match.toDict()

    def settleScore(self, match):
        self.updateElo(match.winner, match.loser)
        self.users[match.winner].wins += 1
        self.users[match.loser].losses += 1

        self.updateUser(self.users[match.winner])
        self.updateUser(self.users[match.loser])

    def updateUser(self, user):
        user_range = self.getUserRange(user.id)

        for cell, row_value in zip(user_range, user.toRow()):
            cell.value = row_value

        self.user_sheet.update_cells(user_range)

    def getUserRange(self, user_id):
        id_list = self.user_sheet.col_values(1)
        row = id_list.index(user_id) + 1
        return self.user_sheet.range('A{row}:E{row}'.format(row=row))

    def updateElo(self, winner_id, loser_id):
        winner = self.users[winner_id]
        loser = self.users[loser_id]

        new_elos = rate_1vs1(winner.elo, loser.elo)

        winner.elo = int(round(new_elos[0]))
        loser.elo = int(round(new_elos[1]))
        
    def getUserDict(self):
        users = {}
        user_records = self.user_sheet.get_all_records()

        for user in user_records:
            users[str(user["id"])] = User(
                user["id"],
                user["name"],
                user["elo"],
                user["wins"],
                user["losses"]
            )
        return users

    def getMatchesList(self):
        matches = []
        match_table = self.client.open("zpp_db").get_worksheet(1)
        match_records = match_table.get_all_records()

        for match in match_records:
            print(match)
            matches.append(Match(
                games=match["games"],
                winner=match["winner"],
                loser=match["loser"]
            ))

        return matches
