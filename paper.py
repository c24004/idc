from noid import Noid

class Paper:
    def __init__(self):
        self.dec = {"ノイド":{"class":Noid,"num":(0,0),"check":False}}

    def addIgnes(self,name):
        if name not in self.dec:
            print("存在しないイグネス")
            return None
        data = self.dec[name]

        return {
            "class": data["class"](),
            "num": data["num"],
            "check": data["check"]
            }
