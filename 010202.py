# Using dictionary: O(n)
def isPermutation(a, b):
    c = {}
    for _ in a: c[_] = c.setdefault(_, 0) + 1
    for _ in b: c[_] = c.setdefault(_, 0) - 1
    return not any(c.values())

print(isPermutation('banana', 'abanan'))
print(isPermutation('banana', 'canana'))