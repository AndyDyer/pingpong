
class User:

  def __init__(self, phone, name, elo, wins, losses, history):
        self.id = phone
        self.name = name
        self.elo = elo
        self.wins = wins
        self.losses = losses
        self.history = str(history).split(',')