import random
#
print(list('12345678'))
num_list = list('1234567890')


def digit_number():
    num = random.sample(num_list, k=3)
    mystery_digit = ""
    for a in num:
        mystery_digit = a + mystery_digit

    return mystery_digit


num = digit_number()
print(set(num))

# print(num)
# for i in num:
#     print(i)
#
# print(num[1])
# string = '022'
#
# i = input(">:")
# print(i[0])



