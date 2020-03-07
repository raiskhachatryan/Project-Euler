"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(string):
    if string == string[::-1]:
        return True

lst = [i*j for i in range(900,1000)
        for j in range(900, 1000)
        if is_palindrome(str(i*j))]

def largest_palindrome():
    large = lst[0]
    for i in lst:
        if i > large:
            large = i
    return large
print(largest_palindrome())






