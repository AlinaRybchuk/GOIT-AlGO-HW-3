from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.name = name

name = Name("John")
name = Name("Oliwia")   

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

    def validate_phone(self, phone):
        if not phone:
            raise ValueError("Phone number cannot be empty")
        if not phone.isdigit():
            raise ValueError("Phone number can only contain digits")
        if len(phone) != 10:
            raise ValueError("Phone number must be 10 digits long")
        return phone

John_phone_one = Phone("4857961301")
John_phone_two = Phone("2300697458")
Oliwia_phone_one = Phone("5411008833")
Oliwia_phone_two = Phone("2896300177")

class Birthday(Field):
    def __init__(self, value: str):
        try:
            if self.__is_valid(value):
                self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record():
    def __init__(self, name, birthday):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))
        
    def remove_phone(self, phone: str):
        for p in self.phones:
            if p.phone == phone:
             self.phones.remove(p)

    def edit_phone(self, old_phone: str, new_phone: str):
        for p in self.phones:
            if new_phone != old_phone:
             self.add_phone(new_phone)
        
    def find_phone(self, phone: str):
        for p in self.phones:
            if p.phone == phone:
             return p

    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.book = {}

    def add_record(self, record):
        self.book[record.name] = record.phones

    def find(self, name: str):
        name = Name(name)
        for key in self.book:
         if key == name:
            return Record(name, self.book.values)
        else:
            return None

    def delete(self, name):
        name = Name(name)
        if name in self.book:
           del self.book[name]

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.today().date()
        for name, record in self.data.items():
            if record.birthday:
                birthday = record.birthday.value.date()
                birthday_this_year = birthday.replace(year=today.year)
                next_week = today + timedelta(days=7)
            if today <= birthday_this_year <= next_week:
                upcoming_birthdays.append({"name": name, "birthday_date": birthday_this_year.strftime("%d.%m.%Y")})
        return upcoming_birthdays

book = AddressBook()
john_record = Record("John")
john_record.add_phone("4857961301")
john_record.add_phone("2300697458")
book.add_record(john_record)

oliwia_record = Record("Oliwia")
oliwia_record.add_phone("5411008833")
oliwia_record.add_phone("2896300177")
book.add_record(oliwia_record)

print(book)

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("ValueError occurred")
    return inner

@input_error("add")
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error("add-birthday")
def add_birthday(args, book):
    if len(args) < 2:
        return ("Invalid input. Use 'add-birthday [name] [date of birth in DD.MM.YYYY format]'")
    name, date = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
    return ("Birthday added.")

@input_error("show-birthday")
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        if record.birthday:
            return record.birthday
        else:
            return ("Birthday not added to this contact.")

@input_error("change")
def change_contact(args, book):
    if len(args) != 3 or not Phone(args[1]).value or not Phone(args[2]).value:
        return ("Invalid input. Use 'change [name] [old_phone] [new_phone]'")
    name, old_number, new_number = args
    record = book.find(name)
    if record is None:
        record.edit_phone(old_number, new_number)
        return ("Phone changed.")
    
@input_error("phone")
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        return record 
    else:
        return ("Contact not found")

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

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
            print(all(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))                    

        elif command == "show-birthday":
            print(show_birthday(args, book))                    

        elif command == "birthdays":
            print(book.get_upcoming_birthdays(args, book))                    
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()














    