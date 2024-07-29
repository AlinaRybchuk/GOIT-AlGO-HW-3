from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        self.value = self.validate_phone(phone)

    def validate_phone(self, phone):
        if not phone:
            raise ValueError("Phone number cannot be empty")
        if not phone.isdigit():
            raise ValueError("Phone number can only contain digits")
        if len(phone) != 10:
            raise ValueError("Phone number must be 10 digits long")
        return phone

class Birthday(Field):
    def __init__(self, value: str):
        if self.__is_valid(value):
         self.value = datetime.strptime(value, "%d.%m.%Y")
        else:
         raise ValueError("Invalid date format. Use DD.MM.YYYY")
    
    def __is_valid(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            return True
        except ValueError:
            return False

class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))
        
    def remove_phone(self, phone: str):
        for p in self.phones:
            if p.phone == phone:
             self.phones.remove(p)
             break

    def edit_phone(self, old_phone: str, new_phone: str):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)
        
    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
             return p

    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
         del self.data[name]

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.today().date()
        next_week = today + timedelta(days=7)
        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if today <= birthday_this_year.date() <= next_week:
                    upcoming_birthdays.append({
                        "name": record.name.value, 
                        "birthday_date": birthday_this_year.strftime("%d.%m.%Y")
                    })
        return upcoming_birthdays

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
    return inner

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        if phone in [p.value for p in record.phones]:
            return "Phone number already exists for this contact."
        record.add_phone(phone)
    return message
    
@input_error
def add_birthday(args, book):
    if len(args) < 2:
        return "Invalid input. Use 'add-birthday [name] [date of birth in DD.MM.YYYY format]'"
    name, date = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return "Birthday added."
    else:
        return "Contact not found"

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        if record.birthday:
            return record.birthday
        else:
            return "Birthday not added to this contact."
    else:
        return "Contact not found"

@input_error
def change_contact(args, book):
    if len(args) != 3:
        return "Invalid input. Use 'change [name] [old_phone] [new_phone]'"
    name, old_number, new_number = args
    record = book.find(name)
    if record:
        record.edit_phone(old_number, new_number)
        return "Phone changed."
    else:
        return "Contact not found"
    
@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return '; '.join(p.value for p in record.phones)
    else:
        return "Contact not found"

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

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
            print(add_contact(args, book))                    

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print("All contacts:")
            for record in book.values():
                print(record)

        elif command == "add-birthday":
            print(add_birthday(args, book))                    

        elif command == "show-birthday":
            print(show_birthday(args, book))                    

        elif command == "birthdays":
            upcoming_birthdays = book.get_upcoming_birthdays()
            if upcoming_birthdays:
                print("Upcoming birthdays:")
                for bday in upcoming_birthdays:
                    print(f"{bday['name']}: {bday['birthday_date']}")
            else:
                print("No upcoming birthdays.")                   
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()








