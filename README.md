# Current files for Bottle project

### Encrypting a message, generating a URL for sharing, and then decrypting once viewed

This project has been written and tested using Python 3.5.3 in IDLE on a Raspberry Pi 3, Debian version 9.13

## This project currently requires the installation of the following modules:
  * Bottle `pip install bottle` (the main Bottle file can be found in this repo)
  * pyperclip `pip install pyperclip`
  * cryptography `pip install cryptography` 
  * Crypto `pip install pycrypto`

## Project information:

* The project is dependent on the main Bottle file: 'bottle.py' (already in this repository)
* 'main.py' is the primary working file, this file will be ran as a Python script and will start a server listening on __port 8080__
* This can be accessed in a browser at '_localhost:8080/message_' - this will bring you to the input prompt for a message at the beginning of the process
* 'main_bottle.py' was originally used with the legacy encryption method in 'crypt.py' -- this will no longer be used but is retained here for reference
* 'crypt.py' contains two sections:
  * The first part is referred to as "Legacy encryption code" -- in terms on my project, this was the first method used to perform encryption and it was based on a basic Caeser cipher that was modified :arrow_right: <sub>_this is no longer in use but is kept in the file for reference_</sub>
  * The second part is the set of cryptographic functions that are being usesd in 'main.py' -- AES, Blowfish and Fernet (there is also a MD5 function, but that is not being used)

## How to test the current encryption engines:

* 'crypt.py' serves as the module from which cryptographic functions will be imported from
* 'captcha_bot.py' is a small script that generates a short string of pseudo-randomly generated lower and upper letters, and numbers
* 'test1.py' contains a rudimentary message encryption script to test the __Fernet__ module
  * This can be ran as a regular .py file; it will prompt you for input, generate a pseudo-randomly generated token via 'captcha_bot.py', display your message encrypted via Fernet encryption, then decrypt and display the plaintext result
* 'test2.py' contains functions for MD5, AES, Blowfish and Fernet - once pycrypto has been installed this file can be ran as-is to test the functionality of these algorithms
  * There are built-in messages for testing which will display ciphertext, then decrypt and display plaintext
* 'test3.py' serves to test as a file that imports these functions from 'crypt.py' as a module and encrpyts a pre-defined string


