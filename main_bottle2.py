from bottle import route, run, post, get, request, template, error
from sitecrypt_bottle import *
from captcha_bot import captcha
import pyperclip as pc
import os


def copyFunc(link):
    pc.copy(link)


@route('/message')
def message_in():
    return '''
        <form action="/encrypted" method="post">
            Message: <input name="message" type="text" />
            <input value="Encrypt message" type="submit" />
        </form>
    '''

@post('/encrypted')
def do_encrypt():
    message = request.forms.get('message')
    url = captcha()
    link = "localhost:8080/message/{url}".format(url=url)
    global ciphertext
    pc_url = pc.copy(link)
    
    # Functions called from 'sitecrypt_bottle'
    # 'Message' passed as argument
    generate_otp(len(message))
    sheet = load_sheet("otp.txt")
    ciphertext = encrypt(message, sheet)
    save_file("encrypted.txt", ciphertext)
    ciphertext = load_file("encrypted.txt")

    variables = {"message": message, "link": link, "url": url, "pc_url": pc_url}

    return template("encryption_page.html", variables)


@get('/message/<url>')
def show_message(url):
    sheet = load_sheet("otp.txt")
    ciphertext = load_file("encrypted.txt")
    plaintext = decrypt(ciphertext, sheet)

    # Upon accessing the generated URL for the encrypted message,
    # the following files are deleted
    os.remove("otp.txt")
    os.remove("encrypted.txt")

    variables = {"message": plaintext}
    
    return template("decryption_page.html", variables)










run(host="localhost", port=8080, debug=True)
