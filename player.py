from battle_chara import BattleChara
from common import line,select

class Player(BattleChara):
    def __init__(self,name):
        super().__init__(name,100,10,10)
        self.con = "通常"
        self.item = []
        self.helper = []

    def open_status(self,player):
        self.show_status_base()
        print(f"ST:{self.con}")
        if self.item:
            name_list = [i.name for i in self.item]
            print(f"{name_list}")
        if self.helper:
            name_list = [h.name for h in self.helper]
            print(f"{name_list}")
        line()
        input("(確認)")

    def show_status(self):
        self.show_status_base()
        if self.item:
            name_list = [i.name for i in self.item]
            print(f"{name_list}")
        if self.helper:
            name_list = [h.name for h in self.helper]
            print(f"{name_list}")
        line()
        input("(確認)")

    def addItem(self,item):
        input(f"{item.name}をゲットした！")
        self.item.append(item)

    def removeItem(self,item):
        self.item.remove(item)

    def addHelper(self,helper):
        input(f"{helper.name}が仲間になった！")
        self.helper.append(helper)

    def removeHelper(self,helper):
        self.helper.remove(helper)

    def attack(self,enemy):
        line()
        print(f"{self.name}は剣で攻撃！")
        enemy.damage(self.at)
        return True

    def defense(self,enemy):
        line()
        input(f"{self.name}は盾で防御！")
        self.addEffect(self,"防御","defense")
        return True

    def observer(self,enemy):
        ac = {1:self,2:enemy}
        line()
        print("誰を確認？")
        line()
        for k,v in ac.items():
            print(f"{k}:{v.name}")
        print("0:戻る")
        ans = select(len(ac),["0"])
        if ans == "0":
            pass
        else:
            ac[int(ans)].show_status()
        return False

    def i_use(self,enemy):
        line()
        print("どれを使う？")
        line()
        for i,it in enumerate(self.item,1):
            print(f"{i}:{it.name}")
        print("0:戻る")
        line()
        ans = select(len(self.item),["0"])
        if ans == "0":
            pass
        else:
            self.item[int(ans) - 1].use(self,enemy)
            return True

    def h_action(self,enemy):
        line()
        print("誰にする？")
        line()
        for i,h in enumerate(self.helper,1):
            print(f"{i}:{h.name}")
        print("0:戻る")
        line()
        ans = select(len(self.item),["0"])
        if ans == "0":
            pass
        else:
            self.helper[int(ans) - 1].action(self,enemy)
            return True

    def action(self,enemy):
        while True:
            ac = {1:("攻撃",self.attack),2:("防御",self.defense),3:("確認",self.observer)}
            if self.item:
                ac[len(ac) + 1] = ("道具",self.i_use)
            if self.helper:
                ac[len(ac) + 1] = ("味方",self.h_action)
            line()
            print("行動一覧")
            line()
            for i,(v,_) in ac.items():
                print(f"{i}:{v}")
            line()
            ans = select(len(ac))
            isFinish = ac[int(ans)][1](enemy)
            if isFinish:
                break
