"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns
the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

KATA:
https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
"""
# Solution


def array_diff(a, b):
    if a != []:
        for i in range(len(b)):
            if b[i] in a:
                for k in range(a.count(b[i])):
                    a.remove(b[i])
        return a
    else:
        return a
