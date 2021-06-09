import pandas as pd

import datetime

import pymysql

import time

import random

start = time.time()

data = pd.read_csv("headphones-master_data.csv")  # read csv file and save this into a variable named data

link_list = data['Product_url'].tolist()  # taking athe url value from the data vaiable and turn into a list

price_list = data['Sale_price'].tolist()

price_change_list = [0,50,80,0, 100, 150, 180,0, 200, 225, 260, 300,0, 330, 450, 550,0, 650]

date_today = datetime.datetime.today() + datetime.timedelta(days=12) # adding two days to todays date

crawled_date = date_today.strftime('%Y-%m-%d') #formating the date string to write to mysql

def price_change(price_input):  # code to add a time delay between requests

    x = random.choice(price_change_list)

    if price_input == 1299 or price_input == 1099:

        change = price_input

    elif price_input>600 and price_input <999:

        change = price_input

    else:

        change = price_input + x

    print(f"The price change is {x} rupees")

    return change


connection = pymysql.connect(host='localhost',
                             user='root',
                             password='passme123@#$',
                             db='hpsize')  # connection obhect to pass the database details

my_cursor = connection.cursor()  # curser object to communicate with database

for i in range(len(link_list)):

    link = link_list[i]

    price_temp = price_list[i]

    price = price_change(price_temp)

    sql = "INSERT INTO dummy (link, price, crawled_date) VALUES (%s, %s, %s)"  # sql query to add data to database with three variables

    val = link, price, crawled_date  # the variables to be addded to the SQL query

    my_cursor.execute(sql, val)  # execute the curser obhect to insert the data

    connection.commit()  # commit and make the insert permanent

my_cursor.execute("SELECT * from dummy")  # load the table contents to verify the insert

result = my_cursor.fetchall()

for i in result:
    print(i)

connection.close()

end = time.time()

print(end - start)

print(date_today)
print(crawled_date)