"""Print each square on a new line.

A simple square will only be one line::

    >>> dump(0)
    0

    >>> dump(1)
    1

A split square will use four lines::

    >>> dump([0, 1, 0, 1])
    0
    1
    0
    1

A nested split square will use one line per square::

    >>> dump([0, 0, 0, [1, 1, 1, 1]])
    0
    0
    0
    1
    1
    1
    1

Of course, these can nested deeply and still work::

    >>> dump([0, 0, 0, [1, 1, 1, [0, 0, 0, [1, 1, 1, 1]]]])
    0
    0
    0
    1
    1
    1
    0
    0
    0
    1
    1
    1
    1
"""


def dump(s):
    """Print each square on a new line."""
    if isinstance(s, int):
        # Base case: s is a simple square, print it
        print(s)
    elif isinstance(s, list):
        # Recursive case: s is a split or nested square, iterate and dump each element
        for element in s:
            dump(element)

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS; NICE JOB!\n")


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS; NICE JOB!\n"
