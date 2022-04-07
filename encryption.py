from configparser import ConfigParser
import rsa


config_object = ConfigParser()
encrypted_message = ''
user_input = ''


def make_keys():
    # makes a pair of private and public keys and writes them in .ini file
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
    # encrypts the entry with the public key
    pub_key_file = open("public_key.ini", 'r')

    publicKey = rsa.PublicKey.load_pkcs1(pub_key_file.read(), 'PEM')

    encrypted_message = rsa.encrypt(message_toBe_encrypted.encode(), publicKey)

    pub_key_file.close()

    return encrypted_message


def decrypt(encrypted_message):
    # decrypts the file with the private key
    print('\nDecrypting file...')

    priv_key_file = open("private_key.ini", 'r')

    privateKey = rsa.PrivateKey.load_pkcs1(priv_key_file.read(), 'PEM')

    decMessage = rsa.decrypt(encrypted_message, privateKey).decode()

    priv_key_file.close()

    print('\nDecrypting Complete')

    return decMessage


def console(user_input):
    match user_input:
        case 1:
            try:
                # password encrypt
                user_input = input(
                    '\nPlease input the Password to begin encrypting (Your password will never be accessible and only decrypted with your private key) or press Ctrl + C to cancel : ')

                file = open("password.ini", 'wb')
                file.write(encrypt(user_input))

                print('\nYour password was successfuly Encrypted!')

            except (TypeError):
                print(
                    '\nError : TypeError, Could not write the encrypted password to file')

            except (FileNotFoundError):
                print(
                    '\nError : password.ini not found, Password encryption failed')

            except:
                print('\nError : Unknown, Password encryption failed')

        case 2:
            try:
                # encrypt username
                user_input = input(
                    '\nPlease input the Username to begin encrypting (Your username will never be accessible and only decrypted with your private key) or press Ctrl + C to cancel : ')

                file = open("username.ini", 'wb')
                file.write(encrypt(user_input))

                print('\nYour Username was successfuly Encrypted!')

            except (TypeError):
                print(
                    '\nError : TypeError, Could not write the encrypted username to file')

            except (FileNotFoundError):
                print(
                    '\nError : username.ini not found please create, Username encryption failed')

            except:
                print('\nError : Unknown, Username encryption failed')

        case 3:
            # renew keys
            try:
                make_keys()
            except:
                print('Error : Unknown, Making keys failed')

        case 4:
            # exits
            print('\nExiting, Goodbye!\n')
            exit()

        case _:
            # default case
            print(
                '\nError : Invalid Response, Wrong Number, You entered : [', user_input, ']')


if __name__ == "__main__":
    # checking if the files exist
    try:
        priv_key_file = open("private_key.ini", 'r')
        pub_key_file = open("public_key.ini", 'r')

    # building the files if they dont exist
    except(FileNotFoundError):
        print('\nKey files not found, building key files...')

        # writing the non existance files
        priv_key_file = open("private_key.ini", 'w')
        pub_key_file = open("public_key.ini", 'w')

        # reading to see if the file is empty
        priv_key_file = open("private_key.ini", 'r')
        pub_key_file = open("public_key.ini", 'r')

        print('\nKey files made')

    # checking if the key files are empty
    if priv_key_file.read() == '' or pub_key_file.read() == '':
        print('\nNo keys detected, generating keys...')
        make_keys()

    while True:
        user_input = 0
        while not 1 <= user_input <= 4:
            try:
                user_input = int(input(
                    "\nHello welcome to the Encryptor, for encrypting your PASSWORD enter [1], for USERNAME enter [2], to renew your keys enter [3] and enter [4] to exit... "))
            except ValueError:
                print('\nError : Invalid Response, Non numeric entry')
        console(user_input)

# DECRYPT IS EXTERAL USE ONLY DONT RUN HERE
# decrypt example:
    # file = open("password.ini", 'rb')
    # decrypt(file.read())
