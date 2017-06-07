#!/usr/bin/python3
#
# @Time    : 2017/5/23 下午4:25
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

def insert_sort(list):
    '''
    插入排序
    
    就是将一个无序的数组整理为有序的新数组
    在数组里面的第一个数据开始作为新的数组,然后之后的每个都按数值的大小排到新数组里
    时间复杂度为O(n^2)
    
    :return: 
    '''

    n = len(list)
    if n == 1: return list

    for i in range(1, n): # 从1开始,到n为止
        for j in range(i, 0, -1): # 从i开始到0为止,间隔为-1,就是倒序查找
            if list[j] < list[j - 1]: list[j], list[j - 1] = list[j - 1], list[j]
    return list


print(insert_sort([1, 2, 5, 2, 3, 6, 7, 3, 2, 1, 7, 8, 9, 0]))
