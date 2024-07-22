from collections import UserDict

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

John_phone_one = Phone("4857961301")
John_phone_two = Phone("2300697458")
Oliwia_phone_one = Phone("5411008833")
Oliwia_phone_two = Phone("2896300177")

class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

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


















    