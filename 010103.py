# Using bit vector
import BitVector
def isUnique(s):
    v = BitVector(size=256)
    for _ in s: v[_] = 1
    return v.count_bits() == len(s)

print(isUnique("abc"))
print(isUnique("abca"))
