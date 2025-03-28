s = "ASISH"

def subsequences(s, index = 0, current = ""):
    if index == len(s):
        return {current} if current else set()
    with_char = subsequences(s, index+1, current+s[index])
    without_char = subsequences(s, index+1, current)

    return with_char.union(without_char)

print(subsequences(s))
