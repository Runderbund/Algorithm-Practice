def print_duplicates(string):
    # Makes a set for seen characters, cannot contain duplicates
    seen_chars = set()
    # Makes a dictionary of duplicate characters and their count
    duplicate_chars = {}
    for char in string:
        if char in seen_chars:
            if char in duplicate_chars:
                duplicate_chars[char] += 1
            else:
                duplicate_chars[char] = 2
        else:
            seen_chars.add(char)
    if len(duplicate_chars) > 0:
        print("Duplicate characters in the string:")
        for char, count in duplicate_chars.items():
            print(f"{char}: {count} times")
    else:
        print("No duplicate characters found in the string.")
print_duplicates("Hello World!")
print_duplicates("Hello, hello, World!")

def reverse_recursive(string):
    if len(string) == 0:
        return string
    else:
        return reverse_recursive(string[1:]) + string[0]
print(reverse_recursive("Hello World!"))
print(reverse_recursive("Hello, hello, World!"))

def count_vowels_consonants(string):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    for char in string.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return {"vowels": vowel_count, "consonants": consonant_count}
print(count_vowels_consonants("Hello World!"))
print(count_vowels_consonants("The quick brown fox jumps over the lazy dog."))

# Assumes numerical values are separated by spaces and should be counted as a single value 
def sum_numerical_values(string):
    total = 0
    for word in string.split():
        if word.isnumeric():
            total += int(word)
    return total
print(sum_numerical_values("The quick brown 123 fox jumps over the 456 lazy dog."))

# Treats numerical values as individual characters and sums them
def sum_numerical_values_alt(string):
    total = 0
    for char in string:
        if char.isnumeric():
            total += int(char)
    return total
print(sum_numerical_values_alt("The quick brown 123 fox jumps over the 456 lazy dog."))

def difference_from_15(num):
    diff = abs(num - 15)
    if diff > 10:
        return diff * 2
    else:
        return diff
print(difference_from_15(-10))
print(difference_from_15(10))

# Assumes words are at least 2 characters long
def pig_latin_converter(string):
    words = string.split()
    pig_latin_words = []
    for word in words:
        pig_latin_word = word[1:] + word[0] + "ay"
        pig_latin_words.append(pig_latin_word)
    return " ".join(pig_latin_words)
print(pig_latin_converter("The quick brown fox"))
print(pig_latin_converter("Hello World!"))

def largest_numeric_value(lst):
    max_num = None
    for num in lst:
        if isinstance(num, (int, float)):
            if max_num is None or num > max_num:
                max_num = num
    return max_num
print(largest_numeric_value([1, 2, 3, "four", 5.0, 6]))
print(largest_numeric_value(["one", "two", "three"]))

def largest_numeric_value_alt(lst):
    numeric_lst = [num for num in lst if isinstance(num, (int, float))]
    if not numeric_lst:
        return None
    return max(numeric_lst)
print(largest_numeric_value_alt([1, 2, 3, "four", 5.0, 6]))
print(largest_numeric_value_alt(["one", "two", "three"]))

# Treats repeat letters as the same
# E.g., "abb" wil not have "bab" twice 
from itertools import permutations
def all_permutations(string):
    return set(''.join(p) for p in permutations(string))
print (all_permutations("BAB"))
print(all_permutations("hello"))