def dismemvowel(string):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for i in vowels:
        string = string.replace(i, "")

    return string


# ----------------------------------------------------------------------------------------------------------------------
print dismemvowel("hello world")
print dismemvowel("she sells sea shells")
print dismemvowel(" ")
print dismemvowel("This website is for losers LOL!")
