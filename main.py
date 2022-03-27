import selenium

webdriver_path = 'C:\webdriver\chromedriver'
selenium.webdriver = webdriver_path


class My_Classes:
    def __init__(self, class_name, class_time, class_url):
        self.class_name = class_name
        self.class_time = class_time
        self.class_url = class_url

    def add_class(self):
        pass
    
    def delete_class(self):
        pass

    def num_of_classes(self):
        return self.class_nested_dict.len


class Build:
    def __init__(self, password_path, username_path, login_ur):
        self.password_path = password_path
        self.username_path = username_path
        self.login_url = login_ur

    def login(self):
        pass

    def check_time_till_class_start(self):
        pass

    def get_to_class(self):
        pass


class Interactive_console:
    pass

test = My_Classes('math', 20, 'www.balls.com', 'new')
test.add_class()