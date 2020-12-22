import os

# 关于文件路径os.path.dirname()：绝对路径，可以获取你当前的文件或者文件夹所在的目录的绝对路径
# 参数：__file__，文件夹的路径
# 以下要写的代码，代表获取test.py所在的文件夹->
# file_path = os.path.dirname(__file__)
# print(file_path)

# 以下代码，获取tool所在的文件夹-->lesson6_2-->base_dir 工程目录
# base_dir = os.path.dirname(os.path.dirname(__file__))
# print(base_dir)
# #

from os.path import join, realpath, dirname, pardir, abspath, exists

def get_path(*args):
    global ROOT_PATH
    ROOT_PATH = abspath(join(dirname(realpath(__file__)), pardir))   # ROOT_PATH：获取的是该工程目录的绝对路径
    fp_path = ROOT_PATH
    for item in args:
        fp_path = os.path.join(fp_path, item)
    return fp_path   # D:\Learn\Code\webautoTest\lesson6_2\data\data.xlsx

'''
os.path.abspath(path)：返回path规范化的绝对路径
abspath(__file__)：
==> D:\Learn\Code\webautoTest\lesson6_2\tool\test.py，获取的是当前运行的这个.py文件的绝对路径

os.path.join(path1[, path2[, ...]])：将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
abspath(join(__file__))：
==> D:\Learn\Code\webautoTest\lesson6_2\tool\test.py 

abspath(join(dirname(__file__)))：
==> D:\Learn\Code\webautoTest\lesson6_2\tool，获取的是当前运行的这个.py文件的父级文件夹目录

abspath(join(dirname(realpath(__file__))))：
==> D:\Learn\Code\webautoTest\lesson6_2\tool，获取的是当前运行的这个.py文件的父级文件夹目录
==> os.path.realpath(__file__)：D:\Learn\Code\webautoTest\lesson6_2\tool\test.py：realpath() 获得的是该方法所在的脚本的路径

abspath(join(dirname(realpath(__file__)), pardir))：
==> D:\Learn\Code\webautoTest\lesson6_2，获取整个框架的工程目录，os.pardir：获取的是当前运行的这个.py文件的父级文件夹目录的父级

'''


if __name__ == '__main__':

    file_path = get_path('data', 'data.xlsx')
    print(file_path)
