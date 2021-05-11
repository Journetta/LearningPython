#True OUTPUT = It's a hot day, Enjoy your day, FALSE OUTPUT = ENjoy your day
is_hot = False
is_cold = False

#Will be ignored if is_hot is False
if is_hot:
    #Double quotes = allows ' in the string
    print("It's a hot day")
    print("Drink plently of water")
    #elif = else if
    #Will be ignored if is_cold is false
elif is_cold:
    print("It's a cold day")
    print("Wear warm Clothes")
#this will be executed if is_hot or is_cold is not true
else:
    print("It's neither warm or cold")
#Shift + tab moves the indent back
#Always going to see this message
print("Enjoy your day")