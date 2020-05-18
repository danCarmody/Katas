def longest_consec(strarr, k):
    consec_string = []
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    else:
        for i in range(0, len(strarr)-(k - 1)):
            temp_string = ""
            for j in range(0, k):
                temp_string += strarr[i+j]
            consec_string.append(temp_string)

        max_consec = consec_string[0]
        for i in range(1, len(consec_string)):
            if (len(consec_string[i]) > len(max_consec)):
                max_consec = consec_string[i]

    return max_consec


