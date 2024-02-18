import random

# A.
# 1. Create two variables name X and Y.
# 2. Print “BIG” if X is bigger than Y .
# 3. Print “small” if X is smaller than Y.
X = 7
Y = 5
if X > Y:
    print("BIG")
else:
    print("small")

########################################
# B.
# 1. Run a “for” loop 5 times.
# 2. Print iteration number every time.
for i in range(5):
    print(i)

########################################
# C.
# 1. Create a variable and initialize it with a number 1-4.
# 2. Create 4 conditions (if-elif) which will check the variable.
# 3. print the season name accordingly:
#
# - 1 = summer
# - 2 = winter
# - 3 = fall
# - 4 = spring
season_number = random.randint(1, 4)
if season_number == 1:
    print("summer")
elif season_number == 2:
    print("winter")
elif season_number == 3:
    print("fall")
elif season_number == 4:
    print("spring")
else:
    print("No such season :)")


########################################
# D.
# 1. how many times will the following loop run? - 11 times
# 2. what will be printed last? - 10


# E.
# Write a program with variables holding the following:
# 1. Your age.
# 2. First letter of your last name.
# 3. Current shekels-dollar currency.
# 4. Did you flew abroad (true/false)
# 5. Your apartment number.
#
# ● Print all variables.
# ● Add the currency to your age, and check the result.
age = 55
last_name_first_letter = "s"
nis_usd = 3.64
was_abroad = True
apartment = 32
print(age)
print(last_name_first_letter)
print(nis_usd)
print(was_abroad)
print(apartment)
print(age + nis_usd)


# F.
#
# Create a program which uses input with the following:
# 1. Ask user for his phone number
# 2. Print the words “phone number” and the phone number the
# user entered.
phone_num = input("What's your phone number: ")
print("phone number: %s" % phone_num)


# G.
#
# Write a program with the following:
# 1. Method named printHello() that prints the word “hello”.
# 2. Method named calculate() which adds 5+3.2 and prints the
# result.
def print_hello():
    print("hello")


def calculate():
    print(5+3.2)


# H.
# Write a program with the following:
# 1. Method that receive your name and prints it.
# 2. Method that receive a number, divide it by 2, and prints the
# result.
def what_is_your_name():
    name = input("What is your name? :")
    print(name)


def divide_by_two(number):
    print(number / 2)


# I.
# Write a program with the following:
# 1. Method that receive two numbers, add them, and return the
# sum.
# 2. Method that receive two Strings, add space between them,
# and return one spaced string.
def add(x, y):
    return x + y


def concatenate(a, b):
    return "%s %s" % (a, b)


# K.
# Create a nested for loop (loop inside another loop) to create
# a pyramid shape:
for i in range(1, 6):
    output = ""
    for j in range(i):
        output += "*"

    print(output)


# L.
#
# Create a nested for loop to create X shape (width is 7,
# length is 7):
size = 7  # Size of the X shape

for row in range(size):
    for col in range(size):
        if row == col or row + col == size - 1:
            print('#', end='')
        else:
            print(' ', end='')
    print()


# M.
# Write a program with the following:
# 1. Method that gets a number from the user (using input).
# 2. Method that receive the number from the first method, and
# computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7)
def get_user_input():
    while True:
        try:
            value = input("Enter integer number:")
            number = int(value)
            return number
        except ValueError:
            print("Please enter a valid number.")


def sum_user_input_digits(number):
    summ = 0
    number = abs(number)
    while number:
        summ += number % 10
        number //= 10

    return summ


print(sum_user_input_digits(get_user_input()))
