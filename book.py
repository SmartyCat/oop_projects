class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        if isinstance(pages, (int, float)) is True and pages > 0:
            self.__pages = pages
        else:
            raise ValueError("Количество страниц должно быть положительным")

    @property
    def get_info(self):
        return f"'{self.__title}', by {self.__author}, {self.__pages} pages"

    @get_info.setter
    def get_info(self, new_title, new_author, new_pages):
        self.__author = new_author
        self.__title = new_title
        self.__pages = new_pages

    def is_short(self):
        return self.__pages < 100
