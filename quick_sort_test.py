#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分
的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以
递归进行，以此达到整个数据变成有序序列。
'''


def quick_sort(seq):
    # 快速排序
    if seq == []:
        return []
    else:
        pivot = seq[0]
        lesser = quick_sort([x for x in seq[1:] if x < pivot])
        greater = quick_sort([x for x in seq[1:] if x >= pivot])
        return lesser + [pivot] + greater


if __name__ == '__main__':
    seq_ = [5, 6, 78, 9, 0, -1, 2, 3, -65, 12]
    print(quick_sort(seq_))
