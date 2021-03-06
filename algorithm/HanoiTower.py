#!/usr/bin/python3
# @Time    : 2017/5/19 下午2:58
# @Author  : Steven.He
#
# Copyright Steven.He
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def hanoi(a, b, c, n):
    '''
    汉诺塔算法
    有a,b,c的针塔,把所有盘子依次从a的针上移动到c上
    盘子半径均由上往下增大,规则是
    1,圆盘可以插进a,b,c塔座上,
    2,每次移动一个圆盘,
    3,任何时刻都不能将一个较大的圆盘压在较小的圆盘之上
    原理是
    反向推敲,根据最后结果所有圆盘都在c针盘上,所以最大底盘移动到c
    顺序是
    1,把除底盘以外的盘子移动到b上
    2,把底盘移动到c上
    3,把剩下的盘子移动到c
    
    :param a:初始针座 
    :param b:借助针座 
    :param c:目标针座 
    :param n: 初始针座上的盘子数
    :return: 
    '''
    if n == 1:
        print(a, '->', c)
    else:
        hanoi(a, c, b, n - 1)
        print(a, '->', c)
        hanoi(b, a, c, n - 1)


# 执行汉诺塔算法,初始基数为4
hanoi('a', 'b', 'c', 4)
