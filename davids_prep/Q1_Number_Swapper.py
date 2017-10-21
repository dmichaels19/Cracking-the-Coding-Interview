"""
Write a function to swap a number in place (that is without temporary
variables).
"""

a = 5436
b = -123

a = a ^ b
# 'a' is now a^b

b = ~ (a ^ b)
# So ~ ( (a^b) & b)
# (a^b) & b would be all the bits that are not in a
# so the negation of that would be everything that is in a


# Same logic
a = (a ^ b)

# Something Something Twos Complement
a = ~a
b = ~b

print('a: ' + str(a))
print('b: ' + str(b))
