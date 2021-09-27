# 1. Write a function that takes in a number and returns the number times two. Then run the function and print the result.


def number_times_two(number):
    return number * 2


print(number_times_two(6))

# 2. Write a function that takes in a string and returns the string with all capital letters. Then run the function and print the result.


def capitalize(string):
    return string.upper()


print(capitalize('animal'))

# 3. Write a function that takes in two numbers and returns the first number subtracted by the second. Then run the function and print the result.


def subtract(num1, num2):
    return num1 - num2


print(subtract(10, 3))

# 4. Write a function that takes in a number and returns the number times itself. Then run the function and print the result.


def number_times_itself(number):
    return number * number


print(number_times_itself(10))

# 5. Write a function that takes in a string and returns the first letter of the string. Then run the function and print the result.


def first_letter(string):
    return string[0]


print(first_letter("animal"))

# 6. Write a function that takes in three strings and returns a string that combines all three strings with spaces in between. Then run the function and print the result.


def add_strings(str1, str2, str3):
    return '{} {} {}'.format(str1, str2, str3)


print(add_strings('animal', 'cake', 'melon'))

# 7. Write a function that takes in a number and returns the number as a string. Then run the function and print the result.


def number_to_string(number):
    return str(number)


print(number_to_string(9))

# 8. Write a function that takes in a string and returns the string repeated 5 times. Then run the function and print the result.


def repeat(string):
    index = 0
    while index < 5:
        print(string)
        index += 1


repeat('animal')

# 9. Write a function that takes in 3 numbers and returns the average (the sum divided by 3.0). Then run the function and print the result.

# 10. Write a function that takes in a number and returns the number times 10 plus 30. Then run the function and print the result.
