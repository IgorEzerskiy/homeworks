"""
Consider an array/list of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined

KATA:
https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
"""
# Solution


def count_sheeps(sheep):
    return sum(1 for i in sheep if i == True)
