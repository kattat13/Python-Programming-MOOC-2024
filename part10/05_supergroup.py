
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'


class SuperGroup:
    def __init__(self, _name: str, _location: str):
        self._name = _name
        self._location = _location
        self._members = []

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location
    
    def add_member(self, hero: SuperHero):
        self._members.append(hero)

    def print_group(self):
        print(f'{self.name}, {self.location}\nMembers:')
        for hero in self._members:
            print(f'{hero.name}, superpowers: {hero.superpowers}')
        
        

if __name__ == '__main__':
    superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
    invisible = SuperHero("Invisible Inca", "Invisibility")
    revengers = SuperGroup("Revengers", "Emerald City")

    revengers.add_member(superperson)
    revengers.add_member(invisible)
    revengers.print_group()