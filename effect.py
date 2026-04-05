class Effect:
    def __init__(self,name,e_type,timing,turn):
        self.name = name
        self.type = e_type
        self.isStart = timing
        self.turn = turn

    def update(self,target,phase):
        if (phase == "start" and self.isStart) or (phase == "end" and not self.isStart):
            self.turn -= 1
            if self.turn <= 0:
                target.removeEffect(self)
