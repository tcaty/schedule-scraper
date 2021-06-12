import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent


class Scraper:

    def __init__(self, url):
        headers = {'User-Agent': generate_user_agent(device_type='desktop', os=('mac', 'linux'))}
        self.__url = url
        self.__response = requests.get(self.__url, timeout=5, headers=headers)
        self.__soup = BeautifulSoup(self.__response.text, 'lxml')

    def __get_data(self, tag, tag_class=None):
        data = []
        tags = self.__soup.find_all(tag, class_=tag_class)
        for tag in tags:
            data.append(tag.text)
        return data

    def get_auditoriums_or_teachers(self, choice):
        """choice=0 => auditoriums, choice=1 => teachers"""
        auditoriums_and_teachers = self.__get_data('a', 'glink')
        result = []
        for i in range(len(auditoriums_and_teachers)):
            if i % 2 == choice:
                result.append(auditoriums_and_teachers[i])
        return result

    def get_date_and_time(self):
        date_and_time_list = self.__get_data('td', 'time')
        date, time, temp_list = [], [], []
        for element in date_and_time_list:
            if element.find(' ') != -1 and element.find('(') != -1:
                date.append(element)
                time.append(temp_list)
                temp_list = []
            else:
                temp_list.append(element)
        return dict(zip(date, time[1:]))

    def get_subjects(self):
        return self.__get_data('span', 'disc')[7:]

    def print_data(self):
        print(f'SUBJECTS -> {self.get_subjects()}')
        print(f'AUDITORIUMS -> {self.get_auditoriums_or_teachers(0)}')
        print(f'TEACHERS -> {self.get_auditoriums_or_teachers(1)}')
        print(f'DATE AND TIME -> {self.get_date_and_time()}')

    def __str__(self):
        return 'Подключение прошло успешно' if self.__response else 'Не удалось подключиться'
