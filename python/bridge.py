class Action(object):
    def do(self):
        pass

class PlayBall(Action):
    def do(self):
        print "Let us play a ball."

class WatchTV(Action):
    def do(self):
        print "Let us watch TV."
        
class Pet(object):
    def speak(self, act):
        pass

class Cat(Pet):
    def __init__(self, act):
        self.__act = act
        
    def speak(self):
        print "I am a cat. "
        if self.__act:
            self.__act.do()

class Dog(Pet):
    def __init__(self, act):
        self.__act = act
    def speak(self):
        print "I am a dog. "
        if self.__act:
            self.__act.do()
        
if __name__ == "__main__":
    act = PlayBall()
    dog = Cat(act)
    dog.speak()