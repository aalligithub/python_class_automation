from asyncore import write
from distutils.fancy_getopt import wrap_text
from configparser import ConfigParser
import rsa

config_object = ConfigParser()
encrypted_message = ''


def make_keys():
    publicKey, privateKey = rsa.newkeys(512)

    priv_key_file = open("private_key.ini", 'w')
    priv_key_file.write(privateKey.save_pkcs1().decode('utf-8'))
    priv_key_file.close()

    pub_key_file = open("public_key.ini", 'w')
    pub_key_file.write(publicKey.save_pkcs1().decode('utf-8'))
    pub_key_file.close()


def encrypt(message_toBe_encrypted):
    pub_key_file = open("public_key.ini", 'r')
    publicKey = rsa.PublicKey.load_pkcs1(pub_key_file.read(), 'PEM')

    encrypted_message = rsa.encrypt(message_toBe_encrypted.encode(), publicKey)

    print("\noriginal string: ", message_toBe_encrypted)
    print("\nencrypted string: ", encrypted_message)

    return encrypted_message

    pub_key_file.close()


def decrypt(encrypted_message):
    priv_key_file = open("private_key.ini", 'r')
    privateKey = rsa.PrivateKey.load_pkcs1(priv_key_file.read(), 'PEM')

    decMessage = rsa.decrypt(encrypted_message, privateKey).decode()
    print("\ndecrypted string: ", decMessage)

    priv_key_file.close()


make_keys()

message_toBe_encrypted = input('\nPlease enter what you want to encrypt : ')

encrypted_message = encrypt(message_toBe_encrypted)

decrypt(encrypted_message)

# add console that only runs make_keys once
# use encryption in the main code
