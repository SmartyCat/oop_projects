class Word:
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word.title()

    def __repr__(self):
        return f"Word('{self.word}')"

    def __eq__(self, value):
        if isinstance(value, Word):
            return len(self.word) == len(value.word)
        return NotImplemented

    def __lt__(self, value):
        if isinstance(value, Word):
            return len(self.word) < len(value.word)
        return NotImplemented

    def __le__(self, value):
        if isinstance(value, Word):
            return len(self.word) <= len(value.word)
        return NotImplemented
