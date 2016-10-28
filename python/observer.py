class Pet(object):
    def speak(self, act):
        pass

class Cat(Pet):
    def __init__(self, school):
        self.__school = school
        
    def speak(self):
        print('I am a cat, get school message: {0}'.format(self.__school.get_message()))

class Dog(Pet):
    def __init__(self, school):
        self.__school = school
    def speak(self):
        print('I am a dog, get school message: {0}'.format(self.__school.get_message())) 
            
class School(object):
    def __init__(self):
        self.__pet_list = []
    def add_pet(self, p):
        self.__pet_list.append(p)
    def del_pet(self, p):
        self.__pet_list.remove(p)
    def notify_pet(self):
        for pet in self.__pet_list:
            pet.speak()

class SportSchool(School):
    def get_message(self):
        return self.message
    def set_message(self, msg):
        self.message = msg
        
class PaitSchool(School):
    def get_message(self):
        return self.message
    def set_message(self, msg):
        self.message = msg   

            
        
if __name__ == "__main__":
    ss = SportSchool()
    ss.set_message('do some sport')
    ss.add_pet(Cat(ss))
    ss.add_pet(Dog(ss))
    ss.notify_pet()
    
    ps = PaitSchool()
    ps.set_message('draw a picture')
    cat = Cat(ps)
    dog = Dog(ps)
    ps.add_pet(cat)
    ps.add_pet(dog)
    ps.notify_pet()
    
    ps.del_pet(cat)
    ps.notify_pet()
    
    
    
    
    
    