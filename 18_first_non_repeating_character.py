s = "aabbcdde"

freq = {}

for ch in s:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1

print(freq)

for ch in s :
    if freq[ch] == 1:
        print(ch , "is the first non repeating character")
        break