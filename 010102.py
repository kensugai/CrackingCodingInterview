# Without additional data structure
def isUnique(s):
    if (len(s) < 2):
        return True
    elif (s[0] in s[1:]):
        return False
    else:
        return isUnique(s[1:])

print(isUnique("abc"))
print(isUnique("abca"))
