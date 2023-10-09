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
