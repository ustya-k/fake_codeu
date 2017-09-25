# -*- coding: utf-8 -*-


def is_a_permutation(string1, string2):
    """
    Given two strings, finds out, if a one string is a
    permutation of the other.

    Args:
            * string1 (string)
            * string2 (string)

    Returns:
            * True, if the first string is a permutation
            of the other.
            * False, if vice versa.
    """

    if not isinstance(string1, str) or not isinstance(string2, str):
        raise ValueError('Input must be string!')

    char_set1 = sorted(string1.lower())
    char_set2 = sorted(string2.lower())

    if char_set1 == char_set2:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
