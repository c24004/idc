from ignes import RoomIgnes
from item import Item
from helper import Helper
from common import line,select

class Elixir(Item):
    def __init__(self):
        super().__init__("エリクサーの瓶")
        self.count = 0
        self.isUse = True

    def use(self,user,target):
        line()
        if self.isUse:
            print("瓶の液体を飲んだ")
            user.heal(999)
            self.consum()
        else:
            self.count += 1
            if self.count < 3:
                input("しかし、中身が空だ")
            else:
                input("液体が満たされている！")
                self.available()

    def consum(self):
        self.count = 0
        self.isUse = False

    def available(self):
        self.isUse = True

class ElixirBottle(RoomIgnes):
    def __init__(self,_):
        super().__init__("エリクサーの瓶")
        self.isRoom = True
        self.elixir = Elixir()

    def com(self,player):
        if self.isRoom:
            line()
            print("エリクサーの瓶がある")
            line()
            ac = {1:("拾う",self.item),2:("飲む",self.use)}
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
        player.addItem(self.elixir)
        self.isRoom = False

    def use(self,player):
        line()
        print("瓶の液体を飲んだ")
        user.heal(999)

    def roomBack(self,player):
        line()
        input("エリクサーの瓶を部屋に返した")
        player.removeItem(self.elixir)
        self.isRoom = True
        self.elixir.available()
