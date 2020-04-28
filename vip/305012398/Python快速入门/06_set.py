a = {1,2,3,4,5} # 无序,不能索引
print(1 in a)
a.add(6) # 只能添加不能改变的值:number,tuple,string
a.add((1,2,3))
a.add('handsomeb')

a.update((6,7)) # 改写数据:拆分再添加(列表也可以)
a.update([8,9])
a.update({8,9})
a.update({'name':'sb'})

a.remove(9) # 删除的值不存在会报错
a.discard(10) # 不会报错
a.clear()

print(a)

b = {1,2,3,4,5}
c = {4,5,6,7,8}
d ={4,5}
print(b.union(c)) # 并集
print(b.intersection(c)) # 交集
print(d.issubset(b)) # 判断是否子集
print(b.issuperset(d)) # 判断是否父集