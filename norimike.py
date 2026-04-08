from ignes import RoomIgnes,EventIgnes
from enemy import Enemy
from battle import Battle
from common import line,select
import random

class Monster(Enemy):
    def __init__(self):
        super().__init__("魔物",20,10,10)

    def action(self,player):
        line()
        if any(e.type == "power" for e in self.effect):
            print("魔物の突き！")
            player.damage(self.at)
            return
        ac = random.choice(["強化","ミス"])
        if ac == "強化":
            input("魔物が構えている！")
            self.addEffect("強化","power",False,2)
        else:
            input("魔物が様子を見ている")

class NorimikeEnemy(Enemy):
    def __init__(self):
        super().__init__("ノリミケ",10,1,1)
        self.isSeoul = False
        self.deathCount = 0
        self.maxRevive = 3

    def action(self,player):
        line()
        if self.isSeoul:
            self.hp = self.maxHp
            self.name = "ノリミケ"
            self.isSeoul = False
            print("青い魂からノリミケが飛び出してきた！")
            input("ノリミケ「生き返った～」")
            return
        print("ノリミケは魔物を生み出した！")
        ac = random.choice(["攻撃","暴走","ミス"])
        if ac == "攻撃":
            print("魔物はこちらに攻撃してきた！")
            player.damage(10)
        elif ac == "暴走":
            print("魔物は暴れまわった！")
            player.damage(20)
            print("ノリミケも巻き込まれた")
            self.damage(20)
        else:
            input("しかし、魔物は棒立ちだ")

    def hit(self,damage):
        if self.isSeoul:
            input("しかし、攻撃が当たらない……")
            return
        self.hp -= damage
        input(f"{self.name}に{damage}ダメージ！")
        if self.hp <= 0:
            line()
            input(f"{self.name}を倒した！")
            self.hp = 0
            self.name = "青い魂"
            input("青い魂が現れた！？")
            if self.deathCount >= self.maxRevive:
                input("しかし、青い魂はどこかへと消えていった……")
                self.die()
            else:
                self.deathCount += 1
                self.isSeoul = True

class Norimike(RoomIgnes,EventIgnes):
    def __init__(self,_):
        super().__init__("ノリミケ")

    def com(self,player):
        line()
        print("ノリミケ「よう！」")
        line()
        ac = {1:("待つ",self.monster),2:("戦う",self.battle)}
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

    def monster(self,player):
        line()
        input("ノリミケが魔物を生成した！")
        battle = Battle(player,Monster())
        battle.start()

    def battle(self,player):
        line()
        input("ノリミケ「ほへぇ？」")
        battle = Battle(player,NorimikeEnemy())
        battle.start()

    def action(self,player):
        battle = Battle(player,Monster())
        battle.start()
        
