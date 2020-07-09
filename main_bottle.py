from bottle import route, run, post, get, request, template, error
from sitecrypt_bottle import *
from captcha_bot import captcha
import pyperclip as pc
import os

url = captcha()


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
    global ciphertext
    
    # Functions called from 'sitecrypt_bottle'
    # 'Message' passed as argument
    generate_otp(len(message))              # Can this file be saved to the Bottle server?
    sheet = load_sheet("otp.txt")
    ciphertext = encrypt(message, sheet)
    save_file("encrypted.txt", ciphertext)  # Can this file be saved to the Bottle server?
    ciphertext = load_file("encrypted.txt")

    link = "localhost:8080/message/{url}".format(url=url)
    def copyFunc():
        pc.copy(link)
    
          
    return '''
        <table style="width:50%", border=1px solid black>
            <tr>
                <th>Encrypted message</th>
                <th>Sharable link</th>
            </tr>
            <tr>
                <td>{message}</td>
                <td id=link><a href={link}>{link}</a>
                <button onclick="copyFunc()">Copy link</button></td>
            </tr>            
        </table>
    '''.format(message=ciphertext, link=link)



@get('/message/<url>')
def show_message(url):
    sheet = load_sheet("otp.txt")
    ciphertext = load_file("encrypted.txt")
    plaintext = decrypt(ciphertext, sheet)

    # Upon accessing the generated URL for the encrypted message,
    # the following files are deleted
    os.remove("otp.txt")
    os.remove("encrypted.txt")

    return '''
        <table style="width:50%", border=1px solid black>
            <tr>
                <th>Decrypted message</th>                
            </tr>
            <tr>
                <td>{message}</td>                
            </tr>
        </table>
    '''.format(message=plaintext)


# Issue: the two text files (OTP and encrypted) generated are stored locally -- how would
# this work on a public website? Can they be temporarily created and stored prior to deletion?

# Issue: copy link button


# ///////////////////////////////////////////////////////////////////////
# ERROR
@error('500')
def error500(error):
    return 'ERROR 500: Dude, you fucked up. Go back and edit your code.'



# //////////////////////////////////////////
run(host="localhost", port=8080, debug=True, reloader=True)
