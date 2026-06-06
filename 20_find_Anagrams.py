# Easy way but interviewers wont look for this solution

# word1 = "listen"
# word2 = "silent"

# word1 = word1.lower()
# word2 = word2.lower()

# if sorted(word1) == sorted(word2):
#     print(True)
# else:
#     print(False)

# Alternate

word1 = "listen"
word2 = "silent"

word1 = word1.lower()
word2 = word2.lower()

freq1 = {}
freq2 = {}

for ch in word1:
    freq1[ch] = freq1.get(ch,0) + 1
    
    # if ch not in freq1:
#       freq1[ch] = 1
#     else:
#       freq1[ch] += 1
    

for ch in word2:
    freq2[ch] = freq2.get(ch, 0) + 1

print(freq1 == freq2)