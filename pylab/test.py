def isAlphabeticalWord(word, wordList=word):
    if (len(word) > 0):
        curr = word[0]
    for letter in word:
        if (curr > letter):
            return False
        else:
            curr = letter
    if wordList is None:
        return True
    return word in wordList
line = inFile.readline()
field = line.split()