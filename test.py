import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='passme123@#$',
                             db='hpsize')  # connection obhect to pass the database details

sql1 = "SELECT price FROM dummy WHERE crawled_date BETWEEN '2021-06-13' AND '2021-06-15'"

sql2 = "SELECT price FROM dummy WHERE crawled_date BETWEEN '2021-06-13' AND '2021-06-15' AND link ='https://www.flipkart.com/bose-noise-cancelling-700-anc-enabled-bluetooth-headset/p/itma57a01d3bd591?pid=ACCFGYZEVVGYM8FP'"

sql = "SELECT price FROM dummy WHERE link ='https://www.flipkart.com/bose-noise-cancelling-700-anc-enabled-bluetooth-headset/p/itma57a01d3bd591?pid=ACCFGYZEVVGYM8FP'"

# the variables to be addded to the SQL query

my_cursor = connection.cursor()

my_cursor.execute(sql)  # execute the curser obhect to insert the data

result = list(my_cursor.fetchall())

print(result)

new_list = [i[0] for i in result]

print(new_list)

connection.close()
