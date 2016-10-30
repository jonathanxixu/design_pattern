def singleton(cls, *args, **kw):
    instances = {}
    def singletond():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return singletond
        
@singleton
class MyClass(object):
    a = 1
    def __init__(self):
        pass
    
if __name__ == "__main__":
    m1 = MyClass()
    m1.a = 5
    m2 = MyClass()
    print m2.a