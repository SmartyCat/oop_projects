class Word:
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word.title()

    def __repr__(self):
        return f"Word({self.word})"

    @staticmethod
    def helper(x):
        return isinstance(x, Word)

    def __eq__(self, value):
        if self.helper(value):
            return len(self.word) == len(value.word)
        return NotImplemented

    def __lt__(self, value):
        if self.helper(value):
            return len(self.word) < len(value.word)
        return NotImplemented

    def __le__(self, value):
        if self.helper(value):
            return len(self.word) <= len(value.word)
        return NotImplemented
