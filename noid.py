from ignes import RoomIgnes
from helper import Helper
from enemy import Enemy
from battle import Battle
from common import line,select

class NoidHelper(Helper):
    def __init__(self):
        super().__init__("ノイド")

    def action(self,user,target):
        line()
        input(f"{self.name}は立っている")

class NoidEnemy(Enemy):
    def __init__(self):
        super().__init__("ノイド",10,1,1)

    def action(self,player):
        line()
        input(f"{self.name}は立っている")

class Noid(RoomIgnes):
    def __init__(self,_):
        super().__init__("ノイド")
        self.isRoom = True
        self.noid_helper = None

    def com(self,player):
        if self.isRoom:
            line()
            print("ノイド「やぁ」")
            line()
            ac = {1:("仲間にする",self.helper),2:("戦う",self.battle)}
        else:
            line()
            print("ノイド「ぼくの部屋だ」")
            line()
            ac = {1:("部屋に戻す",self.roomBack)}
        for i,(v,_) in ac.items():
            print(f"{i}:{v}")
        print("0:戻る")
        ans = select(len(ac),["0"])
        if ans == "0":
            line()
            input(f"{player.name}は部屋を出た")
        else:
            ac[int(ans)][1](player)

    def helper(self,player):
        line()
        print("ノイド「よろしくね～」")
        self.noid_helper = NoidHelper()
        player.addHelper(self.noid_helper)
        self.isRoom = False

    def battle(self,player):
        line()
        print("ノイド「えぇー！なんでー！？」")
        battle = Battle(player,NoidEnemy())
        battle.start()

    def roomBack(self,player):
        line()
        print("ノイド「ばいば～い」")
        input("ノイドは部屋に戻った")
        player.removeHelper(self.noid_helper)
        self.isRoom = True
