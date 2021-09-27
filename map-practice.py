#  1. Start with an array of numbers and create a new array with each number times 3.
#     For example, [1, 2, 3] becomes [3, 6, 9].

numbers = [1, 2, 3]


def number_times_three(array):
    numbers_times_three = map(lambda number: number * 3, array)
    return numbers_times_three


print(number_times_three(numbers))

#  2. Start with an array of strings and create a new array with each string upcased.
#     For example, ["hello", "goodbye"] becomes ["HELLO", "GOODBYE"].

words = ["hello", "goodbye"]


def uppercase(array):

    uppercase_words = map(lambda string: string.upper(), array)
    return uppercase_words


print(uppercase(words))

#  3. Start with an array of hashes and create a new array of string values from each hash's :name key.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes ["Alice", "Blane"].


#  4. Start with an array of numbers and create a new array with each number plus 7.
#     For example, [1, 2, 3] becomes [8, 9, 10].

numbers = [1, 2, 3]


def number_plus_seven(array):
    numbers_plus_seven = map(lambda number: number + 7, array)
    return numbers_plus_seven


print(number_plus_seven(numbers))
