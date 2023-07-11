import random

print(list('12345678'))
num_list = list('1234567890')


def digit_number():
    num = random.sample(num_list, k=3)
    mystery_digit = ""
    for a in num:
        mystery_digit = a + mystery_digit

    return mystery_digit


while True:
    mys_digit = digit_number()
    print(mys_digit)
    chanses = 10
    print("I thought Up a Number")

    while chanses > 0:

        print(f"Guess #{chanses}")
        str_dig = str(input(">:"))
        chanses = chanses-1
        # print(str_dig, type(str_dig))
        # # for a in str_dig:
        # #     print(a)

        if int(str_dig) == int(mys_digit):
            print("You Got It !! Voila")
            break

        elif set(str_dig).isdisjoint(set(mys_digit)) == True:
            print("Bagels")
        else:

            if str_dig[0] == mys_digit[0]:
                print("fermi", end=' ')
            elif str_dig[1] == mys_digit[0]:
                print("pico", end=' ')
            elif str_dig[2] == mys_digit[0]:
                print("pico", end=' ')

            if str_dig[0] == mys_digit[1]:
                print("pico", end=' ')
            elif str_dig[1] == mys_digit[1]:
                print("fermi", end=' ')
            elif str_dig[2] == mys_digit[1]:
                print("pico", end=' ')

            if str_dig[0] == mys_digit[2]:
                print("pico", end=' ')
            elif str_dig[1] == mys_digit[2]:
                print("pico", end=' ')
            elif str_dig[2] == mys_digit[2]:
                print("fermi", end=' ')

            print("")

    play = input("Do You want to Play Again(Yes/No)")
    if play.lower() == "yes":
        pass
    else:
        break

print("Thanks for Playing :)")