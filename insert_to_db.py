import json
import MySQLdb
from cleaners import (prize_bond_into_id,
                      city_into_id,
                      date_to_db_date)
from db_utils import (insert_into_schedule,
                      insert_into_results)

NAME = 'prizebondlist'
USER = 'root'
PASSWORD = 'your_password_here'
HOST = '127.0.0.1'

db = MySQLdb.connect(host=HOST, user=USER,
                     passwd=PASSWORD, db=NAME)

cursor = db.cursor()

with open('result.json', 'r') as doc:
    a = json.load(doc)
    for row in a['data']:
        prize_bond_id = prize_bond_into_id(row['prize_bond'])
        city_id = city_into_id(row['city'])
        date = date_to_db_date(row['date'])
        day = row['day']
        first_prize = row['first_prize']
        second_prize = row['second_prize']
        third_prize = row['third_prize']

        # insert into table prize_bond_schedule
        try:
            cursor.execute(insert_into_schedule(prize_bond_id,
                                                city_id,
                                                date,
                                                day))
            db.commit()
        except Exception as err:
            print(err)

        # insert into table prize_bond_results
        schedule_id = cursor.lastrowid
        print('prize_bond_schedule - ', schedule_id)
        # position == 1
        try:
            prize_position = 1
            cursor.execute(insert_into_results(prize_bond_id,
                                               schedule_id,
                                               first_prize,
                                               prize_position,
                                               date,
                                               day))
            db.commit()
        except Exception as err:
            print(err)

        # position == 2
        try:
            prize_position = 2
            for number in second_prize:
                cursor.execute(insert_into_results(prize_bond_id,
                                                   schedule_id,
                                                   int(number),
                                                   prize_position,
                                                   date,
                                                   day))
                db.commit()
        except Exception as err:
            print(err)

        # position == 3
        try:
            prize_position = 3
            for number in third_prize:
                cursor.execute(insert_into_results(prize_bond_id,
                                                   schedule_id,
                                                   int(number),
                                                   prize_position,
                                                   date,
                                                   day))
                db.commit()
        except Exception as err:
            print(err)

db.close()
print('Finished!')
