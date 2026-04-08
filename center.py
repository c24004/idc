class Center:
    def __init__(self):
        self.status = "通常"
        self.danger = 0
        self.flags = {}

    def statusChange(self, new):
        self.status = new

    def addDanger(self, value):
        self.danger = min(100, self.danger + value)

    def removeDanger(self,value):
        self.danger = max(0,self.danger - value)

    def setFlag(self, key,isTrigger = True):
        self.flags[key] = isTrigger

    def getFlag(self, key):
        return self.flags.get(key, False)
