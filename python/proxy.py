class Person(object):
    pass

class Xiaoming(Person):
    def help(self):
        print "do somebody a favor"
        
class Leifeng(Person):
    def __init__(self):
        self.proxyed = Xiaoming()
    def help(self):
        self.proxyed.help()
        
if __name__ == "__main__":
    leifeng = Leifeng()
    leifeng.help()