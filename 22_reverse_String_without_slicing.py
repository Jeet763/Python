# s = "python"

# reversed_string = ""

# for ch in s:
#     reversed_string  = ch + reversed_string

# print(reversed_string)

# Better interview Solution

s = "python"

chars = list(s)

left = 0
right = len(chars) - 1 

while left < right:
    chars[left] , chars[right] = chars[right] , chars[left]

    left +=1
    right -=1

print(",".join(chars))