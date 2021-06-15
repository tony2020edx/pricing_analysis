import pandas as pd

import pymysql

df = pd.read_csv("pricing1.csv")

link_list = df['link'].tolist()

date_list = df["crawled_date"].tolist()

prices = df['price'].tolist()

precentage_changes = []

change_list = []

unique_urls = set(link_list)

offset_value = len(unique_urls)

limiting_value = len(link_list) - offset_value


def percentage_change(old_price, new_price):  # get the percentage change by accepting two inputes

    difference_in_price = new_price - old_price

    if difference_in_price == 0:

        price_change_percentage = 0

    else:

        if old_price == 0:

            price_change_percentage = 0

        else:
            price_change_percentage = (difference_in_price / old_price) * 100
            price_change_percentage = round(price_change_percentage, 2)

    return price_change_percentage


for count in range(len(link_list)):

    if count < offset_value:

        change = 0

        change_list.append(change)

        precentage_changes.append(change)

    else:

        price1 = prices[count]

        next_count = count - offset_value

        if next_count < len(link_list):

            price2 = prices[next_count]

            change = price2 - price1

            change_list.append(change)

            get_change = percentage_change(price2, price1)

            precentage_changes.append(get_change)

        else:

            pass

for value in precentage_changes:
    print(value)

print(len(precentage_changes))

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='passme123@#$',
                             db='hpsize')  # connection object to pass the database details

my_cursor = connection.cursor()  # cursor object to communicate with database

for i in range(len(link_list)):

    link = link_list[i]

    price = prices[i]

    crawled_date = date_list[i]

    price_change = change_list[i]

    precentage_change = precentage_changes[i]

    sql = "INSERT INTO sample (link, price, crawled_date, price_change,precentage_change) VALUES (%s, %s, %s,%s,%s)"  # sql query to add data to database with three variables

    val = link, price, crawled_date,price_change,precentage_change  # the variables to be added to the SQL query

    my_cursor.execute(sql, val)  # execute the cursor object to insert the data

    connection.commit()  # commit and make the insert permanent

my_cursor.execute("SELECT * from sample")  # load the table contents to verify the insert

result = my_cursor.fetchall()

for i in result:
    print(i)

connection.close()


