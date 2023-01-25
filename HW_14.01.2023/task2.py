"""
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

KATA:
https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python
"""
# Solution

def sum_mix(arr):
    return sum(map(lambda i: int(i), arr))
