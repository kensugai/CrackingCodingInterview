# Using dictionary
def isUnique(s): return len({_:1 for _ in s}) == len(s)

print(isUnique("abc"))
print(isUnique("abca"))
