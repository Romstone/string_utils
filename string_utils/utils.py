import re

def reverse_words(s: str) -> str:
    """
    Tier 1:
    Given an input string `s`, return a string in which the order
    of words is reversed, but each word’s letters stay in order.
    Words are separated by whitespace.
    Example: "hello world" → "world hello"
    """
    return ' '.join(s.split()[::-1])

def reverse_words_tier_2(s: str) -> str:
    """
    Tier 2:
    Extending reverse_words to:
    Raise TypeError if `s` is not a string.
    Preserve all whitespaces as they are like this: "\\\\tHello World\\\\n" -> "\\\\tWorld Hello\\\\n"
    """
    if type(s) is not str:
        raise TypeError('Input must be a string!')

    parts = re.findall(r'\s+|\S+', s)
    words = []
    for part in parts:
        if not part.isspace():
            words.append(part)
    reversed_words = words[::-1]

    reversed_string = ''
    counter = 0
    for part in parts:
        if part.isspace():
            reversed_string += part
        else:
            reversed_string += reversed_words[counter]
            counter += 1

    return reversed_string