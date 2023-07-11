import random

print(list('12345678'))
num_list = list('1234567890')


num = random.sample(num_list, k=3)
mystery_digit = ""
for a in num:
    mystery_digit = a + mystery_digit

mys_digit = '943'
print(mys_digit)

while True:
    print("")
    str_dig = str(input(">:"))
    print(str_dig, type(str_dig))
    # for a in str_dig:
    #     print(a)

    # mys_digit = digit_number()
    print(type(mys_digit))

    if int(str_dig) == int(mys_digit):
        print("You Got It !! Voila")
    # elif str_dig not in list(str(mystery_digit)):
    #     print("Bagels")
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
