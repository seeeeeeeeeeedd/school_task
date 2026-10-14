from person import Person


class Teacher(Person):
    def __init__(self, name: str, surname: str, age: int, subject: str):
        super().__init__(name, surname, age)

        is_valid = self.__is_valid_subject(subject)

        if is_valid:
            self.__subject = subject.lower()
        else:
            self.__subject = 'Неизвестный предмет'

    def get_role(self) -> str:
        return 'учитель'

    def greet(self) -> str:
        basic_info = super().greet()
        teacher_info = f'{basic_info} Мой предмет: {self.get_subject()}'

        return teacher_info

    def get_subject(self) -> str:
        return self.__subject

    def __is_valid_subject(self, subject: str) -> bool:
        if isinstance(subject, str):
            if subject.strip():
                return True

        return False
