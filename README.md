# Current files for Bottle project

<h3>Encrypting a message, generating a URL for sharing, and then decrypting once viewed</h3>

This project has been written and tested using Python 3.5.3 in IDLE on a Raspberry Pi 3, Debian version 9.13

## This project currently requires the installation of the following modules:
  * pyperclip `pip install pyperclip` (considering incorporating JavaScript)
  * cryptography `pip install cryptography` 
  * Crypto `pip install pycrypto` (currently in testing)

## How to test the code:

* The project is dependent on the main Bottle file: 'bottle.py' (already in this repository).
* 'main_bottle2.py' is the primary working file currently, this file will be ran as a python script and will start a server listening on __port 8080__.
* This can be accessed in a browser at '_localhost:8080/message_' - this will bring you to the input prompt for a message at the beginning of the process.
* 'main_bottle.py' was originally used with the legacy encryption method in 'crypt.py' -- this will no longer be used but is retained here for reference

## How to test the current encryption engines:

* 'crypt.py' will now serve as the module from which cryptographic functions will be imported from
* 'test1.py' contains a rudimentary message encryption script
* This can be ran as a regular .py file; it will prompt you for input, generate a pseudo-randomly generated token via 'captcha_bot.py', display your message encrypted via Fernet encryption, then decrypt and display the plaintext result
* 'test2.py' contains functions for MD5, AES, Blowfish and Fernet - once pycrypto has been installed this file can be ran as-is to test the functionality of these algorithms -- there are built-in messages for testing which will display ciphertext, then decrypt and display plaintext
* 'test3.py' serves to test as a file that imports these functions from 'crypt.py' as a module


