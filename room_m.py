from paper import Paper
from center import Center
from event import Event
from room import Room
from common import line,select

class RoomManager:
    def __init__(self):
        self.paper = Paper()
        self.center = Center()
        self.event = Event()
        self.room_list = [[Room() for _ in range(5)] for _ in range(2)]

    def addIgnes(self,name):
        ignes = self.paper.addIgnes(name)
        self.room_list[ignes["num"][0]][ignes["num"][1]].addIgnes(ignes["class"])
        if ignes["check"]:
            self.event.addIgnes(ignes["class"])

    def search(self,player):
        page = 0
        while player.isAlive:
            line()
            print(f"部屋一覧({page + 1}/{len(self.room_list)})")
            line()
            for i,n in enumerate(self.room_list[page],1):
                print(f"{i}:{n.name}")
            line()
            print("0：戻る")
            print("ENTER：前へ")
            print("b:後ろへ")
            line()
            ans = select(len(self.room_list[page]),["0","","b"])
            if ans == "0":
                break
            elif ans == "":
                page = (page + 1) % len(self.room_list)
            elif ans == "b":
                page = (page - 1) % len(self.room_list)
            else:
                self.room_list[page][int(ans) - 1].enter(player,self.center)
                self.event.action(player,self.center)

