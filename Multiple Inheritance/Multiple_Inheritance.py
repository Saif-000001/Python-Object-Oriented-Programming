class GrandMother:
    def __init__(self, name):
        self.name = name
    
    def sleep(self):
        print('sleeping')
    
class Mother(GrandMother):
    def hobby(self):
        print('Cooking')

class Father(GrandMother):
    def interest(self):
        print('market')

        

class SmallChaild(Mother):
      def character(self):
        print('tawut numer 1')
class MiddleChaild(Father):
    def character(self):
        print('tawut number 2')

class BigChaild(Mother, Father):
    def character(self):
        print('less than tawut number 1 and 2')

small = SmallChaild('babul')
middle = MiddleChaild('kabil')
big = BigChaild('habil')

# print(small.name)
# big.interest()
# big.hobby()

# small.interest()
# middle.interest()

small.sleep()








    