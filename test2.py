import time
import cryptography
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Cipher import Blowfish
from Crypto.Hash import MD5



# Create a new instance of the hash object
hash = MD5.new()
# Encode a message for hashing
message = "Hashing".encode()
# The 'update' method continues the hashing by consuming the next chunk
hash.update(message)
# The 'digest' method returns a digest of what's been hashed so far
digest = hash.digest()
print("MD5 digest: %s" % digest)


# Create new AES cipher
# An IV can be used, but 'MODE_ECB' ignores it
obj = AES.new('This is a key456This is a key456',AES.MODE_ECB)
messages = "The answer is no"
ciphertext = obj.encrypt(messages)
print("AES encryption: %s" % ciphertext)
time.sleep(1)
print("Decrypting AES...")
time.sleep(1)
# This decrypts and decodes
aes_decrypt = obj.decrypt(ciphertext).decode()
print(aes_decrypt)


# This prints a Blowfish encrypted message
bs = Blowfish.block_size    # 8 bits
iv = Random.new().read(bs)
key = "An abritrarily long key"
bobj = Blowfish.new(key, Blowfish.MODE_CBC, iv)
bmessage = "What the".encode()
cblow = bobj.encrypt(bmessage)
print("Blowfish encryption: %s" % cblow)
time.sleep(1)
print("Decrypting Blowfish...")
# Not working, printing byte string
blow_decrypt = bobj.decrypt(cblow)
print(blow_decrypt)
