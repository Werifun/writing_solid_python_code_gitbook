#coding:utf-8

# this program calculates the volume of a cylinder given RADIUS and HEIGHT
# Cylinder Volume = (pi)*(radius**2)*(height)

import math
import argparse

# 创建解析器
parser = argparse.ArgumentParser(description='Calculate volume of a Cylinder')
# 添加参数步骤
# -r 和 --radius貌似指定的是同一个参数
# metavar 用于简化help的信息
# type 指定数据类型
# required 表明是否是可选参数 True表示必须输入
# help是帮助参数
parser.add_argument('-r','--radius', metavar='',type=int, required=True, help='Radius of Cylinder')  # metavar 用于简化help的信息
parser.add_argument('-H','--height', metavar='',type=int, required=True, help='Height of Cylinder')
# 创建互斥组
# -q -v 只能二选一
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet' ,action='store_true',help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
# 解析参数步骤
args = parser.parse_args()

def cylinder_volume(radius, height):
    vol = (math.pi)*(radius**2)*(height)
    return vol


if __name__ == '__main__':
    volume = cylinder_volume(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print("Volume of a Cylinder with radius {} and height {} is {}".format(args.radius, args.height, volume))
    else:
        print('Volume of Cylinder = {}'.format(volume))

