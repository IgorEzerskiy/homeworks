"""
Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter
in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will
always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!

KATA:
https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python
"""
# Solution


def find_missing_letter(chars):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    chars = "".join(chars)
    if chars.isupper():
        alphabet = alphabet.upper()
    start = alphabet.find(chars[0])
    end = alphabet.find(chars[-1])
    alphabet = list(alphabet[start:end+1])
    for i in range(len(chars)):
        if chars[i] in alphabet:
            alphabet.remove(chars[i])
    return "".join(alphabet)
