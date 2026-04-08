from ignes import RoomIgnes
from helper import Helper
from common import line,select

class SukuraHelper(Helper):
    def __init__(self):
        super().__init__("スクラ")

    def action(self,user,target):
        line()
        print("スクラ「ワンワン」")
        input("応援してくれているようだ")

class Sukura(RoomIgnes):
    def __init__(self,_):
        super().__init__("スクラ")
        self.isRoom = True
        self.sukura_helper = SukuraHelper()

    def com(self,player):
        line()
        print("どうする？")
        line()
        if self.isRoom:
            ac = {1:("仲間にする",self.helper)}
        else:
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
        print("スクラ「ワンワン」")
        player.addHelper(self.sukura_helper)
        self.isRoom = False

    def roomBack(self,player):
        line()
        print("スクラ「ワンワン」")
        input("スクラは部屋に戻った")
        player.removeHelper(self.sukura_helper)
        self.isRoom = True
