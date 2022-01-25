def does_string_contain_letter(letter, string):
    """Determine whether a given letter is in a string."""

    return letter in string


def contain_letters_in_common(string1, string2):
    """Determine whether the two strings have any letters in common."""

    duplicates = []
    for letter in string1:
        if letter in string2:
            if letter not in duplicates:
                duplicates.append(letter)

    return len(duplicates) > 0


def letters_in_common(string1, string2):
    """Return a list of letters in common between two strings.
    If a letter appears more than once, the list should only contain the letter
    once.
    """

    duplicates = set()
    string2 = set(string2)
    for letter in string1:
        if letter in string2:
            duplicates.add(letter)

    return list(duplicates)
