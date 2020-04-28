class Person:
    str = '帅哥'# 共有变量
    def __init__(self,name,age):# 初始化
        self.name = name
        self.age = age
    def say(self,something):# 定义方法
        return '{}说{}'.format(self.name,something)
    def eat(self,food):
        return '{}吃{}'.format(self.name,food)

handsomeb = Person('handsomeb',18)
zhang_san = Person('zhangsan',19)
print(handsomeb.name)
print(handsomeb.age)
print(zhang_san.name)
print(zhang_san.age)
print(handsomeb.str)
print(zhang_san.str)

print(handsomeb.say('哈哈哈哈哈哈哈'))
print(zhang_san.eat('shi'))

# 继承
class Yellowpeople(Person):
    def sing(self,song):
        return '{}正在唱{}'.format(self.name,song)

wang_er = Yellowpeople('wanger',18)
print(wang_er.name)
print(wang_er.age)
print(wang_er.say('我是歌手'))
print(wang_er.sing('大碗宽面'))

# 方法重写 初始化也可以重写
class Blackpeople(Person):
    def eat(self,food):
        return '{}正在狼吞虎咽的吃{}'.format(self.name,food)
    def print_some(self):
        print('子类中使用父类变量或方法用super',super().str)

jack = Blackpeople('jack',18)
print(jack.name)
print(jack.eat('shi'))
jack.print_some()