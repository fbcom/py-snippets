#!/bin/python

def powerset(simple_set):
    """
    + computes the powerset of a set
    + actually we'll be using lists to store the sets
    """
    powerset = [[]]  # include the empty set
    for element in simple_set:  # gradually build the powerset
        powerset += [subset + list(element) for subset in powerset]
    return powerset

# dest
for n in range(5):
    simple_set = map(lambda x: str(x), range(n))  # convert ints to strings
    power_set = powerset(simple_set)
    assert(len(power_set) == 2**n), "Testcase failed"
    print len(power_set), power_set
