# Current files for Bottle project

<h3>Encrypting a message, generating a URL for sharing, and then decrypting once viewed</h3>

## This project currently requires the installation of the following modules:
  * pyperclip `pip install pyperclip` (considering incorporating JavaScript)
  * cryptography `pip install cryptography` 

## How to test the code:

* The project is dependent on the main Bottle file: 'bottle.py' (already in this repository).
* 'main_bottle2.py' is the primary working file currently, this file will be ran as a python script and will start a server listening on __port 8080__.
* This can be accessed in a browser at '_localhost:8080/message_' - this will bring you to the input prompt for a message at the beginning of the process.

## How to test the current encryption engine (cryptography.fernet):

* 'test1.py' contains a rudimentary message encryption script
* This can be ran as a regular .py file; it will prompt you for input, generate a pseudo-randomly generated token via 'captcha_bot.py', display your message encrypted via Fernet encryption, then decrypt and display the plaintext result



