import json


class User:
    # must force parse because google sheets is unreliable
    def __init__(
        self, id_num, name, elo, wins, losses
    ):
        self.id = str(id_num)
        self.name = str(name)
        self.elo = str(elo)
        self.wins = int(wins)
        self.losses = int(losses)

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "elo": self.elo,
            "wins": self.wins,
            "losses": self.losses,
        }

    def toRow(self):
        return [self.id, self.name, self.elo, self.wins, self.losses]

    def toString(self):
        return "id: " + str(self.id) + " name: " + self.name
