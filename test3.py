from crypt import md5_hash, aes_encrypt, blowfish_encrypt, fernet_encrypt


message = "Testing this out"

result = md5_hash(message)
print(result)


aes_cipher, aes_plain = aes_encrypt(message)
print(aes_cipher)
print(aes_plain)

blowfish_cipher, blowfish_plain = blowfish_encrypt(message)
print(blowfish_cipher)
print(blowfish_plain)

fernet_cipher, fernet_plain = fernet_encrypt(message)
print(fernet_cipher)
print(fernet_plain)

