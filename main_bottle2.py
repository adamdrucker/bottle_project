from bottle import route, run, post, get, request, template, error
from cryptography.fernet import Fernet
from Crypto import Cipher
from captcha_bot import captcha
from crypt import *
import pyperclip as pc
import os


algorithms = ['AES', 'Blowfish' , 'Fernet']

# Function to enable copy button
def copyFunc(link):
    pc.copy(link)


# Entry page - 'http://localhost:8080/message'
@route('/message')
def message_in():    

    # Items for drop down list
    variables = {"algorithms": algorithms}

    # Returns the input form prior to encryption
    return template("form.html", variables)



# Page displayed after encryption
@post('/encrypted')
def do_encrypt():

    # Input taken from user, encoded for encryption
    message = request.forms.get('message').encode()

    # This generates a randomized path for the URL for each message encrypted
    url = captcha()
    link = "localhost:8080/message/{url}".format(url=url)

    # Enabled the copy button to grab the URL
    pc_url = pc.copy(link)

    
    
    # Encrypt functions below
    # // 'message' passed as argument
    # -------------------------------------

    # This successfully displays the encryption method selected from the dropdown
    e_method = request.forms.get('enc')

    # The "encryption-name_cipher" variables contain the encrypted message,
    # but are currently never used
    # Not ideal using globals, but it works for the time being
    if e_method == 'AES':
        aes_cipher, aes_plain = aes_encrypt(message)
    elif e_method == 'Blowfish':
        blowfish_cipher, blowfish_plain = blowfish_encrypt(message)
    elif e_method == 'Fernet':
        fernet_cipher, fernet_plain = fernet_encrypt(message)

    global e_method
    global aes_plain
    global blowfish_plain
    global fernet_plain
    
    # -------------------------------------


    # Vars passed into HTML
    variables = {"link": link, "url": url, "pc_url": pc_url, "e_method": e_method}

    return template("encryption_page.html", variables)


# Page displayed after decryption
@get('/message/<url>')
def show_message(url):

    # Remove this?
    
    # Decrypt functions below
    # ------------------------------------

    if e_method == 'AES':
        plaintext = aes_plain
    elif e_method == 'Blowfish':
        plaintext = blowfish_plain
    elif e_method == 'Fernet':
        plaintext = fernet_plain


    # ------------------------------------


    # Vars passed into HTML
    # plaintext variable doesn't currently exist
    variables = {"message": plaintext}
    
    return template("decryption_page.html", variables)






if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True, reloader=True)
