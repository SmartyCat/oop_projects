class CaseHelper:

    @staticmethod
    def is_snake(s):
        l = s.split("_")
        for i in l:
            if i.isalpha() and i[0].isupper():
                return False
        return len(l) - 1 == s.count("_")

    @staticmethod
    def is_upper_camel(s):
        if s[0].isalpha() and s[0].isupper():
            return True
        return False

    @staticmethod
    def to_snake(s):
        result = [s[0].lower()]
        for i in s[1:]:
            if i.islower():
                result.append(i)
            else:
                result.append("_" + i.lower())
        return "".join(result)

    @staticmethod
    def to_upper_camel(s):
        l = s.split("_")
        l = list(map(lambda x: x.title(), l))
        return "".join(l)
