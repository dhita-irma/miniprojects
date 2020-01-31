from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # Split strings per line
    lines_a = a.split("\n")
    lines_b = b.split("\n")

    # Compare lines in both strings
    return [line for line in lines_a if line in lines_b]


def sentences(a, b):
    """Return sentences in both a and b"""

    # Split string per sentence
    sntnces_a = set(sent_tokenize(a))
    sntnces_b = set(sent_tokenize(b))

    # Compare both sentences
    return [sentence for sentence in sntnces_a if sentence in sntnces_b]


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # Set
    substr_a = set()
    substr_b = set()

    # Split string per substring in the length of n
    if n <= len(a) and n <= len(b):
        for i in range(len(a)-n+1):
            substr_a.add(a[i:i+n])

        for i in range(len(b)-n+1):
            substr_b.add(b[i:i+n])

    # Compare both substring
    return [s for s in substr_a if s in substr_b]
