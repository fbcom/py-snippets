#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This implementation of mergesort does not sort in-place


def merge_sort(array):
    if len(array) <= 1:
        return array
    m = len(array)/2
    left_array = merge_sort(array[:m])
    right_array = merge_sort(array[m:])
    return merge(left_array, right_array)


def merge(left_array, right_array):
    ret = []
    i = j = 0
    while i < len(left_array) and j < len(right_array):
        while i < len(left_array) and j < len(right_array) and left_array[i] <= right_array[j]:
            ret.append(left_array[i])
            i = i + 1

        while i < len(left_array) and j < len(right_array) and left_array[i] >= right_array[j]:
            ret.append(right_array[j])
            j = j + 1

    while i < len(left_array):
        ret.append(left_array[i])
        i = i + 1

    while j < len(right_array):
        ret.append(right_array[j])
        j = j + 1

    return ret

array = [8, 2, 4, 9, 3, 6]
print "unsorted:", array
array = merge_sort(array)
print "  sorted:", array
