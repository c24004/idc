class Room:
    def __init__(self):
        self.name = "???"
        self.ignes = None

    def addIgnes(self,ignes):
        self.name = ignes.name
        self.ignes = ignes

    def enter(self,player,center):
        if self.ignes:
            self.ignes.com(player,center)
        else:
            print("空き部屋だ")
