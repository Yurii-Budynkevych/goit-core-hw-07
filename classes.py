from collections import UserDict

class PhoneError(Exception):
    def __init__(self, message="not ok number"):
        self.message = message
        super().__init__(self.message)

class Field:
    def __init__(self, value):
        self.value = value
        
    def get_value (self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        name = name.lower().capitalize() 
        super().__init__(name)    

class Phone(Field):
    def __init__(self, phone):
        if len(phone) < 10:
            raise PhoneError() 
        super().__init__(phone)

class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
            pass
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")          

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone (self, phone):
        new_phone = Phone(phone) 
        self.phones.append(new_phone)

    def edit_phone (self, phone, edited_phone):
        for el in self.phones:
            if el.value == phone:
                el.value = edited_phone

    def find_phone (self, phone):
        for el in self.phones:
            if el.value == phone:
                return phone
        return 'not found'
    
    def get_value (self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.get_value()] = record

    def find(self, record_name):
        return self.data.get(record_name)
    
    def delete(self, record_name):
        self.data.pop(record_name) 

