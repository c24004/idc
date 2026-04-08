from ignes import RoomIgnes
from item import Item
from helper import Helper
from common import line,select
from evil_box import Youkage,Evil

class Bracelet(Item):
    def __init__(self):
        super().__init__("ヒカリの腕輪")
        self.hikari = Hikari()
        self.isFriend = False

    def use(self,user,target):
        line()
        if user.isHelper(Hikari):
            input("ヒカリ「私はここだよ！」")
        else:
            if self.isFriend:
                print("ヒカリ「呼んだ？」")
                user.addHelper(self.hikari)
            else:
                print("謎の存在が飛び出してきた！")
                input("ヒカリ「私はヒカリ、よろしくね！」")
                user.addHelper(self.hikari)
                self.isFriend = True

class Hikari(Helper):
    def __init__(self):
        super().__init__("ヒカリ")

    def action(self,user,target):
        line()
        print("ヒカリ「ライジングストーム！」")
        if isinstance(target,(Youkage,Evil)):
            target.hit(999)
        else:
            target.damage(20)
        self.myRemove(user)

    def myRemove(self,player):
        line()
        print("ヒカリ「それじゃ、バイバーイ！」")
        input("ヒカリは消失した")
        player.removeHelper(self)

class HikariBracelet(RoomIgnes):
    def __init__(self,_):
        super().__init__("ヒカリの腕輪")
        self.isRoom = True
        self.bracelet = Bracelet()

    def com(self,player):
        if self.isRoom:
            line()
            print("ヒカリの腕輪がある")
            line()
            ac = {1:("拾う",self.item),2:("壊す",self.damage)}
        else:
            line()
            print("どうする？")
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

    def item(self,player):
        line()
        player.addItem(self.bracelet)
        self.isRoom = False

    def damage(self,player):
        print(f"{player.name}は感電した！")
        player.hit(5)

    def roomBack(self,player):
        line()
        input("ヒカリの腕輪を部屋に返した")
        player.removeItem(self.bracelet)
        self.isRoom = True
        if player.isHelper(Hikari):
            self.bracelet.hikari.myRemove(player)
