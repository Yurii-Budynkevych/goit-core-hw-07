from classes import AddressBook, Record

def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args

def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error occurred in {func.__name__.replace('_handler', '')}:", e)
    return wrapper

@handle_errors
def add_handler(args, book):
    if not args:
        raise ValueError('Please enter a name.')
    record = book.find(args[0])
    if record is not None:
        record.add_phone(args[1])
    else:
        book.add_record(Record(*args))

@handle_errors
def change_handler(args, book):
    if not args:
        raise ValueError('Please enter a name.')
    record = book.find(args[0])
    if record is not None:
        record.edit_phone(args[1], args[2])
    else:
        print(f"Record with name {args[0]} not found")

@handle_errors
def phone_handler(args, book):
    if not args:
        raise ValueError('Please enter a name.')
    record = book.find(args[0])
    if record is not None:
        print(record.get_phones())
    else:
        print(f"Record with name {args[0]} not found")

@handle_errors
def add_birthday_handler(args, book):
    if not args:
        raise ValueError('Please enter a name.')
    record = book.find(args[0])
    if record is not None:
        record.add_birthday(args[1])
    else:
        print(f"Record with name {args[0]} not found")

@handle_errors
def show_birthday_handler(args, book):
    if not args:
        raise ValueError('Please enter a name.')
    record = book.find(args[0])
    if record is not None:
        print(record.get_birthday())
    else:
        print(f"Record with name {args[0]} not found")

@handle_errors
def birthdays_handler(args, book):
    print(book.show_records_birthdays())

@handle_errors
def all_handler(args, book):
    if not book.data:
        print("No contacts available.")
    else:
        for record in book.values():
            print(record)

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "":
            print("Please enter the command")

        elif command == "add":
            add_handler(args, book)

        elif command == "change":
            change_handler(args, book)

        elif command == "phone":
            phone_handler(args, book)

        elif command == "add-birthday":
            add_birthday_handler(args, book)

        elif command == "show-birthday":
            show_birthday_handler(args, book)

        elif command == "birthdays":
            birthdays_handler(args, book)

        elif command == "all":
            all_handler(args, book)

        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()
