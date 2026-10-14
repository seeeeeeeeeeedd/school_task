class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.__min_age = 0
        self.__max_age = 100

        is_valid_text = self.__is_valid_text(name, gender)
        is_valid_number = self.__is_valid_number(age)

        if is_valid_text and is_valid_number:
            self.__name = name
            self.__age = age
            self.__gender = gender
        else:
            self.__name = 'Имя неизвестно'
            self.__age = 0
            self.__gender = 'Гендер неизвестен'

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_gender(self) -> str:
        return self.__gender

    def __is_valid_text(self, name: str, gender: str) -> bool:
        if isinstance(name, str) and isinstance(gender, str):
            if name.strip() and gender.strip():
                return True

        return False

    def __is_valid_number(self, age: int) -> bool:
        if isinstance(age, int):
            if age > self.__min_age and age <= self.__max_age:
                return True

        return False
