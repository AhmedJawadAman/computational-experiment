# ----- Classes of village residents -----

class Resident:
    """A normal resident of the village."""

    def __init__(self, name, has_beard, shaves_self):
        self.name = name
        self.has_beard = has_beard        # does this person grow a beard?
        self.shaves_self = shaves_self    # does this person shave himself?
        self.shaved = False


class Barber(Resident):
    """A barber is a SEPARATE class with its own rules."""

    def shave_village(self, village):
        for person in village:
            if isinstance(person, Barber):
                continue                  # the rule is NOT for barbers
            if person.has_beard and not person.shaves_self:
                person.shaved = True
                print(self.name, "shaves", person.name)

    def shave_myself(self):
        if self.has_beard:
            self.shaved = True
            print(self.name, "shaves himself (rule of the Barber class)")
        else:
            print(self.name, "has no beard: no need to shave, no paradox")


# ----- Case 1: the barber is a man -----
print("Case 1: the barber is a man")
barber = Barber("Barber", has_beard=True, shaves_self=False)
village = [
    barber,
    Resident("Ivan", has_beard=True, shaves_self=False),
    Resident("Petr", has_beard=True, shaves_self=True),
    Resident("Maria", has_beard=False, shaves_self=False),
    Resident("Child", has_beard=False, shaves_self=False),
]
barber.shave_village(village)
barber.shave_myself()

# ----- Case 2: the barber is a woman -----
print()
print("Case 2: the barber is a woman")
barber2 = Barber("Barber Anna", has_beard=False, shaves_self=False)
barber2.shave_myself()
