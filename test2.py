import time
import cryptography
from cryptography.fernet import Fernet
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Cipher import Blowfish
from Crypto.Hash import MD5


''' As noted in further comments below, these encryption methods work fine
    as they currently are in this script, but the plaintext messages have
    to be a multiple of the block size for each algorithm. I need to figure
    out how to ensure that each of these functions will perform the prescribed
    encryption on data of any length. (padding?)
'''


def decorate():
    print("=" * 34)

# -----------

def md5_hash():
    # Create a new instance of the hash object
    hash = MD5.new()
    # Encode a message for hashing
    message = "Hashing".encode()
    # The 'update' method continues the hashing by consuming the next chunk
    hash.update(message)
    # The 'digest' method returns a digest of what's been hashed so far
    digest = hash.digest()
    print("MD5 digest: %s" % digest)
    decorate()
md5_hash()

# -----------

''' The current AES encryption mode requires the inpur string to be a multiple
    of 16 in length -- need to figure out how to ensure that a string of
    anything length is processed in chunks until completion
'''

def aes_encrypt():
    # Create new AES cipher
    # An IV can be used, but 'MODE_ECB' ignores it
    iv = Random.new().read(AES.block_size)
    obj = AES.new('This is a key456This is a key456',AES.MODE_CBC, iv)
    message = "The answer is no"
    ciphertext = obj.encrypt(message)
    
    print("AES encryption: %s" % ciphertext)
    time.sleep(1)
    print("Decrypting AES...")
    time.sleep(1)
    
    # This decrypts and decodes
    # Per pypi.org documentation,a second object is needed in order
    # to properly decrypt (apparently)
    obj2 = AES.new('This is a key456This is a key456',AES.MODE_CBC, iv)
    # The decode() method below converts from byte string to UTF8
    aes_decrypt = obj2.decrypt(ciphertext).decode('utf-8')
    print(aes_decrypt)
    decorate()
aes_encrypt()

# -----------

''' The current Blowfish encryption mode requires the inpur string to be a
    multiple of 8 in length -- need to figure out how to ensure that a
    string of anything length is processed in chunks until completion
'''

# Encrypt works fine, decrypt coming out in bytes
def blowfish_encrypt():
    # This prints a Blowfish encrypted message
    bs = Blowfish.block_size    # 8 bits
    key = "An arbitrarily long key"
    iv = Random.new().read(bs)
    obj = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    message = b"What the"
    ciphertext = obj.encrypt(message)
    
    print("Blowfish encryption: %s" % ciphertext)
    time.sleep(1)
    print("Decrypting Blowfish...")
    time.sleep(1)
    
    # Not working, printing byte string
    obj2 = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    dec = obj2.decrypt(ciphertext).decode('utf-8')
    #plaintext = dec.decode()
    print(dec)
    decorate()
blowfish_encrypt()

# -----------

# This works fine for in/out crypto
def fernet_encryption():
    # Encrypt with cryptography.fernet
    key = Fernet.generate_key()
    f = Fernet(key)
    message = b"Poo poo potty"
    token = f.encrypt(message)
    
    print("Fernet encryption: %s" % token)
    time.sleep(1)
    print("Decrypting Fernet...")
    time.sleep(1)
    
    dec = f.decrypt(token)
    plaintext = dec.decode('utf8')
    print(plaintext)
    decorate()
fernet_encryption()



    
