print('这是单引号转义字符:\'')
print('这是双引号转义字符:\"')
print('这是换行转义字符:\n换行')
print('表示table:\t对齐')
print('表示回车:\r回车')
print('表示退格:\b')

print(r'打印原始字符\n')

print('字符/整形格式化:我叫%s,今年%d岁' %('小帅比',18))
print('format1:我叫{0},今年{1}岁'.format('小帅比',18))
print('format2:我叫{name},今年{age}岁'.format(name='小帅比',age=18))
# f-string
name = '小帅比'
age = 18
print('f-string:'+f'我叫{name},今年{age}岁')

str1 = '今天是个好日子'
print(str1.find('是个')) # 不存在返回 -1
print(str1[2])

print(str1.replace('今天','昨天'))

#分割
str2 = '2019-10-1 14:00:23'
print(str2.split(" "))
print(str2.split(' ')[0].split("-"))
print(str2.split(' ')[1].split(':'))

# 去空格
str3 = '   好好学习,天天向上        '
print(str3.strip())

# 大写转小写
str4 = 'I AM A HANDSOME BOY'
print(str4.lower())
# 小写转大写
str5 = 'i am a handsome boy'
print(str5.upper())

# 判断开头和结尾字符
str6 = '美女和野兽的故事.MP4'
print(str6.startswith('美女'))
print(str6.endswith('MP4'))