#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过
来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
'''


def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


if __name__ == '__main__':
    seq_ = [5, 6, 78, 9, 0, -1, 2, 3, -65, 12]
    print(bubble_sort(seq_))
