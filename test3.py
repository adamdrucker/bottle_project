from crypt import md5_hash, aes_encrypt, blowfish_encrypt, fernet_encrypt


message = "Testing this out"
result = md5_hash(message)
print(result)


result2 = aes_encrypt(message)
print(result2)


result3 = blowfish_encrypt(message)
print(result3)

result4 = fernet_encrypt(message)
print(result4)
