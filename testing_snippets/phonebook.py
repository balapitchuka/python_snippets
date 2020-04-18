
class PhoneBook:
    def __init__(self):
        self.phonebook = dict()

    def lookup(self, name):
        return self.phonebook[name]

    def add(self, name, number):
        self.phonebook[name] = number

    def is_consistent(self):
        for name1, number1 in self.phonebook.items():
            for name2, number2 in self.phonebook.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True
