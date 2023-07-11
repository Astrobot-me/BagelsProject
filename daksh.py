from time import sleep
from random import randrange

a = input('Please enter your name sir.')
print(''' Dear %s , Welcome to "Bagels" (a deductive logic game.). ''' % (a.title()))
print('''In this game you must guess a three-digit number based on clues \n The game offers one of the following 
hints in response to your guess. \n “Pico” when your guess has a correct digit in the wrong place \n “Fermi” when 
your guess has a correct digit in the correct place \n and “Bagels” if your guess has no correct digits \n You have 
10 tries to guess the secret number''')
print('The game will start in 10 seconds best of luck \n Dont worry the computer is not laggy the program is coded in '
      'this way ;)')
sleep(10)


def random():  ## generates a random 3 digit number.n and stores it in variable b
    global b
    b = randrange(100, 1000)  # randomly generated 3 digit number for the game.


def repetation():  # # checks if there is repetation in the radomly generated number if it is then it generates
    # random number again.
    global c
    for i in c:
        if c.count(i) > 1:
            c = []
            random()
            storinginlist(c, b)
            repetation()


def storinginlist(l, n):  ## function that helps stores that data in the empty lists c and d
    while int(n) / 10 > 0:
        d = int(n) % 10
        l.append(d)
        n = int(n) / 10
    l.reverse()


def input__user():  ## takes the input from user and stores it in d)
    e = int(input('Take a guess , What number is it ?. You have %d chances left.' % (chances)))
    storinginlist(d, e)


chances = 10
z = 0
b = 0
while True:
    if chances == 10:
        random()
    c = []  # c is the list in which the randomly generated number will get stored.
    d = []  # d is the list in which the user inputted number gets stored.
    storinginlist(c, b)
    repetation()
    input__user()
    chances = chances - 1
    ## Here comes the juice you were waiting for : The logic
    e = 0
    f = 0  ## check for the bagel.
    while e <= 2:
        if c[e] in d:
            if c[e] == d[e]:
                print('Fermi')
                e = e + 1
                z = z + 1
            else:
                print('Pico')
                e = e + 1
        elif c[e] not in d:
            f = f + 1
            e = e + 1
    if f == 3:
        print('Bagels')
    if z == 3:
        print('You won the game.')
        k = input('DO you want to play the game again ? y/n')
        if k == 'y' or k == 'yes' or k == 'YES' or k == 'Yes':
            chances = 10
            z = 0
        elif k == 'n' or k == 'no' or k == 'NO' or k == 'No':
            print(
                'Thank you for playing our game. Please contact our deputy programmer in case of bugs (Mr. Aditya Raj)')
            break
    z = 0
    e = 0
    if chances == 0:
        print('oh-ho You lose the game.')
        k = input('DO you want to play the game again ? y/n')
        if k == 'y' or k == 'yes' or k == 'YES' or k == 'Yes':
            chances = 10
            z = 0
        elif k == 'n' or k == 'no' or k == 'NO' or k == 'No':
            print(
                'Thank you for playing our game. Please contact our deputy programmer in case of bugs (Mr. Aditya Raj)')
            break
exit()
