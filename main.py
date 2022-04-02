import selenium
from nested_dict import classes_dict
import mysql.connector


webdriver_path = 'C:\webdriver\chromedriver'
selenium.webdriver = webdriver_path


file = open("username_vadana.txt", "r")
username_vadana = file.read()

file = open("password_vadana.txt", "r")
password_vadana = file.read()

file = open("username_db.txt", "r")
username_db = file.read()

file = open("password_db.txt", "r")
password_db = file.read()


mydb = mysql.connector.connect(
    host='127.0.0.1',
    user=username_db,
    password=password_db
)


class My_Classes:
    def __init__(self):
        pass

    def add_class(self):
        # use input and add a new class to the dict
        return 'class added'

    def delete_all(self):
        for key, value in classes_dict.items():
            print(key)

        input_answer = input('\nProccede to delete all classes? (Y/N)  ')

        if input_answer == 'y' or input_answer == 'Y':
            classes_dict.clear()
            print('Dict cleared, Your Dict : ', classes_dict)
            # delete all dicts

        elif input_answer == 'n' or input_answer == 'N':
            print('Dict unchanged')

        else:
            print('Error : Wrong input')
            return

    def num_of_classes(self):
        # test passed
        print('You have :', len(classes_dict), 'classes.')


class Build:
    def __init__(self):
        pass

    def login(self):
        pass

    def check_time_till_class_start(self):
        # use arrays days hours and see where we are this way we wont need to change anything just add more classes later
        # get every class in the day and lay them out
        # get the time of the class and sort them
        pass

    def get_to_class(self):
        # use the name in the dict and search that name in the search field and click the class
        pass


class Interactive_console:
    pass


test = My_Classes()
# test.delete_all()
print(username_db)
print(username_vadana)
