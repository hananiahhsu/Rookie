

#类的初始化
class CFirstCnn:
    def __init__(self,name):
        self.name = name

    def calculate(self,x,y,z):
        return x + y + z

    def show(self):
        print("%",self.name)