text = "python java python react java python"

words = text.split()
print(words)

freq = {}

for word in words:
    if  word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1

print(freq)