# Reverse Cipher


# message = input('Please enter the message you want to encrypt: >>>')
message = 'Three can keep a secret, if two of them are dead.' #'.daed era eht fo owt fi ,terces a peek nac eerhT' 
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    # print(translated)
    # print('i is', i, ', message[i] is', message[i], ', translated is', translated)
    i = i - 1
    # print(i)

print(translated)
