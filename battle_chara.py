from effect import Effect
from common import line
import random

class BattleChara:
    def __init__(self,name,hp,at,df):
        self.name = name
        self.maxHp = hp
        self.hp = hp
        self.at = at
        self.df = df
        self.effect = []
        self.isAlive = True

    def show_status_base(self):
        line()
        print(f"名前:{self.name}")
        print(f"HP:{self.hp}/{self.maxHp}")
        print(f"AT:{self.at}")
        print(f"DE:{self.df}")
        if self.effect:
            e_list = [e.name for e in self.effect]
            print(f"状態:{e_list}")

    def addEffect(self,e_name,e_type,isStart = True,turn = 1):
        self.effect.append(Effect(e_name,e_type,isStart,turn))

    def removeEffect(self,effect):
        self.effect.remove(effect)

    def damage(self,dmg):
        d = max(1,dmg // 2 - self.df // 4 + random.randint(0,3))
        if any(e.type == "defense" for e in self.effect):
            d //= 2
        self.hit(d)

    def hit(self,damage):
        self.hp -= damage
        input(f"{self.name}に{damage}ダメージ！")
        if self.hp <= 0:
            self.die()

    def die(self):
        self.isAlive = False
