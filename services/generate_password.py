import string
from random import choice

class GeneratePassword():
    def __init__(self) -> str:
        pass
    
    def insert_symbols(self, list_to_fill_out:list):
        [list_to_fill_out.append(i) for i in string.punctuation]
        [list_to_fill_out.append(i) for i in string.ascii_letters]
        return list_to_fill_out       
    
    def generator(self) -> str:
        list_characters = []
        self.insert_symbols(list_characters)
        password_list = []
        while True:
            if len(password_list) < 18:
                password_list.append(choice(list_characters))
            else:
                break
        # print(list_characters)
        return "".join(password_list)