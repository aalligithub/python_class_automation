import selenium
from nested_dict import classes_dict

webdriver_path = 'C:\webdriver\chromedriver'
selenium.webdriver = webdriver_path


class My_Classes:
    def __init__(self):
        pass

    def add_class(self):
        # use input and add a new class to the dict
        return 'class added'
    
    def delete_classes(self):
        for key, value in classes_dict.items():
            print(key)
        print('\nProccede to delete all classes?')

    def num_of_classes(self):
        # test passed
        print('You have :' ,len(classes_dict) , 'classes.')


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
test.delete_classes()
