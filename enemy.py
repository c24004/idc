from battle_chara import BattleChara
from common import line

class Enemy(BattleChara):
    def __init__(self,name,hp,at,df):
        super().__init__(name,hp,at,df)

    def show_status(self):
        self.show_status_base()
        line()
        input("(確認)")
