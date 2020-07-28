import cryptography
from Crypto.Cipher import AES
from Crypto.Cipher import Blowfish
from Crypto.Hash import MD5



# This prints out an MD5 digest
hash = MD5.new()
message = "Hashing".encode()
hash.update(message)
digest = hash.digest()
print("MD5 digest: %s" % digest)

# This prints out an AES encrypted message
obj=AES.new('This is a key456',AES.MODE_ECB)
messages = "The answer is no"
ciphertext = obj.encrypt(messages)
print("AES encryption: %s" % ciphertext)


bobj = Blowfish.new('12345678')
bmessage = "Fishing for some blow"
cblow = bobj.encrypt(message)
print(cblow)
