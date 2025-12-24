# Return the longest word in a given sentence
def longestWord(str):
    str_arr=str.split()
    if not str_arr:
        return ""
    longest=0
    longest_index=0
    for index,word in enumerate(str_arr):
        if len(word) > longest:
            longest = len(word)
            longest_index = index
    return str_arr[longest_index]


# Test cases
assert longestWord("The quick brown fox") == "quick"  # quick and brown both 5, returns first
assert longestWord("Hello world") == "Hello"  # both 5, returns first
assert longestWord("a bb ccc") == "ccc"
assert longestWord("single") == "single"
assert longestWord("") == ""  # empty string
assert longestWord("   ") == ""  # only spaces
assert longestWord("word with punctuation!") == "punctuation!"  # punctuation attached
assert longestWord("multiple   spaces") == "multiple"  # extra spaces ignored
assert longestWord("short longword here") == "longword"

print("All test cases passed!")

# dictionary
def longestWordDictImpl(sentence):
    word_lengths = {word: len(word) for word in sentence.split()}
    longest_word = ""
    longest_word_length = 0
    for key,value in word_lengths.items():
        if value > longest_word_length:
            longest_word = key
            longest_word_length = value
    return longest_word

print(longestWordDictImpl("The quick brown fox"))

# Test cases for longestWordDictImpl
assert longestWordDictImpl("The quick brown fox") == "quick"  # quick and brown both 5, returns first in dict order? Wait, dict order is insertion, so "The", "quick", "brown", "fox" -> "quick" first longer
assert longestWordDictImpl("Hello world") == "Hello"  # both 5, "Hello" first
assert longestWordDictImpl("a bb ccc") == "ccc"
assert longestWordDictImpl("single") == "single"
assert longestWordDictImpl("") == ""  # empty string, split() -> {}, longest_word remains ""
assert longestWordDictImpl("   ") == ""  # only spaces
assert longestWordDictImpl("word with punctuation!") == "punctuation!"  # punctuation attached
assert longestWordDictImpl("multiple   spaces") == "multiple"  # extra spaces ignored
assert longestWordDictImpl("short longword here") == "longword"

print("All test cases for longestWordDictImpl passed!")

# Optimized Version
def longestWordDictImpl(sentence):
    words = sentence.split()
    if not words:
        return ""
    return max(words, key=len)