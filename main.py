import random

mystery_digit = random.randrange(101, 999)
print(mystery_digit)
global var

while True:
    print("")
    input_digit = int(input(">:"))
    mystery_digit_list = [int(x) for x in str(mystery_digit)]
    input_digit_list = [int(x) for x in str(input_digit)]
    # print(input_digit_list)
    # print(mystery_digit_list)

    b_print = 0
    for a in mystery_digit_list:
        if input_digit == mystery_digit:
            print("You Got it !! Voila")
            break

        elif a in input_digit_list and mystery_digit_list.index(a) == input_digit_list.index(a):
            print("Fermi", end=" ")
        # a = 400 , [ 3,0,0]
        elif a in input_digit_list and mystery_digit_list.index(a) != input_digit_list.index(a):
            print("pico", end=" ")

        elif mystery_digit != input_digit:

            if b_print == 0:
                b_print = 1
                print("Bagels")
