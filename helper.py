class Helper:
    def __init__(self,name):
        self.name = name

    def action(self,user,target):
        raise NotImplementedError()
