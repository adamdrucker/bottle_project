# Current files for Bottle project

### Encrypting a message, generating a URL for sharing, and then decrypting once viewed

This project has been written and tested using Python 3.5.3 in IDLE on a Raspberry Pi 3, Debian version 9.13

## This project currently requires the installation of the following modules:
  * Bottle :arrow_right: `pip install bottle` (the main Bottle file can be found in this repo)
  * pyperclip :arrow_right: `pip install pyperclip`
  * cryptography :arrow_right: `pip install cryptography` 
  * Crypto :arrow_right: `pip install pycrypto`

## Project information:

* The project is dependent on the main Bottle file: 'bottle.py' (already in this repository)
* 'main.py' is the primary working file, this file will be ran as a Python script and will start a server listening on __port 8080__
* This can be accessed in a browser at '_localhost:8080/message_' - this will bring you to the input prompt for a message at the beginning of the process
* 'crypt.py' contains two sections:
  * The first part is referred to as "Legacy encryption code" -- in terms of my project, this was the first method used to perform encryption and it was based on a basic Caeser cipher that was modified :arrow_right: <sub>_this is no longer in use but is kept in the file for reference_</sub>
  * The second part is the set of cryptographic functions that are being used in 'main.py' -- AES, Blowfish and Fernet (there is also a MD5 function, but that is not being used)
  * This file also contains information regarding the libraries used, how the different functions operate, and links to external sources for the different types of algorithms
* There are three (3) HTML files related to the project:
  * 'form.html' :arrow_right: the starting point of the website
  * 'encryption_page.html' :arrow_right: the page displayed after an algorithm is selected and a message is entered for encryption
  * 'decryption_page.html' :arrow_right: the page displayed after the generated URL is accessed and the message is decrypted

## How to test the current encryption engines:

* 'crypt.py' serves as the module from which cryptographic functions will be imported from
* 'captcha_bot.py' is a small script that generates a short string of pseudo-randomly generated lower and upper letters, and numbers
* 'test1.py' contains a rudimentary message encryption script to test the __Fernet__ module
  * This can be ran as a regular .py file; it will prompt you for input, generate a pseudo-randomly generated token via 'captcha_bot.py', display your message encrypted via Fernet encryption, then decrypt and display the cleartext result
* 'test2.py' contains functions for MD5, AES, Blowfish and Fernet - once pycrypto has been installed this file can be ran as-is to test the functionality of these algorithms
  * There are built-in messages for testing which will display ciphertext, then decrypt and display cleartext
* 'test3.py' serves to test as a file that imports these functions from 'crypt.py' as a module and encrpyts a pre-defined string

## Testing the main project

* 'main.py' is the primary file - it imports cryptographic modules and functions, and lays out the Bottle structure through the use of decorators
  * The program begins when accessing '_localhost:8080/message_' as prescribed above
* An encryption algorithm can be chosen from the drop down menu
* This will generate a local URL which, when pasted back into a new tab, will perform decryption of the encrypted message
  * Currently, the encrypted message is not displayed anywhere, it's stored in a variable resulting from the encryption process
* Other functionality includes the ability to copy the generated URL via a button, and another button that will allow the user to encrypt another message (by bringing them back to the starting page)

### Known issues/what needs to be done:

* The URL generated for each encrypted message needs to be one-time use; currently it can be pasted over and over and display the decrypted message continuously
* The link is automatically copied to the clipboard without using the button to do initiate the copy function
* Refreshing the "old" link after a new one is generated will display the "new" message, even under the old {url}
