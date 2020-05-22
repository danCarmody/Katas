def duplicate_count(text):
    text_checker = sorted(set(list(text.lower())))
    num_duplicates = 0

    for i in range(0, len(text_checker)):
        if text.count(text_checker[i]) > 1:
            num_duplicates += 1

    return num_duplicates


print duplicate_count("abcde"), "\n"
print duplicate_count("abcdea"), "\n"
print duplicate_count("indivisibility"), "\n"
