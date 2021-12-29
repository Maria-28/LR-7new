#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select():
    parts = command.split(' ', maxsplit=2)
    sel = (parts[1])

    count = 0
    for stations in station:
        if stations.get('finish') == sel:
            count = number
            print(
                '{:>4}: {}'.format(count, stations.get('start', ''))
            )
            print('Номер рейса:', stations.get('number', ''))
            print('Пункт:', stations.get('finish', ''))

    # Если счетчик равен 0, то рейсы не найдены.
    if count == 0:
        print("Рейс не найден.")
        