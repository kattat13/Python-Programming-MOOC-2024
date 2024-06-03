
class Person:
    def __init__(self, name: str):
        self._name = name
        self._numbers = []
        self._address = ''

    def add_number(self, number: str):
        self._numbers.append(number)

    def add_address(self, address: str):
        self._address = address

    def name(self):
        return self._name

    def numbers(self):
        return self._numbers

    def address(self):
        if self._address:
            return self._address
        return None
    

class PhoneBook:
    def __init__(self):
        self.__persons = []

    def add_number(self, name: str, number: str):
        for person in self.__persons:
            if person.name() == name:
                person.add_number(number)
                return
        new_person = Person(name)
        new_person.add_number(number)
        self.__persons.append(new_person)

    def add_address(self, name: str, address: str):
        for person in self.__persons:
            if person.name() == name:
                person.add_address(address)
        new_person = Person(name)
        new_person.add_address(address)
        self.__persons.append(new_person)
        # if not name in self.__persons:
        #     self.__persons.update(Person(name))
            
        #     name.add_number(number)
        # name.add_number(number)

    def get_entry(self, name: str):
        for person in self.__persons:
            if person.name() == name:
                return person.numbers(), person.address()
        else:
            return [], None

    def all_entries(self):
        return self.__persons


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers, address = self.__phonebook.get_entry(name)
        if numbers == []:
            print("number unknown") 
        else:
            for number in numbers:
                print(number)
        if address == None:
            print('address unknown')
        else:
            print('address:', address)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

