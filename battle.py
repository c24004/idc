from common import line

class Battle:
    def __init__(self,player,enemy,log = None):
        self.player = player
        self.enemy = enemy
        self.log = log

    def start(self):
        line()
        print(f"{self.enemy.name}が現れた！")
        line()
        input("(確認)")
        act = [self.player,self.enemy]
        turn = 0
        while self.player.isAlive and self.enemy.isAlive:
            line()
            print(f"{act[turn].name}のターン")
            for e in act[turn].effect[:]:
                e.update(act[turn],"start")
            act[turn].action(act[1 - turn])
            for e in act[turn].effect[:]:
                e.update(act[turn],"end")
            turn = 1 - turn
        line()
        if self.player.isAlive:
            input("勝利！")
        else:
            input("敗北……")
