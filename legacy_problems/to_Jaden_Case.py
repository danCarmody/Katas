# given a string as input, write it in a way that Jaden smith would write it.
def to_jaden_case(tweet):
    j_tweet = ""
    count = 0
    # Test 2 -- Empty string validation
    if tweet is "":
        return "No tweet made"
    # Test 1 -- input validation
    else:
        # Test 3 -- looking for empty string
        for i in range(0, len(tweet)):
            if i is 0:
                tweet = tweet.replace(tweet[i], tweet[i].upper())
            elif tweet[i] is " ":
                tweet = tweet.replace(tweet[i+1], tweet[i+1].upper())
        return tweet


print to_jaden_case("")
print to_jaden_case("foo bar")
print to_jaden_case("Snafu Bar")
print to_jaden_case("here's looking to you kid")
print to_jaden_case("onlY thE hillS havE eyeS")
print to_jaden_case("How can mirrors be real if our eyes aren't real")