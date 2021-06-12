from scraper import Scraper
from class_and_day import Class, Day


group = input('Введите номер группы: ')
url = 'http://schedule.tsu.tula.ru/?group=' + group
scraper = Scraper(url)
print(scraper)

date_and_time = scraper.get_date_and_time()
subjects = scraper.get_subjects()
auditoriums = scraper.get_auditoriums_or_teachers(0)
teachers = scraper.get_auditoriums_or_teachers(1)

i = 0
days, temp = [], []

for date in date_and_time.keys():
    for time in date_and_time[date]:
        temp.append(Class(time, subjects[i], auditoriums[i], teachers[i]))
        i += 1
    days.append(Day(date, temp))
    temp = []

with open(group + '.txt', 'w') as file:
    file.write('-' * 70 + '\n' * 2)
    for day in days:
        file.write(day.get_date().upper() + '\n' * 2)
        for study_class in day.get_classes():
            file.write(study_class.get_info_for_txt())
        file.write('-' * 70 + '\n' * 2)
        print(f'{day} - записан в файл')
