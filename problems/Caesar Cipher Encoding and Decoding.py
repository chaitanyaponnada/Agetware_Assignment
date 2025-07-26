def caesar_cipher(message, shift, decode=False):
    if decode:
        shift = -shift
    result = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  
    return result

original = "Hello, World!"
encoded = caesar_cipher(original, 3)
decoded = caesar_cipher(encoded, 3, decode=True)

print("Encoded:", encoded)
print("Decoded:", decoded)
