def decorator_phone_cover(fn):
    def cover(*args):
        fn(*args)
        print('after I get the iphone, I will cover sth to its screen.')
    return cover

def decorator_phone_cases(fn):
    def cases(*args):
        fn(*args)
        print('aftern I get the iphone, I will add a case for it. ')
    return cases

def prepare_money(fn):
    def prepare(*args):
        print 'I have enough money, I will buy a phone. '
        fn(*args)
    return prepare

@prepare_money    
@decorator_phone_cases
@decorator_phone_cover
def get_phone(a, b):
    print 'I get a phone, {}'.format(a+b)
    
    
if __name__ == "__main__":
    get_phone(500,100)