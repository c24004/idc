from ignes import RoomIgnes,EventIgnes
from item import Item
from enemy import Enemy
from battle import Battle
from common import line,select

class EvilBoxItem(Item):
    def __init__(self):
        super().__init__("邪悪箱")

    def use(self,user,target):
        line()
        input("コツンと叩いた")
        if isinstance(target,Evil):
            print(f"ヨウカゲ「オレに任せろ……」")
            input("ヨウカゲが敵を一掃した")
            target.die()
        else:
            input("しかし、何も起きない")

class Youkage(Enemy):
    def __init__(self):
        super().__init__("ヨウカゲ",100,50,50)

    def action(self,player):
        line()
        input("ヨウカゲ「消え失せろ……」")
        player.damage(self.at)

class Evil(Enemy):
    def __init__(self):
        super().__init__("邪悪な存在",50,20,20)

    def action(self,player):
        line()
        print("邪悪な存在「ガルル！」")
        player.damage(self.at)

class EvilBox(RoomIgnes,EventIgnes):
    def __init__(self):
        super().__init__("邪悪箱")
        self.isRoom = True
        self.item = EvilBoxItem()

    def com(self,player,center):
        if self.isRoom:
            line()
            print("邪悪箱がある")
            line()
            ac = {1:("拾う",self.evil),2:("戦う",self.battle)}
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
            ac[int(ans)][1](player,center)

    def evil(self,player,center):
        line()
        input("箱の中から黒い影が飛び出してきた！")
        battle = Battle(player,Evil())
        battle.start()

    def battle(self,player,center):
        line()
        input("？？？「お前……偉そうだな？」")
        battle = Battle(player,Youkage())
        battle.start()
        if player.isAlive:
            player.addItem(self.item)
            self.isRoom = False

    def roomBack(self,player,center):
        line()
        input("邪悪箱を部屋に返した")
        player.removeItem(self.item)
        self.isRoom = True

    def action(self,player,center):
        line()
        input("邪悪な存在が襲い掛かってきた！")
        battle = Battle(player,Evil())
        battle.start()
