import os
# os.mkdir('新建文件夹') # 创建文件夹
# os.rename('新建文件夹', 'new_dir') # 修改文件夹名
# print(os.getcwd()) # 获取文件夹路径
# os.chdir('new_dir') # 切换目录
# print(os.getcwd())
# os.rmdir('/home/xiong/PycharmProjects/Python快速入门/new_dir') # 删除文件夹

# my_file = open('test.txt') # 打开文件
# # print(my_file.read()) # 读取文件内容
# print(my_file.readline()) # 逐行读取文件内容
# print(my_file.readline()) # 逐行读取文件内容
# print(my_file.readline()) # 逐行读取文件内容

"""
读取时也可以追加模式(模式可以组合):
'r'       只读模式
'w'       写入模式
'x'       创建一个新的可写文件
'a'       追加内容
'b'       字节模式
't'       文本模式
'+'       打开磁盘文件进行读写
"""
my_flie = open('test.txt', mode='wt')
my_flie.write('新添加内容')
my_flie = open('test.txt', mode='at')
my_flie.write('\n这是追加内容')
my_flie.close() #　关闭文件

os.rename('test.txt', '666.txt') #　重命名文件
os.remove('666.txt') # 删除文件

os.listdir('venv') # 获取文件夹里所有文件

# 也可以用 with 打开文件
with open('/home/xiong/PycharmProjects/Python快速入门/11_文件操作.py') as file:
    data = file.read()
print(data)
