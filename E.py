class StrExtension:

    @staticmethod
    def remove_vowels(s):
        vowels = "euioay"
        result = [i for i in s if i.lower() not in vowels]

        return "".join(result)

    @staticmethod
    def leave_alpha(s):
        a = "qwertyuiopasdfghjklzxcvbnm"
        result = [i for i in s if i.lower() in a]

        return "".join(result)

    @staticmethod
    def replace_all(string, chars, char):
        result = []
        for i in string:
            if i not in chars:
                result.append(i)
            else:
                result.append(char)
        return "".join(result)
