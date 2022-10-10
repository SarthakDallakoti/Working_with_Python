def ext_vigenere(text, key, option):
    if option == 'encrypt' or option == 'decrypt':
        result = ''

        for i in range(len(text)):
            index = ord(text[i]) - 32
            offset = ord(key[i % len(key)]) - 32

            modifiedIndex = index + offset if option == 'encrypt' else index - offset

            modifiedCharacter = chr((modifiedIndex % 95) + 32)
            result += modifiedCharacter

        return result

    return 'Invalid option!'
