try:
    x = 1 / 0
except ZeroDivisionError as err: # 超类 Exception (多个异常信息可以(,,,)表示)
    print('try语句发生异常,错误信息{}'.format(err))
else:
    print('没有异常才会执行的语句')
finally:
    print('不管有没有异常都会执行的语句')
print('结果')


# 自定义异常
# raise Exception('自己抛出一个异常')

# 最简单的自定义异常
# class MyException(Exception):
#     pass
#
# raise MyException('抛出一个自定义异常')


# 还可以自定义方法
class MyError(Exception):
    def __init__(self, value):
        super().__init__(self)
        self.value = value
    def __str__(self):
        return self.value
try:
    raise MyError('自定义异常')
except MyError as err:
    print(err)

