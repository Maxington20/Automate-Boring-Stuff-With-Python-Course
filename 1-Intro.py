# Just fucking around in the python terminal

# Data types in Python
# ints
# floats
# string 
# boolean

# this program says hello and asks for my name

print("Hello World")
print("What is yoru name?")
myName = input()
print("It is good to mee you " + myName)
print("The length of your name is " + str(len(myName)))
print(len(myName))
print("What is your age?")
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.")

name = 'Alice'
if name == 'Alice':
    print('Hi Alice')
print('done')

password = 'swordfish'
if password == 'swordfish':
    print('access granted')
else:
    print('wrong password')