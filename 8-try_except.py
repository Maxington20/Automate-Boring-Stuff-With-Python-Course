def divby42(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('Error: You tried to divide by 0')

print(divby42(2))
print(divby42(0))
print(divby42(12))

print('how many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That\'s a lot of cats')
    elif int(numCats) < 0:
        print('You cannot have negative cats')
    else:
        print('That\'s not that many cats')
except ValueError:
    print('You did not enter a number')

