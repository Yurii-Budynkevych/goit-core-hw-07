from classes import AddressBook, Record

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_handler(args, book):
    try:
        if not args:
            raise Exception('Please enter a name.')
        record = book.find(args[0])
        if record is not None:
            record.add_phone(args[1])
        else:
            book.add_record(Record(*args))
    except Exception as e:
        print("Error occurred while adding contact:", e)

def change_handler(args, book):
    try:
        if not args:
            raise Exception('Please enter a name.')
        record = book.find(args[0])
        if record is not None:
            record.edit_phone(args[1], args[2])
        else:
            print(f"Record with name {args[0]} not found")
    except Exception as e:
        print("Error occurred while changing phone number:", e)

def phone_handler(args, book):
    try:
        if not args:
            raise Exception('Please enter a name.')
        record = book.find(args[0])
        if record is not None:
            print(record.get_phones())
        else:
            print(f"Record with name {args[0]} not found")
    except Exception as e:
        print("Error occurred while showing phone:", e)

def add_birthday_handler(args, book):
    try:
        if not args:
            raise Exception('Please enter a name.')
        record = book.find(args[0])
        if record is not None:
            record.add_birthday(args[1])
        else:
            print(f"Record with name {args[0]} not found")
    except Exception as e:
        print("Error occurred while adding birthday:", e)

def show_birthday_handler(args, book):
    try:
        if not args:
            raise Exception('Please enter a name.')
        record = book.find(args[0])
        if record is not None:
            print(record.get_birthday())
        else:
            print(f"Record with name {args[0]} not found")
    except Exception as e:
        print("Error occurred while showing birthday:", e)

def birthdays_handler(args, book):
    try:
        print(book.show_records_birthdays())
    except Exception as e:
        print("Error occurred while listing birthdays:", e)  

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
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

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
