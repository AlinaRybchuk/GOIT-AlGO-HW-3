from abc import ABC, abstractmethod


class AdressBook(ABC):
    @abstractmethod
    def process_adressbook(self, adressbook):
        pass

    @abstractmethod
    def print_text(self, text):
        pass

    @abstractmethod
    def list_commands(self):
        pass

class ConcreteClass(AdressBook):
    def process_adressbook(self, adressbook):
      for key, value in adressbook.items():
        print(f'{key}:{value}') 
  
    def print_text(self, text):
        print (text)

    def list_commands(self):
        return ['add_contacts', 'find_contacts', 'all_contacts']
        

adressbook = {'Jane':'+380536894758', 'John':'+380956921003'}
concrete_instance = ConcreteClass()
concrete_instance.process_adressbook(adressbook)
concrete_instance.print_text("Text")
print(concrete_instance.list_commands())

  
