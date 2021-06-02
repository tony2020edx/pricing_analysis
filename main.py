import pandas as pd

import pymysql

import time

start = time.time()




data = pd.read_csv("headphones-master_data.csv")

link_list = data['Product_url'].tolist()

price_list = data['Sale_price'].tolist()

crawled_date = time.strftime('%Y-%m-%d')

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='passme123@#$',
                             db='hpsize')


my_cursor = connection.cursor()


for i in range(len(link_list)):

    link = link_list[i]

    price = price_list[i]



    sql = "INSERT INTO comparison (link, price, crawled_date) VALUES (%s, %s, %s)"

    val = link , price , crawled_date


    my_cursor.execute(sql, val)

    connection.commit()


my_cursor.execute("SELECT * from comparison")

result = my_cursor.fetchall()

for i in result:
    print(i)

connection.close()

end = time.time()

print(end - start)
