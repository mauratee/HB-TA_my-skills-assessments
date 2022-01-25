def does_string_contain_letter(letter, string):
    """Determine whether a given letter is in a string."""

    return letter in string

# O(n) - linear runtime
# Search an array - O(n)


def contain_letters_in_common(string1, string2):
    """Determine whether the two strings have any letters in common."""

    duplicates = []
    # duplicates will never get longer than 52
    for letter in string1: # -> O(n)
        if letter in string2: # -> O(n)
            if letter not in duplicates: # duplicates is relatively small
                duplicates.append(letter)

    return len(duplicates) > 0

# Total runtime - O(n)^2 -> O(n) nested


def letters_in_common(string1, string2):
    """Return a list of letters in common between two strings.
    If a letter appears more than once, the list should only contain the letter
    once.
    """

    # Time complexity of lookup in set: https://wiki.python.org/moin/TimeComplexity
    duplicates = set()
    string2 = set(string2)
    for letter in string1: # -> O(n)
        if letter in string2: # -> O(1)
            duplicates.add(letter)

    return list(duplicates)

# Total runtime - O(n)
