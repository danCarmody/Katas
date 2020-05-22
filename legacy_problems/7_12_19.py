# Spinning Words
def spinning_words(statement):
    spin_statement = ""
    raw_words = statement.split()
    for i in range(0, len(raw_words)):
        if len(raw_words[i]) >= 5:
            raw_words[i] = (raw_words[i])[::-1]

        if i < len(raw_words):
            spin_statement += (raw_words[i] + " ")
        else:
            spin_statement += (raw_words[i])

    return spin_statement


print(spinning_words("Hey fellow warriors"))
print(spinning_words("This is a test"))
print(spinning_words("This is another test"))

