class Match:
    def __init__(self, **kwargs):
        self.games = kwargs.get("games")
        if not kwargs.get("winner"):
            self.determineWinner(
                self.games,
                kwargs.get("player1_id"),
                kwargs.get("player2_id"),
            )
        else:
            self.winner = kwargs.get('winner')
            self.loser = kwargs.get('loser')

    def toDict(self):
        return {
            "games": self.games,
            "winner": str(self.winner),
            "loser": str(self.loser)
        }

    def toRow(self):
        return [''.join(self.games), self.winner, self.loser]

    def determineWinner(self, games_list, player1_id, player2_id):
        player1_wins = 0
        player2_wins = 0
        for game in games_list:
            scores = game.split(":")
            if scores[0] < scores[1]:
                player1_wins += 1
            else:
                player2_wins += 1
            if player1_wins > player2_wins:
                self.winner = player1_id
                self.loser = player2_id
            else:
                self.winner = player2_id
                self.loser = player1_id

my_match = Match(games=['11:2'], player1_id='123', player2_id='432')
