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