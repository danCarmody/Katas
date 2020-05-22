import re


def abbreviate(s):
    combo = re.findall(r"[\s]+|[\w]+|[.,!?;-]", s)
    for i in range(0, len(combo)):
        if len(combo[i]) > 3:
            temp_str = combo[i]
            temp_str = list(temp_str)
            first_let = temp_str[0]
            last_let = temp_str[len(temp_str)-1]
            let_remove = str(len(temp_str) - 2)
            combo[i] = str(first_let + let_remove + last_let)

    combo = "".join(combo)
    return combo


print(abbreviate("internationalization"))
print(abbreviate("accessibility"))
print(abbreviate("Accessibility"))
print(abbreviate("elephant-ride"))
print(abbreviate("elephant-rides are really fun!"))
