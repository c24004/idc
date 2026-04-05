from room_m import RoomManager
from common import line,select

class WishBox:
    def __init__(self):
        self.room_m = RoomManager()
        self.wishList = ["ノイド"]

    def development(self,player):
        if self.wishList:
            line()
            print("イグネス一覧")
            line()
            for i,w in enumerate(self.wishList,1):
                print(f"{i}:{w}")
            print("0:戻る")
            line()
            ans = select(len(self.wishList),["0"])
            if ans == "0":
                return
            else:
                ignes = self.wishList.pop(int(ans) - 1)
                self.room_m.addIgnes(ignes)
        else:
            line()
            input("今は開発するものはない")

        self.room_m.search(player)
