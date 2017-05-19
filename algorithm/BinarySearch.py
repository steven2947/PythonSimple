#!/usr/bin/python3
#
# @Time    : 2017/5/19 下午4:08
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

def binary_search(arr, start, end, hkey):
    '''
    二分法查找
    
    在有序的非减顺序数组里,通过中间值的对比来快速找到目标值的位置
    折半搜索把区域减半,时间复杂度为O(log n)
    :param arr: 
    :param start: 
    :param end: 
    :param hkey: 
    :return: 
    '''

    if start > end:
        return -1

    mid = int(start + (end - start) / 2)
    if arr[mid] > hkey:
        return binary_search(arr, start, mid - 1, hkey)
    if arr[mid] < hkey:
        return binary_search(arr, mid + 1, end, hkey)

    return mid


print(binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 10, 7))
