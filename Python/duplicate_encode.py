# The goal of this exercise is to convert a string to a new string where
# each character in the new string is "(" if that character appears only
# once in the original string, or ")" if that character appears more than
# once in the original string. Ignore capitalization when determining if
# a character is a duplicate.

def duplicate_encode(word):
    new_word = ""
    aux_word = word.casefold()
    repeated_letters = []
    while len(aux_word) > 0:
        aux_letter = aux_word[0]
        aux_word = aux_word.replace(aux_letter, '', 1)
        if aux_letter in aux_word:
            repeated_letters.append(aux_letter)
    for letter in word.casefold():
        if letter in repeated_letters:
            new_word += ")"
        else:
            new_word += "("
    return new_word
print(duplicate_encode("test"))