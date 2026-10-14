from student import Student
from teacher import Teacher

INVALID_AGE = 0
UNKNOWN_COMMAND_MESSAGE = 'Неизвестная команда. Попробуйте снова'

commands = {
    '1': 'Добавить студента',
    '2': 'Добавить учителя',
    '3': 'Показать всех',
    '0': 'Выйти из программы'
}

ADD_STUDENT_COMMAND, ADD_TEACHER_COMMAND, SHOW_ALL_COMMAND, EXIT_COMMAND = commands.keys()

people = []


def print_commands():
    for number, command in commands.items():
        print(f'{number}: {command}')


def get_person_data():
    name = input('Укажите имя: ').strip()
    surname = input('Укажите фамилию: ').strip()
    age = input('Укажите возраст: ').strip()

    if not age.isdigit():
        print('Возраст должен быть числом')
        age = INVALID_AGE
    else:
        age = int(age)

    return name, surname, age


def show_all_people():
    if not people:
        print('Список пуст')
    else:
        for person in people:
            current_person = person.greet()
            print(current_person)


is_program_running = True

while is_program_running:
    print_commands()
    user_command_number = input('Укажите номер команды: ').strip()

    if user_command_number in commands:
        if user_command_number == ADD_STUDENT_COMMAND:
            name, surname, age = get_person_data()
            faculty = input('Укажите название факультета: ').strip()
            user_student = Student(name, surname, age, faculty)
            people.append(user_student)
        elif user_command_number == ADD_TEACHER_COMMAND:
            name, surname, age = get_person_data()
            subject = input('Укажите название предмета: ').strip()
            user_teacher = Teacher(name, surname, age, subject)
            people.append(user_teacher)
        elif user_command_number == SHOW_ALL_COMMAND:
            show_all_people()
        elif user_command_number == EXIT_COMMAND:
            print('Выход из программы')
            is_program_running = False
        else:
            print(UNKNOWN_COMMAND_MESSAGE)
    else:
        print(UNKNOWN_COMMAND_MESSAGE)
