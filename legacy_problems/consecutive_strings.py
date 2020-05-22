# Consecutive Strings
# July 14th, 2019

#


def longest_consec(starr, k):
    consec_string = ""

    if len(starr) == 0 or k > len(starr) or k <= 0:
        return ""
    else:

        starr.sort(key=len, reverse=True)
        temp_string = ""
        for i in range(0, len(starr)):
            for j in range(0, k):
                temp_string += starr[j]
            if len(temp_string) > len(consec_string):
                consec_string = temp_string
            temp_string = ""

    for i in range(0, k):
        consec_string += starr[i]
    return consec_string


print(longest_consec([], 3))
print("---------------------------------------------------------------------------------------------------------------")
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print("---------------------------------------------------------------------------------------------------------------")
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
print("---------------------------------------------------------------------------------------------------------------")
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2))
print("---------------------------------------------------------------------------------------------------------------")
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))
print("---------------------------------------------------------------------------------------------------------------")
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2))
print("---------------------------------------------------------------------------------------------------------------")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
print("---------------------------------------------------------------------------------------------------------------")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15))
print("---------------------------------------------------------------------------------------------------------------")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0))
