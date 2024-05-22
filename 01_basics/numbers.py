# from decimal import Decimal
import math

x = 2
y = 3
z = 4

print(x + y)
print(x, y, z)

print(repr('hello, world'))
str('hello, world')

math.floor(3.5)
print(math.trunc(3.5))

print(math.trunc(-3.5))    # shift number towards zero

print(0o20)
print(0x10)
print(0b10000)

print(oct(16))
print(hex(16))
print(bin(16))

print(int('53', 16))

x = 1
print(x << 2)     # bitwise shift left by 2
print(x | 2)      # bitwise OR with 2

import random
print(random.randint(1, 100))

li = [1, 2, 3]

print(random.choice(li))
random.shuffle(li)
print(li)

#################################################################################################

# print(0.1 + 0.1 + 0.1 - 0.3)
# print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

#################################################################################################
# Sets

setone = {1, 2, 3, 4, 5}
print(setone & {3, 4, 5, 6, 7})          # intersection
print(setone | {6, 7, 8, 9})              # union
print(setone - {3, 4, 5})                  # difference
print(setone ^ {3, 4, 5, 6, 7})            # symmetric difference, elements in either set but not both


