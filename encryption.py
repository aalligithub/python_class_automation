from asyncore import write
from distutils.fancy_getopt import wrap_text
from configparser import ConfigParser
from unittest import case
import rsa

config_object = ConfigParser()
encrypted_message = ''


def make_keys():
    print('\nMaking Private and Public keys...')
    public_key, private_key = rsa.newkeys(512)

    priv_key_file = open("private_key.ini", 'w')
    priv_key_file.write(private_key.save_pkcs1().decode('utf-8'))
    priv_key_file.close()

    pub_key_file = open("public_key.ini", 'w')
    pub_key_file.write(public_key.save_pkcs1().decode('utf-8'))
    pub_key_file.close()
    print('Keys successfuly made')


def encrypt(message_toBe_encrypted):
    pub_key_file = open("public_key.ini", 'r')
    publicKey = rsa.PublicKey.load_pkcs1(pub_key_file.read(), 'PEM')

    encrypted_message = rsa.encrypt(message_toBe_encrypted.encode(), publicKey)

    pub_key_file.close()

    return encrypted_message


def decrypt(encrypted_message):
    priv_key_file = open("private_key.ini", 'r')
    privateKey = rsa.PrivateKey.load_pkcs1(priv_key_file.read(), 'PEM')

    decMessage = rsa.decrypt(encrypted_message, privateKey).decode()
    print("\ndecrypted string: ", decMessage)

    priv_key_file.close()


if __name__ == "__main__":
    priv_key_file = open("private_key.ini", 'r')
    pub_key_file = open("public_key.ini", 'r')

    if priv_key_file.read() == '' or pub_key_file.read() == '':
        make_keys()

    user_input = input('\nHello welcome to the Encryptor, for encrypting your PASSWORD enter [1], for USERNAME enter [2], to renew your keys enter [3]... ')

    match user_input:
        case 1:
            pass
            exit()

    message_toBe_encrypted = input('\nPlease enter what you want to encrypt : ')

    encrypted_message = encrypt(message_toBe_encrypted)

    decrypt(encrypted_message)


# use encryption in the main code
