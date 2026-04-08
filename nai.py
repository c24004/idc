from ignes import RoomIgnes
from item import Item
from helper import Helper
from enemy import Enemy
from battle import Battle
from common import line,select,prob
import random

class Gun(Item):
    def __init__(self):
        super().__init__("ビームガン")
        self.isBreak = False

    def use(self,user,target):
        line()
        if self.isBreak:
            input("しかし、壊れて使えない")
        else:
            print("ビームガンを撃った")
            target.damage(20)
            if prob(10):
                self.isBreak = True
                input("壊れた音がした……")

class HealBox(Item):
    def __init__(self):
        super().__init__("ヒールボックス")
        self.isBreak = False

    def use(self,user,target):
        line()
        if self.isBreak:
            input("しかし、壊れて使えない")
        else:
            print("ヒールボックスを使った")
            user.heal(random.randint(10,20))
            if prob(10):
                self.isBreak = True
                input("壊れた音がした……")

class Jetpack(Item):
    def __init__(self):
        super().__init__("ジェットパック")
        self.isBreak = False

    def use(self,user,target):
        line()
        if not self.isBreak and prob(20):
            self.isBreak = True
            print("壊れた音がした……")
        if self.isBreak:
            input("しかし、壊れて使えない")
        else:
            print("ジェットパックを装着した")
            input(f"{user.name}は空中を飛んだ！")
            user.addEffect("飛行","avoid",True,2)

class AirBoat(Item):
    def __init__(self):
        super().__init__("エアボート")
        self.isBreak = False

    def use(self,user,target):
        line()
        if self.isBreak:
            input("しかし、壊れて使えない")
        else:
            print("エアボートに乗って突撃した")
            target.damage(40)
            print("反動を受けてしまった")
            user.hit(10)
            if prob(20):
                self.isBreak = True
                input("壊れた音がした……")

class AssistantRobot(Helper):
    def __init__(self):
        super().__init__("アシスタントロボ")
        self.isBreak = False

    def action(self,user,target):
        line()
        if self.isBreak:
            input("アシスタントロボ「故障しています」")
            return
        print("アシスタントロボ「どうしますか？」")
        line()
        ac = {1:("攻撃",self.attack),2:("回復",self.heal)}
        for i,(v,_) in ac.items():
            print(f"{i}:{v}")
        line()
        ans = select(len(ac))
        line()
        ac[int(ans)][1](user,target)
        if prob(20):
            self.isBreak = True
            input("アシスタントロボ「システムエラー」")
            print("アシスタントロボは爆発した！")
            user.damage(50)
            target.damage(50)

    def attack(self,user,target):
        print("アシスタントロボのビームガン！")
        target.damage(30)

    def heal(self,user,target):
        print("アシスタントロボのヒールライト！")
        user.heal(random.randint(10,30))

class NaiEnemy(Enemy):
    def __init__(self):
        super().__init__("ナイ",30,20,20)

    def action(self,player):
        if any(e.type == "power" for e in self.effect):
            print("エアボートで突撃してきた！")
            player.damage(self.at * 2)
            print("反動を受けた！")
            self.hit(10)
            return
        ac = random.choice(["攻撃","強化","回避","ミス"])
        line()
        if ac == "攻撃":
            print("ナイのビームガン")
            player.damage(self.at)
        elif ac == "強化":
            if self.hp <= self.maxHp // 2:
                print("ナイのヒールボックス")
                self.heal(10)
            else:
                input("ナイはエアボートに乗り込んだ！")
                self.addEffect("強化","power",False,2)
                self.addEffect("防御","defense")
        elif ac == "回避":
            input("ナイはジェットパックで空中を飛んだ！")
            self.addEffect("飛行","avoid",True,2)
        else:
            input("ナイはこちらの様子をうかがっている")

class Nai(RoomIgnes):
    def __init__(self,_):
        super().__init__("ナイ")
        self.robot = AssistantRobot()

    def com(self,player):
        item_list = [Gun,HealBox,Jetpack,AirBoat]
        p_list = [i for i in player.item if isinstance(i,(Gun,HealBox,Jetpack,AirBoat))]
        for i in item_list[:]:
            if player.isItem(i):
                item_list.remove(i)
        ac = {}
        if item_list:
            ac[1] = ("もらう",self.item)
        if p_list:
            ac[len(ac) + 1] = ("返す",self.itemBack)
        ac[len(ac) + 1] = ("ロボ",self.helper)
        ac[len(ac) + 1] = ("戦う",self.battle)
        line()
        print("ナイ「この僕に何か用かい？」")
        line()
        for i,(v,_) in ac.items():
            print(f"{i}:{v}")
        print("0:戻る")
        line()
        ans = select(len(ac),["0"])
        if ans == "0":
            line()
            input(f"{player.name}は部屋を出た")
        else:
            ac[int(ans)][1](player,item_list,p_list)

    def item(self,player,item_list,_):
        line()
        print("ナイ「有効活用してくれよ？」")
        player.addItem(random.choice(item_list)())

    def itemBack(self,player,_,p_list):
        line()
        print("ナイ「もう、良いのかい？」")
        line()
        for i,it in enumerate(p_list,1):
            print(f"{i}:{it.name}")
        line()
        ans = select(len(p_list))
        line()
        input(f"{p_list[int(ans) - 1].name}を返した")
        player.removeItem(p_list[int(ans) - 1])

    def helper(self,player,i_,p_):
        if player.isHelper(AssistantRobot):
            print("ナイ「役に立ったかい？」")
            input("アシスタントロボを返した")
            player.removeHelper(self.robot)
        else:
            print("ナイ「アシスタントロボ連れてくかい？」")
            print("アシスタントロボ「よろしくお願いします」")
            player.addHelper(self.robot)

    def battle(self,player,i_,p_):
        line()
        print("ナイ「ちょうど発明品の効果を試したかったんだ」")
        battle = Battle(player,NaiEnemy())
        battle.start()
