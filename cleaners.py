import datetime


def prize_bond_cleaner(p_b):
    for obj in p_b.split():
        if obj.isdigit():
            return int(obj)
    if '40,0000 PREMIUM Bond' in p_b:
        return '40000 Premium'


def city_cleaner(city):
    return city.split('/-')[1].split(' ')[-1].lower().title()


def date_cleaner(date):
    return date.split(':')[-1].lstrip()


def second_prize_cleaner(p_b):
    return p_b.split('\n')[-1].replace('S:', '').split(',')


def third_prize_cleaner(p_b):
    return [i.text for i in p_b]


# database formaters

def weekday_cleaner(day_number):
    day, month, year = day_number.split('-')
    number_of_day = datetime.datetime(int(year),
                                      int(month),
                                      int(day)
                                      ).weekday()
    return {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }[number_of_day]


def prize_bond_into_id(p_b):
    if not isinstance(p_b, str):
        p_b = str(p_b)
    return {
        '100': 1,
        '200': 2,
        '750': 3,
        '1500': 4,
        '7500': 5,
        '15000': 6,
        '25000': 7,
        '40000': 8,
        '40000 Premium': 9
    }[p_b]


def city_into_id(city):
    return {
        'Rawalpindi': 1,
        'Faisalabad': 2,
        'Quetta': 3,
        'Peshawar': 4,
        'Hyderabad': 5,
        'Muzafarabad': 6,
        'Muzaffarabad': 6,
        'Karachi': 7,
        'Lahore': 8,
        'Multan': 9,
        'Islamabad': 10,
        'Gujranwala': 11,
        'Bahawalpur': 12,
        'Sialkot': 13,
        'Sukkur': 14
    }[city]


def date_to_db_date(date):
    day, month, year = date.split('-')
    return datetime.datetime(int(year),
                             int(month),
                             int(day))
