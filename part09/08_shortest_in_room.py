
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0
    
    def print_contents(self):
        combined_height = 0
        for person in self.persons:
            combined_height += person.height
        print(f'There are {len(self.persons)} persons in the room, and their combined height is {combined_height} cm')
        for person in self.persons:
            print(f'{person.name} ({person.height} cm)')

    def shortest(self):
        if not self.is_empty():
            lowest_height = self.persons[0].height
            shortest_name = self.persons[0]
            for person in self.persons:
                if person.height <= lowest_height:
                    lowest_height = person.height
                    shortest_name = person
            return shortest_name
        return None
    
    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person:
            self.persons.remove(shortest_person)
            return shortest_person
        return None

        

if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()