name = ""
while name != 'your name':
    print('Please type your name')
    name = input()
print('thank you')

spam = 0
while spam < 5:
    spam += 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))