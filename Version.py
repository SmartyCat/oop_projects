class Version:

    def __init__(self, version):
        version = version.split(".")
        while len(version) != 3:
            version.append("0")
        version = list(map(lambda x: int(x), version))
        self.version = version

    def __str__(self):
        result = list(map(lambda x: str(x), self.version))
        return ".".join(result)

    def __repr__(self):
        result = list(map(lambda x: str(x), self.version))
        result = ".".join(result)
        return f"Version('{result}')"

    def __eq__(self, value):
        if isinstance(value, Version):
            return (
                self.version[0] == value.version[0]
                and self.version[1] == value.version[1]
                and self.version[2] == value.version[2]
            )
        return NotImplemented

    def __gt__(self, value):
        if isinstance(value, Version):
            return (
                self.version[0] > value.version[0]
                or self.version[0] == value.version[0]
                and self.version[1] > value.version[1]
                or self.version[0] == value.version[0]
                and self.version[1] == value.version[1]
                and self.version[2] > value.version[2]
            )
        return NotImplemented

    def __ge__(self, value):
        if isinstance(value, Version):
            return (
                self.version[0] >= value.version[0]
                or self.version[0] == value.version[0]
                and self.version[1] >= value.version[1]
                or self.version[0] == value.version[0]
                and self.version[1] == value.version[1]
                and self.version[2] > value.version[2]
            )


