import json
class User:
  #must force parse because google sheets is unreliable
  def __init__(self, phone, name, elo, wins, losses, history):
        self.id = str(phone)
        self.name = str(name)
        self.elo = str(elo)
        self.wins = int(wins)
        self.losses = int(losses)
        self.history = str(history).split(',')
  
  def toDict(self):
        return {
          'id': self.id,
          'name': self.name,
          'elo': self.elo,
          'wins': self.wins,
          'losses': self.losses,
        }

  def toString(self):
        return "id: " + str(self.id) + " name: " + self.name