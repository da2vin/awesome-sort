#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
基数排序（radix sort）属于“分配式排序”（distribution sort），又称“桶子法”
（bucket sort）或bin sort，顾名思义，它是透过键值的部份资讯，将要排序的元素
分配至某些“桶”中，藉以达到排序的作用，基数排序法是属于稳定性的排序，其时间
复杂度为O (nlog(r)m)，其中r为所采取的基数，而m为堆数，在某些时候，基数排序法
的效率高于其它的稳定性排序法。
'''

import random, timeit


def _counting_sort(A, i):
    """计数排序，以i位进行排序，以适用于基数排序。
    Args:
        A (Sequence): 排序数组
        i (int): 位数，从0开始而不是1
    """
    C = [0] * 10  # 任意位值范围为[0,9]
    A = [(a / (10 ** i) % 10, a) for a in A]  # 元素i位值及其自身的元组的数组
    for k, a in A:
        C[k] = C[k] + 1
    for i in xrange(1, 10):
        C[i] = C[i] + C[i - 1]
    B = [0] * len(A)  # 结果数组
    for k, a in A[::-1]:
        B[C[k] - 1] = a
        C[k] = C[k] - 1
    return B


def radix_sort(A, d):
    """基数排序，从最低位进行排序直到最高位：
    RADIX-SORT(A, d)
    1  for i ← 1 to d
    2    do use a stable sort to sort array A on digit i

    Args:
        A (Sequence): 排序数组
        d (int): 最大数位数
    """
    for i in xrange(d):  # 遍历位数，从低到高
        A = _counting_sort(A, i)
    return A


def rsort(A, d):
    """基数排序（桶排序版本）"""
    for i in xrange(d):  # 遍历位数，从低到高
        S = [[] for _ in xrange(10)]  # 存放[0,9]位数值所对应元素（[0-9]10个桶）
        for a in A:  # 遍历元素
            S[a / (10 ** i) % 10].append(a)  # 存放对应位数值的元素（元素当前位值在哪个桶就放进去）
        A = [a for b in S for a in b]  # 以当前位数值排序好的A（依次从各桶里把元素拿出来）
    return A


if __name__ == '__main__':

    items = range(10000)
    random.shuffle(items)


    def test_sorted():
        print(items)
        sorted_items = sorted(items)
        print(sorted_items)


    def test_radix_sort():
        print(items)
        sorted_items = radix_sort(items, 4)  # [0,9999]，4位数
        print(sorted_items)


    test_methods = [test_sorted, test_radix_sort]
    for test in test_methods:
        name = test.__name__  # test.func_name
        t = timeit.Timer(name + '()', 'from __main__ import ' + name)
        print(name + ' takes time : %f' % t.timeit(1))
