def is_isogram(string):
    isogram = True
    for i in range(0, len(string)):
        for j in range(0, len(string)):
            if string[i].lower() == string[j].lower() and i != j:
                isogram = False
    return isogram


print is_isogram("Dermatoglyphics")
print is_isogram("isogram")
print is_isogram("aba")
print is_isogram("sees")
print is_isogram("FoO BaR")
