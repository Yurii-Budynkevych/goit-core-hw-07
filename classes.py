from collections import UserDict, defaultdict
from datetime import datetime, timedelta
import re

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
    __pattern = r"^\+?\d{10,}$"

    def __init__(self, phone):
        if not phone:
                raise PhoneError("Plese enter phone")
        elif not re.match(self.__pattern, phone):
                raise PhoneError() 
        super().__init__(phone)

class Birthday(Field):
    def __init__(self, value):

        try:
            datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")    
        super().__init__(value)

    def __repr__(self):
        return f"Object Birthday. birthday: {self.value}"


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.phones = [Phone(phone)]
        self.birthday = birthday
  
    def add_phone (self, phone):
        new_phone = Phone(phone) 
        self.phones.append(new_phone)

    def edit_phone(self, phone, edited_phone):
        for el in self.phones:
            if el.value == phone:
                el.value = Phone(edited_phone).value
                return
        raise ValueError("Original phone number not found.")

    def find_phone(self, phone):
        for el in self.phones:
            if el.value == phone:
                return el 
        return None
    
    def get_phones (self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_birthday (self, birthday):
        new_birthday = Birthday(birthday) 
        self.birthday = new_birthday

    def get_birthday (self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday}"
    
    def __repr__(self):
        name = self.name.value
        phones = '; '.join(p.value for p in self.phones)
        bday = self.birthday if self.birthday else "N/A"
        return f"Name: {name}, Phones: {phones}, Birthday: {bday}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.get_value()] = record

    def find(self, record_name):
        return self.data.get(record_name.lower().capitalize())
    
    def show_records_birthdays(self):
            today = datetime.today().date()
            upcoming_birthdays = defaultdict(list)

            for record in self.data.values():
                if not record.birthday:
                    continue

                bday_str = record.birthday.value  # Format: 'DD.MM.YYYY'
                bday_date = datetime.strptime(bday_str, '%d.%m.%Y').date()
                this_year_birthday = bday_date.replace(year=today.year)

                # If birthday has already passed this year, skip or set to next year
                if this_year_birthday < today:
                    this_year_birthday = bday_date.replace(year=today.year + 1)

                # Check if it's in the upcoming 7 days
                if 0 <= (this_year_birthday - today).days < 7:
                    greeting_day = this_year_birthday

                    # If weekend, shift to Monday
                    if greeting_day.weekday() == 5:  # Saturday
                        greeting_day += timedelta(days=2)
                    elif greeting_day.weekday() == 6:  # Sunday
                        greeting_day += timedelta(days=1)

                    weekday_name = greeting_day.strftime('%A')
                    upcoming_birthdays[weekday_name].append(record.name.value)

            if not upcoming_birthdays:
                return "No upcoming birthdays this week."

            result = []
            for day in sorted(upcoming_birthdays.keys()):
                names = ', '.join(upcoming_birthdays[day])
                result.append(f"{day}: {names}")

            return '\n'.join(result)

    def delete(self, record_name):
        self.data.pop(record_name) 

