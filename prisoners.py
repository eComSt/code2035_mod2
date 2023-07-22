from collections import Counter

class player:
    def __init__(self,model):
        self.model = model
        self.history = []

class Cheater(player):
    def step(self):
        return False

class Cooperator(player):
    def step(self):
        return True

class Copycat(player):
    def step(self):
        return True if not self.history else self.history[-1]


class Game(object):

    def __init__(self, matches=1000):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        for _ in range(self.matches):
            ans1,ans2 = player1.step(),player2.step()
            if ans1 and ans2:
                self.registry[player1.model]+=2
                self.registry[player2.model]+=2
            elif not ans1 and ans2:
                self.registry[player1.model]+=3
                self.registry[player2.model]-=1
            elif not ans2 and ans1:
                self.registry[player2.model]+=3
                self.registry[player1.model]-=1

            player2.history.append(ans1)
            player1.history.append(ans2)

        player2.history = []
        player1.history = []

g = Game(matches=100000)
g.play(Cooperator("Cooperator"),Copycat("Copycat"))
for i in g.registry:
    print(i,g.registry[i])