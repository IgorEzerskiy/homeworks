"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order
of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
KATA:
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
"""
# Solution


def move_zeros(lst):
    lst_zero = [i for i in lst if i == 0]
    for i in range(len(lst_zero)):
        lst.remove(lst_zero[i])
    for i in lst_zero:
        lst.append(i)
    return lst
