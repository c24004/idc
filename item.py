class Item:
    def __init__(self,name):
        self.name = name

    def use(self,user,target):
        raise NotImplementedError()
