from bottle import route, run, post, get, request, template, error
from cryptography.fernet import Fernet
from Crypto import Cipher
from captcha_bot import captcha
from crypt import *
import pyperclip as pc
import os


# Function to enable copy button
def copyFunc(link):
    pc.copy(link)


# Entry page - 'http://localhost:8080/message'
@route('/message')
def message_in():

    algorithms = ['AES', 'Blowfish' , 'Fernet']

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

    # ** HOW DO I GET DIFFERENT DROP DOWN MENU SELECTIONS IN HTML
    # ** TO CALL DIFFERENT PYTHON FUNCTIONS? I.E.:
    # if getElementById = "AES":
    #   aes_encrypt(message)

    
    # -------------------------------------


    # Vars passed into HTML
    variables = {"link": link, "url": url, "pc_url": pc_url}

    return template("encryption_page.html", variables)


# Page displayed after decryption
@get('/message/<url>')
def show_message(url):

    # Remove this?
    
    # Decrypt functions below
    # ------------------------------------

    


    # ------------------------------------


    # Vars passed into HTML
    # plaintext variable doesn't currently exist
    variables = {"message": plaintext}
    
    return template("decryption_page.html", variables)






if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True, reloader=True)
