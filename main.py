from bottle import route, run, post, get, request, template, error
from cryptography.fernet import Fernet
from Crypto import Cipher
from captcha_bot import captcha
from crypt import *
import pyperclip as pc
import os


''' The captcha_bot module imports a small program that generates a string of six pseudo-random
    characters that is only used in the URL for the encrypted method.

    Fernet encryption is used via the cryptographyt module for Python.

    AES and Blowfish are used via the Crypto moduel for Python.

    Pyperclip is a module used to enable the copy button on the encryption page.

'''

# List to append the 'url' value to, this will be checked later on
# If the URL generated during encryption exists in the list, the message can be decrypted
# If it does not, the message will not be displayed
approved_list = []


# Function to enable copy button
def copyFunc(link):
    pc.copy(link)


# Entry page - 'http://localhost:8080/message'
@route('/message')
def message_in():    

    algorithms = ['AES', 'Blowfish' , 'Fernet']
    alg_desc = ['AES is a federally approved encryption algorithm. It has been adopted by agencies such as the NSA for top secret information.',
    'Blowfish is a general-purpose encryption algorithm. It works well with short messages.',
    'Fernet encryption makes use of 128-bit AES encryption, and is a good choice when working with the Python language.']

       
    # Items for drop down list
    variables = {"algorithms": algorithms, "alg_desc": alg_desc}

    # Returns the input form prior to encryption
    return template("form.html", variables)



# Page displayed after encryption
@post('/encrypted')
def do_encrypt():

    # Input taken from user, encoded for encryption
    message = request.forms.get('message').encode()

    # This generates a randomized path for the URL for each message encrypted
    url = captcha()
    approved_list.append(url)
    link = "localhost:8080/message/{url}".format(url=url)

    # Enabled the copy button to grab the URL
    pc_url = pc.copy(link)

    
    # Encrypt functions below
    # // 'message' passed as argument
    # Not ideal using globals, but it works for the time being
    global e_method
    global aes_plain
    global blowfish_plain
    global fernet_plain

    # This successfully displays the encryption method selected from the dropdown
    e_method = request.forms.get('enc')

    # The "encryption-name_cipher" variables contain the encrypted message,
    # but are currently never used
    if e_method == 'AES':
        aes_cipher, aes_plain = aes_encrypt(message)
    elif e_method == 'Blowfish':
        blowfish_cipher, blowfish_plain = blowfish_encrypt(message)
    elif e_method == 'Fernet':
        fernet_cipher, fernet_plain = fernet_encrypt(message)


    # Vars passed into HTML
    variables = {"link": link, "url": url, "pc_url": pc_url, "e_method": e_method}

    return template("encryption_page.html", variables)


# Page displayed after decryption
@get('/message/<url>')
def show_message(url):

    
    # Decrypt functions
    if url in approved_list:
        if e_method == 'AES':
            plaintext = aes_plain
        elif e_method == 'Blowfish':
            plaintext = blowfish_plain
        elif e_method == 'Fernet':
            plaintext = fernet_plain

        approved_list.pop()
    else:
        plaintext = 'Message not available'
        
        



    # Vars passed into HTML
    variables = {"message": plaintext}
    
    return template("decryption_page.html", variables)






if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True, reloader=True)
