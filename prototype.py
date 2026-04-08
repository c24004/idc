from ignes import RoomIgnes
from helper import Helper
from enemy import Enemy
from battle import Battle
from common import line,select

class PrototypeEnemy(Enemy):
    def __init__(self):
        super().__init__("プロトタイプ",10,100,100)
        self.chargeCount = 0

    def action(self,player):
        line()
        self.chargeCount += 1
        if self.chargeCount == 1:
            input("プロトタイプ「システム再機動」")
        elif self.chargeCount == 2:
            input("プロトタイプ「エネルギー充填中」")
        elif self.chargeCount == 3:
            input("プロトタイプ「チャージ完了」")
        elif self.chargeCount == 4:
            input("プロトタイプ「ターゲットロックオン」")
        else:
            print("プロトタイプ「アルティメットキャノン法、発射！」")
            player.damage(self.at)
            self.chargeCount = 0

class PrototypeHelper(Helper):
    def __init__(self):
        super().__init__("プロトタイプ")
        self.chargeCount = 0

    def action(self,user,target):
        line()
        self.chargeCount += 1
        if self.chargeCount == 1:
            input("プロトタイプ「マズハボタンヲ押シテクダサイ」")
        elif self.chargeCount == 2:
            input("プロトタイプ「次ニレバーヲ引イテクダサイ」")
        else:
            print("プロトタイプ「チャージ完了！」")
            input("プロトタイプ「アルティメットキャノン法、発射！」")
            target.damage(100)
            self.systemDown()

    def systemDown(self):
        self.chargeCount = 0

class Prototype(RoomIgnes):
    def __init__(self,_):
        super().__init__("プロトタイプ")
        self.isRoom = True
        self.prototype_helper = PrototypeHelper()

    def com(self,player):
        if self.isRoom:
            line()
            print("プロトタイプ「ドウモ」")
            line()
            ac = {1:("仲良くする",self.helper),2:("戦う",self.battle)}
        else:
            line()
            print("どうする？")
            line()
            ac = {1:("部屋に戻す",self.roomBack)}
        for i,(v,_) in ac.items():
            print(f"{i}:{v}")
        print("0:戻る")
        line()
        ans = select(len(ac),["0"])
        if ans == "0":
            line()
            input(f"{player.name}は部屋を出た")
        else:
            ac[int(ans)][1](player)

    def helper(self,player):
        line()
        print("プロトタイプ「ヨロシク、オネガイシマス」")
        player.addHelper(self.prototype_helper)
        self.isRoom = False

    def battle(self,player):
        line()
        print("プロトタイプ「暴走モードへ移行」")
        battle = Battle(player,PrototypeEnemy())
        battle.start()

    def roomBack(self,player):
        line()
        print("プロトタイプ「デハ、マタ」")
        input("プロトタイプは部屋に戻った")
        player.removeHelper(self.prototype_helper)
        self.isRoom = True
        self.prototype_helper.systemDown()
