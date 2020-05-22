def duplicate_encode(word):
    word = list(word.lower())
    mul_stack = []
    encoder = ""

    for i in range(0, len(word)):
        if word.count(word[i]) > 1 and word[i] not in mul_stack:
            mul_stack.append(word[i])

    for j in range(0, len(word)):
        if word[j] in mul_stack:
            encoder += ")"
        else:
            encoder += "("
    return encoder


print duplicate_encode("din")
print duplicate_encode("recede")
print duplicate_encode("Success")
print duplicate_encode("(( @")
