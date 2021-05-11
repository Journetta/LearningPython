#formatted strings
first = 'John'
last = 'Doe'
#This works but isn't that optimized
message = first + ' [' + last + '] is a coder'
#this is a more optimized way of doing it
msg = f'{first} [{last}] is a coder!'
print(msg)

course = 'Python For Beginners'
#len counts how many characters in a input field (but it's not limited to only that as it's general)
print(len(course))
#meta (when a function belongs to a specfic object it's a meta)
#This changes the 'Python for Beginners' to 'PYTHON FOR BEGINNERS'
print(course.upper())
#lower case
print(course.lower())
#orignal not modified
print(course)
#will return the index of the letter first character (starts at 0) (-1 means it's not found)
print(course.find('P')) #P is character 0
#Beginners starts at index 11
print(course.find('Beginners'))
#This replaces Beginners with Absolute Beginners
print(course.replace('Beginners', 'Absolute Beginners'))
#This will replace the P with a J (Jython For Beginners)
print(course.replace('P', 'J'))
#This should reply 'TRUE' As it's looking for the word "Python" in the course variable
# (but if it's a lower case instead of a upper case, then it'll return false)
print('python' in course)

#len function = number of characters in a string (general purpose)
#meta includes, upper, lower, title,find,replace
#in operator ('...) in (string)
