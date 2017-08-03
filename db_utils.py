

def insert_into_schedule(prize_bond_id, city_id, date, day):
    return """INSERT INTO prize_bond_schedule (prize_bond_id,
                                                city_id,
                                                date,
                                                day)
                        VALUES ({prize_bond_id},
                                {city_id},
                                '{date}',
                                '{day}');""".format(
        prize_bond_id=prize_bond_id,
        city_id=city_id,
        date=date,
        day=day
    )


def insert_into_results(prize_bond_id, schedule_id, prize_bond_number,
                        prize_position, date, day):
    return """INSERT INTO prize_bond_results (prize_bond_id,
                                              schedule_id,
                                              prize_bond_number,
                                              prize_position,
                                              date,
                                              day)
                            VALUES ({prize_bond_id},
                                    {schedule_id},
                                    {prize_bond_number},
                                    {prize_position},
                                    '{date}',
                                    '{day}');""".format(
        prize_bond_id=prize_bond_id,
        schedule_id=schedule_id,
        prize_bond_number=prize_bond_number,
        prize_position=prize_position,
        date=date,
        day=day
    )