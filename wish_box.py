from room_m import RoomManager
from common import line,select
import random

class WishBox:
    def __init__(self):
        self.room_m = RoomManager()
        self.wishList = ["プロトタイプ","邪悪箱","ヒカリの腕輪","ナイ","ノリミケ","ノウゼン","スクラ","エリクサーの瓶","ゾンビウイルス","キョンビ"]

    def development(self,player):
        if self.wishList:
            l = random.sample(self.wishList,min(3,len(self.wishList)))
            line()
            print("イグネス一覧")
            line()
            for i,w in enumerate(l,1):
                print(f"{i}:{w}")
            line()
            ans = select(len(l))
            if ans == "0":
                return
            else:
                ignes = l[int(ans) - 1]
                line()
                print(f"{ignes}を開発した！")
                line()
                input("(確認)")
                self.room_m.addIgnes(ignes)
                self.wishList.remove(ignes)
        else:
            line()
            input("今は開発するものはない")

        self.room_m.search(player)
