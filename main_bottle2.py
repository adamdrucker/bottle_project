from bottle import route, run, post, get, request, template, error
from cryptography.fernet import Fernet
from captcha_bot import captcha
import pyperclip as pc
import os


key = Fernet.generate_key()
f = Fernet(key)


def copyFunc(link):
    pc.copy(link)


@route('/message')
def message_in():
    return template("form.html")


@post('/encrypted')
def do_encrypt():
    message = request.forms.get('message').encode()
    url = captcha()
    link = "localhost:8080/message/{url}".format(url=url)
    pc_url = pc.copy(link)
    
    # Encrypt functions below
    # *** 'message' passed as argument ***
    # -------------------------------------
    token = f.encrypt(message)
    global token
    # -------------------------------------

    variables = {"message": token, "link": link, "url": url, "pc_url": pc_url}

    return template("encryption_page.html", variables)


@get('/message/<url>')
def show_message(url):

    # Decrypt functions below
    # ------------------------------------
    dec = f.decrypt(token)
    plaintext = dec.decode('utf8')


    # ------------------------------------

    variables = {"message": plaintext}
    
    return template("decryption_page.html", variables)






if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True, reloader=True)
