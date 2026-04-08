from ignes import RoomIgnes
from common import line

class Kyombie(RoomIgnes):
    def __init__(self,center):
        super().__init__("キョンビ")
        self.center = center

    def com(self,player):
        line()
        print("キョンビ「キョンビだぞ～」")
        input(f"{player.name}は部屋を出た")
        self.center.setFlag("isKyombie")
