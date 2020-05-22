def rot13(message):

    encoded_msg = message
    decoded_msg = ""

    for indx in range(len(encoded_msg)):
        print(ord(encoded_msg[indx]))
        if (ord(encoded_msg[indx]) >= 65 and ord(encoded_msg[indx]) <= 77):
            decoded_msg += (str(chr(ord(encoded_msg[indx]) + 13)))
            print(len(decoded_msg))
        
        if(ord(encoded_msg[indx]) >= 78 and ord(encoded_msg[indx]) <= 90):
            decoded_msg += (str(chr(ord(encoded_msg[indx]) - 13)))
        if (ord(encoded_msg[indx])>= 97 and ord(encoded_msg[indx])<= 122):
            decoded_msg += (str(chr(ord(encoded_msg[indx]) )))

        else:
            decoded_msg += encoded_msg[indx]

        print(len(decoded_msg))

    return decoded_msg

print("initial amount", len("EBG13 rknzcyr.\n"))
print(rot13("EBG13 rknzcyr."))
