# Using sort: O(n*log(n))
def isPermutation(a, b): return sorted(a) == sorted(b)

print(isPermutation('banana', 'abanan'))
print(isPermutation('banana', 'canana'))