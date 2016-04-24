#!/bin/python
# -*- coding: utf-8 -*-
import itertools


def choose_n_from_list(n, my_list):
    return tuple(itertools.combinations(my_list, n))

n = 2
my_list = 'abc'
print choose_n_from_list(n, my_list)
my_list = [1, 2, 3]
print choose_n_from_list(n, my_list)
