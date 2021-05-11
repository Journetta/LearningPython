#This times 10 by 3 which equals 30
#This is quite common in Python tests
print(10 * 3)
# ** = Power e.g (10 ** 3) which is 10 to the power of 3
#incrementing x by 3
x = 10
x = x + 3
print(x)
#ignore line 9 as this is resetting it for line 10-12
x = 10
#this is excatly what is on line 6
x += 3
print(x)
#x should be 16 after this, as the times happens first
y = 10 + 3 * 2
print(y)
#This will do 2+3 first which is 5, then times it by 10 = 50, and then minus 3.. which is 47
z = (2+3) * 10 - 3
print(z)

# THE ORDER OF OPERATIONS
#parenthesis takes priority e.g (sum) + 3 * 3 (sum is done first)
#explontiation 2**3
#multiplication or division e.g x or /
#addition or subtraction e.g + or -