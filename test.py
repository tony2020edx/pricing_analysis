

import pymysql



connection = pymysql.connect(host='localhost',
                             user='root',
                             password='passme123@#$',
                             db='hpsize')  # connection obhect to pass the database details




sql = "SELECT price FROM dummy WHERE crawled_date BETWEEN '2021-06-13' AND '2021-06-15'";



  # the variables to be addded to the SQL query

my_cursor = connection.cursor()

my_cursor.execute(sql)  # execute the curser obhect to insert the data

result = my_cursor.fetchall()

for i in result:
    print(i)

connection.close()
