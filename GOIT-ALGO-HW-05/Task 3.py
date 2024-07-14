def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
    
def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Exactly 2 arguments (name and phone) are required."
    name, phone = args
    if name in contacts:
       contacts[name] = phone
       return f"Contact {name}'s phone number has been changed to {phone}"
    else:
        return f"No contact found under the name {name}"

def show_phone_number(args, contacts):
    if len(args) != 1:
        return "Error: Exactly 1 argument (name) is required."
    name = args[0]
    if name in contacts:
        return f"Contact {name}'s phone number is {contacts[name]}"
    else:
        return f"No contact found under the name {name}"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in {"close", "exit"}:
         print("Goodbye!")
         break
        elif command == "hello":
         print("How can I help you?")
        elif command == "add":
         print(add_contact(args, contacts))
        elif command == "change":
         print(change_contact(args, contacts))
        elif command == "phone":
         print(show_phone_number(args, contacts))
        else:
         print("Invalid command.")

if __name__ == "__main__":
    main()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("ValueError occurred")
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("KeyError occurred.")
    return inner 

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Exactly 2 arguments (name and phone) are required."
    name, phone = args
    if name in contacts:
       contacts[name] = phone
       return f"Contact {name}'s phone number has been changed to {phone}"
    else:
        return f"No contact found under the name {name}"

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print("IndexError occurred")
    return inner 
  
@input_error
def show_phone_number(args, contacts):
    if len(args) != 1:
        return "Error: Exactly 1 argument (name) is required."
    name = args[0]
    if name in contacts:
        return f"Contact {name}'s phone number is {contacts[name]}"
    else:
        return f"No contact found under the name {name}"
    

