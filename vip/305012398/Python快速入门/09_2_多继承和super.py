class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self, food):
        print(self.name,'调用的是 Person 方法,正在吃{}'.format(food))
class Yellowpeople(Person):
    def eat(self, food):
        # print(self.name,'调用的是 Yellowpeople 方法,正在吃{}'.format(food))
        super().eat(food)
class Blackpeople(Person):
    def eat(self, food):
        print(self.name,'调用的是 BlackPeople 方法,正在吃{}'.format(food))
class Son(Yellowpeople,Blackpeople):
    def eat(self, food):
        # print(self.name,'调用的是 Son 方法,正在吃{}'.format(food))
        super().eat(food) # super 就是调用__mro__顺序的下一个


handsome = Son('handsomeb', 18)
handsome.eat('food')
# print(Son.__mro__) # 查看调用顺序