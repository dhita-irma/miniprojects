def matchingStrings(strings, queries):
    results = []
    for q in queries:
        occurence = 0
        for s in strings: 
            if s == q:
                occurence += 1
        results.append(occurence)
    return results


if __name__ == "__main__":
    strings = ["aba", "baba", "aba", "xzxb"]
    queries = ["aba", "xzxb", "ab"]

    print(matchingStrings(strings, queries))
