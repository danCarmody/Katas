def consec_test(arr, consec):
    consec_string = []
    if len(arr) == 0 or consec > len(arr) or consec <= 0:
        return ""
    else:
        for i in range(0, len(arr)-(consec - 1)):
            temp_string = ""
            for j in range(0, consec):
                temp_string += arr[i+j]
            consec_string.append(temp_string)

        max_consec = consec_string[0]
        for i in range(1, len(consec_string)):
            if (len(consec_string[i]) > len(max_consec)):
                max_consec = consec_string[i]

    return max_consec

print(consec_test(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(consec_test(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
print(consec_test(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))