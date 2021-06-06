import pandas as pd

import pymysql

import time

from pandas import DataFrame

start = time.time()


data = pd.read_csv("headphones-master_data.csv") #read csv file and save this into a variable named data

link_list = data['Product_url'].tolist()  #taking athe url value from the data vaiable and turn into a list

price_list = data['Sale_price'].tolist()

crawled_date = []

#crawled_date = time.strftime('%Y-%m-%d') #generate the date format compatiable with mysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='passme123@#$',
                             db='hpsize')   #connection obhect to pass the database details


my_cursor = connection.cursor() #curser object to communicate with database


def generate_df():

    for i in range(len(link_list)):

        link = link_list[i]

        price = price_list[i]

        crawled_date_data = time.strftime('%Y-%m-%d')

        crawled_date.append(crawled_date_data)

generate_df()


df = pd.DataFrame(list(zip(link_list, price_list, crawled_date)),
                      columns=['link', 'price', 'crawled_date'])

print(df)

df.to_sql('comparison',con = connection, if_exists= 'append', chunksize=1000)












