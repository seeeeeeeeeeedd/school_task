from person import Person


class Student(Person):
    def __init__(self, name: str, surname: str, age: int, faculty: str):
        super().__init__(name, surname, age)

        is_valid = self.__is_valid_faculty(faculty)

        if is_valid:
            self.__faculty = faculty
        else:
            self.__faculty = 'Неизвестный факультет'

    def get_role(self) -> str:
        return 'Студент'

    def greet(self) -> str:
        basic_info = super().greet()
        student_info = f'{basic_info} Мой факультет: {self.get_faculty()}'

        return student_info

    def get_faculty(self) -> str:
        return self.__faculty

    def __is_valid_faculty(self, faculty: str) -> bool:
        if isinstance(faculty, str):
            if faculty.strip():
                return True

        return False
