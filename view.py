import model


def input_class():
    while True:
        in_class = input('С каким классом работаем? ').upper()
        if in_class == '7А':
            return in_class
        else:
            print('Такого класса нет, введите другой ')
            return input_class()


def input_subject():
    while True:
        in_subject = input('Какой предмет? ').lower()
        if in_subject in 'химияматематикафизика':
            return in_subject
        else:
            print('Такого предмета нет, введите другой ')
            return input_subject()


def who_answer():
    while True:
        in_student = input('Кто будет отвечать? ')
        if in_student in 'Петров Петр Алексеев Алексей Смирнов Серега exit выход':
            return in_student
        else:
            print('Такого студента нет, выберите другого ')
            return who_answer()


def what_mark():
    while True:
        in_mark = int(input('На какую оценку ответил? '))
        if 0 < in_mark < 6:
            return in_mark
        else:
            print('Выбери оценку от 1 до 5 ')
            return what_mark()


def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        average_mark = 0
        st_mark_1 =[]
        for mark in journal.get(child):
            average_mark += round(mark/(len(journal.get(child))), 2)
            st_mark_1.append(str(mark))
        st_mark_2 = ', '.join(st_mark_1)
        print(f'{i}. {child:20} {st_mark_2:20}\t ср.балл: {average_mark}')