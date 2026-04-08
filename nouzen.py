from ignes import RoomIgnes,EventIgnes
from enemy import Enemy
from battle import Battle
from common import line,select
from sukura import SukuraHelper

class NouzenEnemy(Enemy):
    def __init__(self,isSukura):
        super().__init__("ノウゼン",10,1,1)
        self.isSukura = isSukura

    def action(self,player):
        line()
        print("ノウゼンの現実改変！")
        if self.isSukura:
            input("しかし、効果はない")
        else:
            input(f"{player.name}は歯車になってしまった……")
            player.die()

    def hit(self,damage):
        if self.isSukura:
            self.hp -= damage
            input(f"{self.name}に{damage}ダメージ！")
            if self.hp <= 0:
                self.die()
        else:
            input("しかし、攻撃が効かない")

class Nouzen(RoomIgnes,EventIgnes):
    def __init__(self,center):
        super().__init__("ノウゼン")
        self.center = center
        self.upCount = 0

    def com(self,player):
        line()
        print("ノウゼン「おい！崇めろ！」")
        line()
        ac = {1:("崇める",self.statusUp),2:("バカにする",self.death)}
        for i,(v,_) in ac.items():
            print(f"{i}:{v}")
        print("0:戻る")
        ans = select(len(ac),["0"])
        if ans == "0":
            line()
            input(f"{player.name}は部屋を出た")
        else:
            isSukura = player.isHelper(SukuraHelper)
            ac[int(ans)][1](player,isSukura)

    def statusUp(self,player,isSukura):
        line()
        input("我の恵みを与えよう……ハッ！")
        if isSukura:
            input("ノウゼン「我の力が通用しない！？」")
        else:
            if self.upCount < 2:
                input("防御力が上昇した！")
                player.df += 10
                self.upCount += 1
            else:
                player.heal(999)

    def death(self,player,isSukura):
        line()
        input("我を愚するな！ハッ！")
        if isSukura:
            input("ノウゼン「我の力が通用しない！？」")
        else:
            input(f"{player.name}は歯車になってしまった……")
            player.die()

    def action(self,player):
        isSukura = player.isHelper(SukuraHelper)
        line()
        input("ノウゼン「我を崇めるのだー！」")
        if self.center.getFlag("isYoukage"):
            input("しかし、ヨウカゲがノウゼンをボコボコにした")
        else:
            battle = Battle(player,NouzenEnemy(isSukura))
            battle.start()

