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