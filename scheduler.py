import pandas as pd

import random

import requests

from bs4 import BeautifulSoup

import re

import pymysql

import time

start = time.time()

data = pd.read_csv("headphones-master_data.csv")  # read csv file and save this into a variable named data

link_list = data['Product_url'].tolist()  # taking athe url value from the data variable and turn into a list

mrp_list = []  # the list is populated when the parser function executes

headers_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
]  # list of headers


def time_delay():  # code to add a time delay between requests
    list1 = [2, 3, 3.5, 4, 6.1, 6.2, 2, 3, 6.5, 6.6, 6.7, 6.9]
    x = random.choice(list1)
    print(f"The time delay is {x} seconcs")
    time.sleep(x)


crawled_date = time.strftime('%Y-%m-%d')


def get_sale_price(soup):  # get the sale price of the product

    try:
        sale_price = soup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}).text.strip()
        sale_price = re.split("₹", sale_price)
        sale_price = sale_price[-1]
        sale_price = sale_price.replace(',', '')
        print(f"The sale_price is {sale_price}")

    except AttributeError:

        sale_price = "0"

    return sale_price


def percentage_completion(list2, url):  # code to understand the percentage completion of scraping

    index_value = list2.index(url)

    temp = 1 - (((len(list2) + 1) - index_value) / len(list2))

    percentage = round(temp * 100, 2)

    print(f'the percentage completion is {percentage} %')


def parse_data(url_list):  # parse the data by fecting the url from the list.

    for links in url_list:

        print(links)

        user_agent = random.choice(headers_list)

        headers = {'User-Agent': user_agent}  # randomise user agent

        percentage_completion(url_list, links)

        new_page = requests.get(links, headers=headers)

        if new_page.status_code == 200:

            new_soup = BeautifulSoup(new_page.text, 'lxml')

            mrp_data = get_sale_price(new_soup)
            mrp_list.append(mrp_data)

        else:
            pass

        time_delay()


parse_data(link_list)

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='passme123@#$',
                             db='hpsize')  # connection obhect to pass the database details

my_cursor = connection.cursor()  # curser object to communicate with database

for i in range(len(mrp_list)):
    link = link_list[i]

    price = mrp_list[i]

    sql = "INSERT INTO pricing_analysis (link, price, crawled_date) VALUES (%s, %s, %s)"  # sql query to add data to database with three variables

    val = link, price, crawled_date  # the variables to be addded to the SQL query

    my_cursor.execute(sql, val)  # execute the curser obhect to insert the data

    connection.commit()  # commit and make the insert permanent

my_cursor.execute("SELECT * from comparison")  # load the table contents to verify the insert

result = my_cursor.fetchall()

for i in result:
    print(i)

connection.close()

end = time.time()

print(end - start)
