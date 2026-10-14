class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.__min_age = 0
        self.__max_age = 100

        is_valid_text = self.__is_valid_text(name, surname)
        is_valid_number = self.__is_valid_number(age)

        if is_valid_text and is_valid_number:
            self.__name = name
            self.__surname = surname
            self.__age = age
        else:
            self.__name = 'Имя неизвестно'
            self.__surname = 'Фамилия неизвестна'
            self.__age = 0

    def get_role(self) -> str:
        return 'Человек'

    def greet(self) -> str:
        return f'Привет я {self.get_role()}. Меня зовут {self.get_name()} {self.get_surname()}, мне {self.get_age()}.'

    def get_name(self) -> str:
        return self.__name

    def get_surname(self) -> str:
        return self.__surname

    def get_age(self) -> int:
        return self.__age

    def __is_valid_text(self, name: str, surname: str) -> bool:
        if isinstance(name, str) and isinstance(surname, str):
            if name.strip() and surname.strip():
                return True

        return False

    def __is_valid_number(self, age: int) -> bool:
        if isinstance(age, int):
            if age > self.__min_age and age <= self.__max_age:
                return True

        return False
