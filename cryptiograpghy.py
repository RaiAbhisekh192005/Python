def machine():
    keys="""abcdefghijklmonpqrstuvwxyz !@#$%^&*()_+|/><;:"""
    value=keys[-1] + keys[0:-1]
    
    encryptDict=dict(zip(keys, value))
    decryptDict=dict(zip(value, keys))
    
    message=input('Please enyer the sercret message: ')
    mode=input('Please enyer the mode Encode(E) OR Decode(D): ')

    if mode.upper()=='E':
        newMessage = ''.join([encryptDict[letter]
                            for letter in message.lower()])

    elif mode.upper()=='D':
        newMessage = ''.join([decryptDict[letter]
                            for letter in message.lower()])
    else:
        print('Please enter a correct choice')

    return newMessage.capitalize()

print(machine())
    
