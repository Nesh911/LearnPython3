# Задание - Напечатайте в консоль даты: вчера, сегодня, месяц назад
#           Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import *
import locale
# locale.setlocale(locale.LC_TIME, "ru_RU")  для IOS
locale.setlocale(locale.LC_ALL, "russian")


# "A timedelta object represents a duration, the difference between two dates or times.
# class datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
# All arguments are optional and default to 0. Arguments may be ints, longs, or floats, and may be positive or negative"
# https://docs.python.org/2/library/datetime.html


def show_date():
    user_input = input('Когда? ')
    date_now = datetime.now()
    today = date_now.strftime('%d.%m.%Y'+', '+'%A')
    delta = timedelta(days=1)
    mdelta = timedelta(weeks=4)
    yesterday = date_now - delta
    tomorrow = date_now + delta
    month_later = date_now + mdelta
    month_ago = date_now - mdelta
    quest = {'сегодня': today,
             'вчера': yesterday,
             'завтра': tomorrow,
             'через месяц': month_later,
             'месяц назад': month_ago}
    if user_input in quest:
        print(quest[user_input].strftime('%d.%m.%Y'+','+'%A'))


def date_string():
    date_str = '01/01/17 12:10:03.234567'
    date_dt = datetime.strptime(date_str, '%m/%d/%y %H:%M:%S.%f')
    print(date_dt)


# date_string()
show_date()




