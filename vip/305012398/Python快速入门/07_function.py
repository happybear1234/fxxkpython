age = 18

def my_func():
    # global age # globle 引用全局变量
    age = 66
    age += 1
    print('my_func:', age)
    def my_inner_func():
        nonlocal age # nonlocal 引用嵌套变量
        age += 1
        print('my_inner_func', age)
    my_inner_func()


my_func()