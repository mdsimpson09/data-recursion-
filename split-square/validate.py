"""Validate that a given square is valid.

Checks that this is either a simple square (``0`` or ``1``), or
a split square (a list of 4 items, each being a simple square or
a split square).

A simple square is valid::

    >>> validate(0)
    True

A split square of four simple filled squares is valid::

    >>> validate([1, 1, 1, 1])
    True

We can nest split and simple squares::

    >>> validate([1, 0, [1, [0, 0, 0, 0], 1, [1, 1, 1, 1]], 1])
    True

    >>> validate([1, [1, 0, 1, [0, [0, 0, 0, 0], 1, 1]], [1, 0, 1, 0], 1])
    True

Simple squares must be either 0 (empty) or 1 (filled)::

    >>> validate(2)
    False

Split squares must contain exactly four parts::

    >>> validate([1, 1, 1, 1, 1])
    False

    >>> validate([1, 0, [1, [0, 0, 0, 0, 1], 1, [1, 1, 1, 1]], 1])
    False

    >>> validate([1, [1, 0, 1, [0, [0, 0, 0], 1, 1]], [1, 0, 1, 0], 1])
    False

"""


def validate(s):
    """Validate that a given square is valid."""
    # Check if s is a simple square
    if isinstance(s, int):
        return s == 0 or s == 1
    
    # Check if s is a split square
    if isinstance(s, list):
        # Split squares must contain exactly four parts
        if len(s) != 4:
            return False
        # Recursively validate each part of the split square
        return all(validate(part) for part in s)
    
    # If s is neither a simple square nor a split square, it's invalid
    return False

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS; THAT'S SUPER-VALID WORK!\n")
