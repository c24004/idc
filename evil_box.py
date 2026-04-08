from ignes import RoomIgnes,EventIgnes
from item import Item
from enemy import Enemy
from battle import Battle
from common import line,select
from nouzen import NouzenEnemy
import random

class EvilBoxItem(Item):
    def __init__(self,center):
        super().__init__("邪悪箱")
        self.center = center
        self.isYoukage = True

    def use(self,user,target):
        line()
        input("コツンと叩いた")
        if self.isYoukage and isinstance(target,(Evil,NouzenEnemy)):
            print(f"ヨウカゲ「オレに任せろ……」")
            input("ヨウカゲが敵を一掃した")
            target.die()
            self.isYoukage = False
            self.center.setFlag("isYoukage")
        else:
            input("しかし、何も起きない")

    def inYoukage(self):
        self.isYoukage = True

class Youkage(Enemy):
    def __init__(self):
        super().__init__("ヨウカゲ",100,50,50)

    def action(self,player):
        line()
        if any(e.type == "power" for e in self.effect):
            input("ヨウカゲ「消え失せろ……」")
            player.damage(self.at * 2)
            return
        ac = random.choice(["攻撃","防御","強化"])
        if ac == "攻撃":
            print("ヨウカゲの殴打！")
            player.damage(self.at)
        elif ac == "強化":
            input("ヨウカゲの腕が変形した！？")
            self.addEffect("強化","power",False,2)
        else:
            input("ヨウカゲが身を固める！")
            self.addEffect("防御","defense")

class Evil(Enemy):
    def __init__(self):
        super().__init__("邪悪な存在",50,20,20)

    def action(self,player):
        line()
        if any(e.type == "power" for e in self.effect):
            input("邪悪な存在の大暴れ！")
            player.damage(self.at * 2)
            return
        ac = random.choice(["攻撃","強化","ミス"])
        if ac == "攻撃":
            print("邪悪な存在の叩き！")
            player.damage(self.at)
        elif ac == "強化":
            input("邪悪な存在の身体が膨れ上がる！")
            self.addEffect("強化","power",False,2)
        else:
            input("邪悪な存在が様子を見ている")

class EvilBox(RoomIgnes,EventIgnes):
    def __init__(self,center):
        super().__init__("邪悪箱")
        self.isRoom = True
        self.center = center
        self.item = EvilBoxItem(center)

    def com(self,player):
        if self.isRoom:
            line()
            print("邪悪箱がある")
            line()
            ac = {1:("拾う",self.evil),2:("壊す",self.battle)}
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

    def evil(self,player):
        line()
        input("箱の中から黒い影が飛び出してきた！")
        battle = Battle(player,Evil())
        battle.start()

    def battle(self,player):
        line()
        input("？？？「この箱を壊そうとしたのは……お前か？」")
        battle = Battle(player,Youkage())
        battle.start()
        if player.isAlive:
            player.addItem(self.item)
            self.center.setFlag("isYoukage",False)
            self.isRoom = False

    def roomBack(self,player):
        line()
        input("邪悪箱を部屋に返した")
        player.removeItem(self.item)
        self.isRoom = True

    def action(self,player):
        line()
        if not self.center.getFlag("isYoukage"):
            input("邪悪な存在が襲い掛かってきた！")
            battle = Battle(player,Evil())
            battle.start()
        elif player.isItem(EvilBoxItem):
            print("ヨウカゲ「おい、それはオレの箱だ」")
            if input("邪悪箱を返す？(y/n):") == "y":
                line()
                print("邪悪箱をヨウカゲに返した")
                input("ヨウカゲ「ありがとよ」")
                player.removeItem(self.item)
                self.isRoom = True
            else:
                line()
                input("ヨウカゲ「お前……偉そうだな？」")
                battle = Battle(player,Youkage())
                battle.start()
            self.center.setFlag("isYoukage",False)
            self.item.inYoukage()
        else:
            input("邪悪な存在が襲い掛かってきた！")
            input("しかし、ヨウカゲが一掃した")
