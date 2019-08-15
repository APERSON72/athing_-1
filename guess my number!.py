import random
while True:
    x = random.randint(0,10)
    y = input('guess my number! It is in between 0 and 10.')
    print (y)
    print (x)
    if x==y:
        print('correct!')
    else:
        print('wrong!')