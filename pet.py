class Pet:
    names = []

    def __init__(self, name):
        self.name = name
        Pet.names.append(self)

    @classmethod
    def first_pet(cls):
        if cls.names:
            return cls.names[0]
        return None

    @classmethod
    def last_pet(cls):
        if cls.names:
            return cls.names[-1]
        return None

    @classmethod
    def num_of_pets(cls):
        return len(cls.names)
