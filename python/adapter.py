class Person(object):
    def wufan(self):
        pass
    def wanfan(self):
        pass

class Lilei(Person):
    def wufan(self):
        print "≥‘ŒÁ≤Õ¡À"
    def wanfan(self):
        print "≥‘ÕÌ∑π¡À"
        
class Lucy():
    def lunch(self):
        print "have a nice lunch"
    def supper(self):
        print "have a nice supper"
        
class Lucy_trans(Person):
    def __init__(self):
        self.friend = Lucy()
    def wufan(self):
        self.friend.lunch()
    def wanfan(self):
        self.friend.supper()
        
if __name__=="__main__":
    students = []
    students.append(Lilei())
    students.append(Lucy_trans())
    for ele in students:
        ele.wufan()
        ele.wanfan()