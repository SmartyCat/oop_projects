class Pet:
    l = []

    def __init__(self, name):
        self.name = name
        Pet.l.append(self.name)

    @classmethod
    def first_pet(cls):
        if cls.l:
            return cls.l[0]
        return None

    @classmethod
    def last_pet(cls):
        if cls.l:
            return cls.l[-1]
        return None

    @classmethod
    def num_of_pets(cls):
        return len(cls.l)
