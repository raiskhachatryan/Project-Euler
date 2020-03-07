'''
The sum of the squares of the first ten natural numbers is,

1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2=552=3025
Hence the difference between the sum of the squares
of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.
'''

n = 10
def difference():
    s1 = 0
    s2 = 0
    for i in range(1, n+1):
        s1 = s1 + i
        s2 = s2 + i**2
    return (s1**2  - s2)

print(difference())







