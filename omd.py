from random import randint
import random


def step2_umbrella():
    print('Утка-маляр 🦆 взяла зонтик и отправилась в бар под дождем')
    time_to_bar = randint(1, 20)
    if time_to_bar > 10:
        event = random.choice(['познакомилась с певцом-гитаристом 🎸',
                               'подарила свой зонтик незнакомому прохожему 🌂',
                               'начала танцевать под дождем 💃'])
    else:
        event = random.choice(['встретила старого друга и провела веселый вечер 🥂',
                               'промокла до нитки, но стала настоящей героиней в баре 💪'])
    print(f'В баре утка-маляр {event}.')


def step2_no_umbrella():
    print('Утка-маляр решила вспомнить, как часто она выпивает')
    dates = {27: 'Выпивала за праздник "День уток"',
             15: 'Выпиывала с уткой одногруппником',
             13: 'Выпивала за день единства уток и человеков 🦆🤝👤 ',
             666: 'Выпивала за день утки-дьявола😈'}
    print('К сожалению утка-маляр из-за того, что часто пьет'
          'все перепутала и в ее голове картинка выглядела так')
    for day, action in enumerate(dates.values()):
        print(f'В данное число {day} первого месяца я {action}')
    print('Что-то я часто пью решила утка и осталась дома')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
