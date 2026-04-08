from noid import Noid
from prototype import Prototype
from evil_box import EvilBox
from hikari_bracelet import HikariBracelet
from nai import Nai
from norimike import Norimike
from nouzen import Nouzen
from sukura import Sukura
from elixir_bottle import ElixirBottle
from zombie_virus import ZombieVirus
from kyombie import Kyombie

class Paper:
    def __init__(self):
        self.dec = {"ノイド":{"class":Noid,"num":(0,0),"event":False},
                    "プロトタイプ":{"class":Prototype,"num":(0,0),"event":False},
                    "邪悪箱":{"class":EvilBox,"num":(0,1),"event":True},
                    "ヒカリの腕輪":{"class":HikariBracelet,"num":(0,2),"event":False},
                    "ナイ":{"class":Nai,"num":(0,3),"event":False},
                    "ノリミケ":{"class":Norimike,"num":(0,4),"event":True},
                    "ノウゼン":{"class":Nouzen,"num":(1,0),"event":True},
                    "スクラ":{"class":Sukura,"num":(1,1),"event":False},
                    "エリクサーの瓶":{"class":ElixirBottle,"num":(1,2),"event":False},
                    "ゾンビウイルス":{"class":ZombieVirus,"num":(1,3),"event":True},
                    "キョンビ":{"class":Kyombie,"num":(1,4),"event":False}
                    }

    def addIgnes(self,name,center):
        if name not in self.dec:
            print("存在しないイグネス")
            return None
        data = self.dec[name]

        return {
            "class": data["class"](center),
            "num": data["num"],
            "event": data["event"]
            }
