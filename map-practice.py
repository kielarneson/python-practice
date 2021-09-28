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


def number_plus_seven(array):
    numbers_plus_seven = map(lambda number: number + 7, array)
    return numbers_plus_seven


print(number_plus_seven(numbers))

#  5. Start with an array of strings and create a new array with each string's length.
#     For example, ["hello", "goodbye"] becomes [5, 7].


def string_length(array):
    words_length = map(lambda word: len(word), array)
    return words_length


print(string_length(words))

#  6. Start with an array of hashes and create a new array of number values from each hash's :age key.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [27, 16].

#  7. Start with an array of numbers and create a new array with each number divided by 2.
#     For example, [1, 2, 3] becomes [0.5, 1.0, 1.5].


def divided_by_two(array):
    numbers_divided_by_two = map(lambda number: number / 2.0, array)
    return numbers_divided_by_two


print(divided_by_two(numbers))

#  8. Start with an array of strings and create a new array with each string's first letter only.
#     For example, ["hello", "goodbye"] becomes ["h", "g"].


def first_letter(array):
    first_letters = map(lambda word: word[0], array)
    return first_letters


print(first_letter(words))

# 9.  Start with an array of hashes and create a new array of number values from each hash's :age key times 2.
#     For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [54, 32].

# 10. Start with an array of numbers and create a new array with each number converted into a string.
#     For example, [1, 2, 3] becomes ["1", "2", "3"].


def number_to_string(array):
    numbers_to_strings = map(lambda number: str(number), array)
    return numbers_to_strings


print(number_to_string(numbers))
