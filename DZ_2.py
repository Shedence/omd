import csv

file = 'Corp_Summary.csv'  # Файл, откуда берем данные
depart_dic_info = {}  # Словарь с информацией о депортаментах
depart_dic = {}  # Словарь с департаментами и командами внутри него
menu = '''Чтобы вывести, какие команды есть в депортаменте нажми 1
Чтобы вывести, полную информацию о депортаменте нажми 2
Чтобы сохранить отчет в виде csv файла нажми 3
'''


def prepare():
    """
    Функция, созданная для того, чтобы смоделировать данные для вывода
    в удобном и читаемом формате для нашего пользователя.
    У пользователя есть только доступ для просмотра данных, так что
    на вход в функции ничего не передается, поэтому
    аннотация типов мне тут не пригодится
    """
    with open(file, encoding='utf-8') as f:  # Cчитываем файл в кодировке utf-8
        csv_reader = csv.reader(f, delimiter=';')  # Разделяем между собой стоблцы by ;.
        for row in csv_reader:
            if row[0] != 'ФИО полностью':  # Первую строчку надо пропустить, т.к она не содержит информативных данных
                departament = row[1]
                division = row[2]
                salary = row[-1]
                salary = int(salary)  # Приводим зарплату к инту
                if departament not in depart_dic:  # Проверяем, есть ли новый считываемый департамент уже в нашем словаре
                    depart_dic[departament] = [
                        division]  # Если нет, то добавляем его в словарь, как ключ, а значения у ключа - массив его отделов
                elif division not in depart_dic[departament]:
                    depart_dic[departament].append(
                        division)  # Проверяем, если у департамента уже данный отдел, если нет то добавляем
                if departament not in depart_dic_info:  # Аналогично с информацией о департаментах
                    depart_dic_info[departament] = {'number': 1, 'max_salary': salary, 'min_salary': salary,
                                                    'sum_salary': salary}  # Хранить информацию о департаментах будем в виде словарь в словаре
                else:
                    depart_dic_info[departament]['number'] += 1  # Добавляем одного человека
                    depart_dic_info[departament]['max_salary'] = max(depart_dic_info[departament]['max_salary'],
                                                                     salary)  # Берем максимум из старой макс. зарплаты и новоый
                    depart_dic_info[departament]['min_salary'] = min(depart_dic_info[departament]['min_salary'],
                                                                     salary)  # Аналогично
                    depart_dic_info[departament]['sum_salary'] = depart_dic_info[departament]['sum_salary'] + salary


def press_one():
    """
    Выводит информацию об отделах в департаменте,
    если пользователь нажал 1
    """
    for depart in depart_dic:
        departments = ', '.join(depart_dic[depart])  # Джоиним наши отделы для красивого вывода
        print(f'Департамент: {depart} содержит отделы: {departments}\n')


def press_two():
    """
    Выводит детальную информацию о депортаментах,
    если пользователь нажал 2
    """
    for depart in depart_dic_info:
        print(f'Название департамента {depart} \n🧔Количество человек в отделе: {depart_dic_info[depart]["number"]}🧔')
        print(
            f'🤑Вилка зарплат сотрудников департамента: {depart_dic_info[depart]["min_salary"]} - {depart_dic_info[depart]["max_salary"]}🤑')
        print(
            f'👀Средняя зарплата сотрудника департамента: {round(depart_dic_info[depart]["sum_salary"] / depart_dic_info[depart]["number"], 3)}👀\n')  # Чтобы посчитать среднюю, делим сумму на кол-во и округляем до 3-его знака


def press_three():
    """
    Функция, котрая записывает информацию из функуии press_two
    в csv файлик
    """
    with open('depart_info.csv', mode='w', encoding='utf-8') as write_file:
        file_writer = csv.writer(write_file, delimiter=';', lineterminator='\r')
        file_writer.writerow(['Название', 'Численность', 'Вилка ЗП', 'Средняя зарплата'])
        for depart in depart_dic_info:
            file_writer.writerow([depart,
                                  depart_dic_info[depart]['number'],
                                  f"{depart_dic_info[depart]['min_salary']} - {depart_dic_info[depart]['max_salary']}",
                                  round(depart_dic_info[depart]["sum_salary"] / depart_dic_info[depart]["number"], 3)]
                                 )


def start():
    """
    Функция, созданная для запуска нашей программы,
    проверки, какие числа ввел пользователь
    """
    prepare()
    print(menu)
    inp = input('Введите на выбор цифру из меню \n')
    if inp not in ('1', '2', '3'):
        raise ValueError('Вы ввели цифру не из меню, попробуйте заново')  # Если пользователь ввел некорректную цифру
    elif inp == '1':
        press_one()
    elif inp == '2':
        press_two()
    elif inp == '3':
        press_three()
        print('\nФайл depart_info.csv успешно создан')


if __name__ == '__main__':
    start()
