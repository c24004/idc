from common import line,prob
import random

class Event:
    def __init__(self):
        self.ignesList = []

    def addIgnes(self,ignes):
        if ignes not in self.ignesList:
            self.ignesList.append(ignes)

    def action(self,player):
        if self.ignesList and prob(30):
            line()
            print("---イベント発生---")
            line()
            input("(確認)")
            ignse = random.choice(self.ignesList)
            ignse.action(player)
