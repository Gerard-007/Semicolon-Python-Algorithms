
def vowel_consonant(word):
    vowels = ["a", "e", "i", "o", "u"]
    result = False
    for v in vowels:
        result = True if v in list(word) else False
    return result


print(vowel_consonant("This is a test"))