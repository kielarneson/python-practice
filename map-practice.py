#  1. Start with an array of numbers and create a new array with each number times 3.
#     For example, [1, 2, 3] becomes [3, 6, 9].

numbers = [1, 2, 3]


def number_times_three(array):
    return map(lambda number: number * 3, array)


print(number_times_three(numbers))

#  2. Start with an array of strings and create a new array with each string upcased.
#     For example, ["hello", "goodbye"] becomes ["HELLO", "GOODBYE"].

words = ["hello", "goodbye"]


def uppercase(array):
    return map(lambda string: string.upper(), array)


print(uppercase(words))
