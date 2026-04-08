class Ignes:
    def __init__(self,name):
        self.name = name

class RoomIgnes(Ignes):
    def com(self,player):
        raise NotImplementedError()

class EventIgnes(Ignes):
    def action(self,player):
        raise NotImplementedError()
