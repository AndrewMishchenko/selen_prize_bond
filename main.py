import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup

from cleaners import (prize_bond_cleaner,
                      city_cleaner,
                      date_cleaner,
                      second_prize_cleaner,
                      third_prize_cleaner,
                      weekday_cleaner)

driver_path = '/home/andrew/development/1_parsers/' \
              'selenium/selen_prize_bond/chromedriver'
driver = webdriver.Chrome(driver_path)

domain = 'https://www.prizebond.net/dlist.php?num='

current_page = 1
end_page = 464

to_json = {'data': []}
while current_page <= end_page:
    try:
        driver.get(domain + str(current_page))
        time.sleep(5)
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')

        blog_page_content = soup.find_all(
            'div', {
                'class': 'col-md-7 blog-page-content'
            })

        prize_bond = prize_bond_cleaner([i.select('h4 span')[0]
                                         for i in blog_page_content][0].text)

        city = city_cleaner([i.select('h4')[0]
                             for i in blog_page_content][0].text)
        date = date_cleaner([i.select('h3')[0]
                             for i in blog_page_content][0].text)

        first_prize = [i.select('div h1')[0]
                       for i in blog_page_content][0].text

        second_prize = second_prize_cleaner(
            [i.select('h4') for i in blog_page_content][0][-1].text)

        third_prize = third_prize_cleaner(
            soup.find_all('td', {'class': 'tab1'}))

        day = weekday_cleaner(date)

        data = {
            'prize_bond': prize_bond,
            'city': city,
            'date': date,
            'day': day,
            'first_prize': first_prize,
            'second_prize': second_prize,
            'third_prize': third_prize
        }
        to_json['data'].append(data)
        current_page += 1
        print('go to page # - ', current_page)
    except Exception as err:
        print(err)
        current_page += 1
        continue

driver.close()

with open('result.json', 'w') as doc:
    json.dump(to_json, doc, indent=2)
