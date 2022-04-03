from configparser import ConfigParser
import rsa

config_object = ConfigParser()
encrypted_message = ''
user_input = ''


def make_keys():
    print('\nMaking Private and Public keys...')
    public_key, private_key = rsa.newkeys(512)

    priv_key_file = open("private_key.ini", 'w')
    priv_key_file.write(private_key.save_pkcs1().decode('utf-8'))
    priv_key_file.close()

    pub_key_file = open("public_key.ini", 'w')
    pub_key_file.write(public_key.save_pkcs1().decode('utf-8'))
    pub_key_file.close()
    print('Keys successfuly made, DO NOT SHARE YOUR PRIVATE KEY!')


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


def console(user_input):
    match user_input:
        case 1:
            # password encrypt
            user_input = input(
                '\nPlease input the Password to begin encrypting (Your password will never be accessible and only decrypted with your private key) or press Ctrl + C to cancel ')
            encrypt(user_input)
            print('\nYour password was successfuly Encrypted!')

        case 2:
            # encrypt username
            user_input = input(
                '\nPlease input the Username to begin encrypting (Your username will never be accessible and only decrypted with your private key) or press Ctrl + C to cancel ')
            encrypt(user_input)
            print('\nYour Username was successfuly Encrypted!')

        case 3:
            # renew keys
            make_keys()

        case 4:
            # exits
            exit()

        case _:
            # default case
            print('\nError : Invalid Response, Please re run encryption.py')


if __name__ == "__main__":
    priv_key_file = open("private_key.ini", 'r')
    pub_key_file = open("public_key.ini", 'r')

    if priv_key_file.read() == '' or pub_key_file.read() == '':
        print('\nNo keys detected, generating keys...')
        make_keys()

    user_input = input(
        '\nHello welcome to the Encryptor, for encrypting your PASSWORD enter [1], for USERNAME enter [2], to renew your keys enter [3] and enter [4] to exit... ')
    console(int(user_input))

# DECRYPT IS EXTERAL USE ONLY DONT RUN HERE
