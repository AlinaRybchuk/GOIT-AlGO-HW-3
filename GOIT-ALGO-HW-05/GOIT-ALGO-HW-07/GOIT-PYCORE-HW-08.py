import pickle
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

RECORDS_FILE_PATH = Path("addressbook.pkl")
DATE_FORMAT = "%d.%m"

@dataclass
class Record:
    name: str
    phone: str
    birthday: datetime

def __str__(self):
    return (
    f"Name: {self.name}", 
    f"Phone: {self.phone}", 
    f"Birthday: {self.birthday.strftime(datetime, DATE_FORMAT)}"
    )

def add_new_record(book):
    name = input("Enter a name: ")
    phone = input("Enter the phone number: ")
    birthday = datetime.strptime(input("Enter the birthday (DD.MM.): "), DATE_FORMAT)

    book.append(Record(name=name, phone=phone, birthday=birthday.strftime(DATE_FORMAT)))
   
def save_records(book):
    with open(RECORDS_FILE_PATH, "wb") as f:
       pickle.dump(book, f)

def load_records():
    book = []
    if RECORDS_FILE_PATH.is_file():
        with open(RECORDS_FILE_PATH, "rb") as f:
         book = pickle.load(f)  
    return book
    
@contextmanager
def records_manager():
    book = load_records()
    try:
        yield book
    finally:
        save_records(book)

if __name__ == "__main__":
    with records_manager() as book:
        while True:
            does_add_record = input("Do you want to add a new record (y/n)? ").lower()
            if does_add_record == "y":
                add_new_record(book)
            elif does_add_record == "n":
                break
            else:
                print("Incorrect input. Try again.")
      
        if book:
          print("Your records:")
          for record in book:
            print(record)
