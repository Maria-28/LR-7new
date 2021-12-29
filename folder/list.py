#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def list():
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20}'.format(
            "No",
            "Пункт",
            "Начало",
        )
    )
    print(line)

    # Вывести данные о всех рейсах.
    for idx, stations in enumerate(station, 1):
        print(
            '| {:>4} | {:<30} | {:<20} |'.format(
                number,
                stations.get('finish', ''),
                stations.get('start', ''),
            )
        )

    print(line)
