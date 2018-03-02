# -*- coding:utf-8 -*-
from datetime import datetime


datetime_formates = [
    '%Y-%m-%d %H:%M:%S',
    '%Y-%m-%dT%H:%M:%S',
    '%Y%m%dT%H%M%S',
    '%Y/%m/%d %H:%M:%S',
    '%d/%m/%Y %H:%M:%S',
    '%d.%m.%Y %H:%M:%S',
    '%Y-%m-%dT%H:%M',
    '%Y%m%d',
    '%Y-%m-%d',
    '%Y/%m/%d',
    '%d/%m/%Y',
    '%d.%m.%Y',
]


def dformat(src=None):
    """
    if src param is None returns datetime.now()

    :param src:
    :return: datetime
    """
    if src is None:
        return datetime.now()

    for datetime_format in datetime_formates:
        date_time = formating(src=src, fmt=datetime_format)
        if date_time is not None:
            return date_time

    return datetime.now()


def formating(src, fmt):
    try:
        return datetime.strptime(src, fmt)
    except ValueError:
        return None
