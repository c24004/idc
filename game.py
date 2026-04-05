from player import Player
from wishBox import WishBox
from common import line,select

class Game:
    def __init__(self,name):
        self.player = Player(name)
        self.wishBox = WishBox()

    def start(self):
        ac = {1:("開発",self.wishBox.development),2:("確認",self.player.open_status)}
        while True:
            line()
            print("どうする？")
            line()
            for i,(v,_) in ac.items():
                print(f"{i}:{v}")
            print("0:終了")
            line()
            ans = select(len(ac),["0"])
            if ans == "0":
                break
            else:
                ac[int(ans)][1](self.player)
