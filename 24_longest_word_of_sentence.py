# Taking input
Text= input("Enter a Sentence:")


def longest_word(Text):
    # Write your code here
    words = Text.split()
    longest_words = []
    max_len = 0

    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            longest_words = [word]
        elif len(word) == max_len:
            longest_words.append(word)

    return longest_words, max_len

longest_words, max_len = longest_word(Text)

if len(longest_words) == 1:
    print(f"'{longest_words[0]}'")
else:
    print(
        f"Both '{longest_words[0]}' and '{longest_words[1]}' have {max_len} characters, "
        f"which are the longest in the sentence. However, since '{longest_words[0]}' appears first, it is returned."
    )