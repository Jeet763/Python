                               # 1 - Without using Slicing

# word = "madam"

# reversed_word = ""
 
# for ch in word:
#     reversed_word = ch + reversed_word

# if word == reversed_word:
#     print(True)
# else:
#     print(False)

                                 # 2- Two-Pointer Approach

word = "madam" 

left = 0 
right = len(word) - 1

is_palindrome = True

while left < right:
    if word[left] != word[right]:
        is_palidrome = False
        break

    left += 1 
    right -=1

print(is_palindrome)

