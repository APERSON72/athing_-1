import random, sys
end = 0
wins = 0
while True:
    x = random.randint(0,10)
    y = input('guess my number! It is in between 0 and 10.')
    print (y)
    print (x)
    if int(x)==int(y):
        print('correct! You win!')
        wins += 1
        print('you have ' + str(wins) + ' wins!')
    else:
        print('wrong!')
        end += 1
    if end == 5:
        print('you lose!')
        sys.exit()