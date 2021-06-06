import pandas as pd

import pymysql

import time

start = time.time()

data = pd.read_csv("headphones-master_data.csv")  # read csv file and save this into a variable named data

link_list = data['Product_url'].tolist()  # taking athe url value from the data vaiable and turn into a list

price_list = data['Sale_price'].tolist()

crawled_date = time.strftime('%Y-%m-%d')  # generate the date format compatiable with mysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='passme123@#$',
                             db='hpsize')  # connection obhect to pass the database details

my_cursor = connection.cursor()  # curser object to communicate with database

for i in range(len(link_list)):
    link = link_list[i]

    price = price_list[i]

    sql = "INSERT INTO comparison (link, price, crawled_date) VALUES (%s, %s, %s)"  # sql query to add data to database with three variables

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
