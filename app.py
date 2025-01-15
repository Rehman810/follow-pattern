def followPattern(pattern, s):
    words = s.split()
    # Check the length of pattern and word, if it is not equal return False
    if len(pattern)!= len(words):
        return False
    # Initialize dictionaries by hash map
    charToWord = {}
    wordToChar = {}
    # Iterate over words and pattern
    for char, word in zip(pattern, words):
      # Check if character is already mapped to a word
        if char in charToWord:
          if charToWord[char]!= word:
                return False
        else:
            charToWord[char] = word
            # Check if word is already mapped to a character
        if word in wordToChar:
            if wordToChar[word]!= char:
                return False
        else:
            wordToChar[word] = char
    # Return True if no issue
    return True

print(followPattern("abba", "dog cat cat dog" ))
print(followPattern("abba", "dog cat cat fish" ))
print(followPattern("aaaa", "dog cat cat dog" ))
print(followPattern("abc", "1 2 3" ))