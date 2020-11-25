from collections import Counter

def findTheDifference( s: str, t: str) -> str:
    return list(Counter(t) - Counter(s))[0]


print(findTheDifference("hello", "abou"))