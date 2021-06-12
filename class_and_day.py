class Class:

    def __init__(self, time, subject, auditorium, teacher):
        self.__time = time
        self.__subject = subject
        self.__auditorium = auditorium
        self.__teacher = teacher

    def print_info(self):
        for key in self.__dict__.keys():
            print(f'{key} : {self.__dict__[key]}')
        print('-' * 30)

    def get_info_for_txt(self):
        res = ''
        for key in self.__dict__.keys():
            res += self.__dict__[key] + '\n'
        return res + '\n'

    def get_time(self):
        return self.__time

    def get_subject(self):
        return self.__subject

    def get_auditorium(self):
        return self.__auditorium

    def get_teacher(self):
        return self.__teacher


class Day:

    def __init__(self, date, classes):
        self.__date = date
        self.__classes = classes

    def get_date(self):
        return self.__date

    def get_classes(self):
        return self.__classes

    def __str__(self):
        return self.__date
