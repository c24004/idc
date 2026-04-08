from ignes import RoomIgnes,EventIgnes
from common import line,select
from elixir_bottle import Elixir

class ZombieVirus(RoomIgnes,EventIgnes):
    def __init__(self,center):
        super().__init__("ゾンビウイルス")
        self.center = center
        self.isKyombie = False

    def com(self,player):
        line()
        if self.isKyombie:
            input("この部屋には何もいない")
            return
        print("ゾンビがいる！？")
        line()
        ac = {1:("待つ",self.death)}
        for i,(v,_) in ac.items():
            print(f"{i}:{v}")
        print("0:戻る")
        ans = select(len(ac),["0"])
        if ans == "0":
            line()
            input(f"{player.name}は部屋を出た")
        else:
            ac[int(ans)][1](player)

    def death(self,player):
        line()
        input(f"{player.name}はゾンビになってしまった……")
        player.die()

    def action(self,player):
        line()
        if self.isKyombie:
            input("キョンビがゾンビウイルスを吐き出した！")
            self.isKyombie = False
        else:
            input("ゾンビの大群が押し寄せてきた！")
            elixir = [i for i in player.item if isinstance(i,Elixir)]
            if elixir and elixir[0].isUse:
                print("しかし、持っていたエリクサーを使って")
                input("ゾンビになったヤツらを治療した")
                elixir[0].consum()
                if self.center.getFlag("isKyombie"):
                    input("ゾンビウイルスはキョンビに食べられた")
                    self.isKyombie = True
            else:
                input(f"{player.name}はゾンビになってしまった……")
                player.die()
            

