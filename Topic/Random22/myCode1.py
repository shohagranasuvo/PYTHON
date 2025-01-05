import random

com = random.randint(1, 100)


user = int(input('Give me a number from 1 to 100 = '))
print("Random number is " + str(com))

if com > user:
    print('Your input is smaller')
elif com == user:
    print('Both are same ')


else:
    print('Your input is large ')

