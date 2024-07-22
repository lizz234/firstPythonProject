# name = "Aliza"
# age = 22
# second_name = "Wasi"
#
# print(name + " " + str(age) + "\n" + second_name)
# print(second_name.upper())
# print(len(name))
# print(name.index("z"))
#
# print("aliza hamid".isdigit())
# print("11".isdecimal())
#
#
# print(pow(3,2))
# from math import *
# print(floor(790.3))
# print(ceil(4.7))
#
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)


def sayHi():
    print("Hello User")

def cube(num):
    return num*num*num

print(cube(3))



is_male = False
is_tall = True


if is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are tall but not male")
elif is_male and is_tall:
    print("You are a tall male")
else:
    print("You are neither male nor tall")