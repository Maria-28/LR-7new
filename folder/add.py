#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add():
    # Запросить данные .
    finish = input("Название пункта назначения рейса ")
    number = input("Номер рейса ")
    start = input("Начального пункта ")

    # Создать словарь.
    st = {
        'finish': finish,
        'number': number,
        'start': start,
    }

    # Добавить словарь в список.
    station.append(st)
    # Отсортировать список в случае необходимости.
    if len(station) > 1:
        station.sort(key=lambda item: item.get('finish', ''))