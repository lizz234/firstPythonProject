# print("Hello World")
#
# print("    /\\--------------------\\")
# print("   /  \\                    \\")
# print("  /    \\                    \\")
# print(" / [  ] \\                    \\")
# print("/________\\____________________\\")
# print("|        |                    |  ")
# print("|        |                    |  ")
# print("|        |                    |  ")
# print("|        |                    |  ")
# print("|________|____________________|  ")

# character_name = "Tom"
# character_age = "50"
#
# print("There once was a man named " + character_name + ",")
# print("he was" + character_age + "years old.")
#
#
# character_name = "John"
#
# print("He really lliked the name" + character_name + ",")
# print("but didn't like being " + character_age + ".")


def min_num(num1, num2, num3, num4):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3

# print(min_num(45,76,23,90))

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# print("Done with loop")
#
# for index in range(5):
#     if index == 0:
#         print("First Iteration")
#     else:
#         print("Not First")
#
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
# print(raise_to_power(4, 2))


new_file = open(r'C:\Users\MSI\OneDrive\Desktop\Following.txt', "r")
print(new_file.read())
new_file.close()