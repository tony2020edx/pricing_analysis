import pandas as pd

df = pd.read_csv("kbk.csv")

link_list = df['link'].tolist()

unique_urls = set(link_list)

prices = df['price'].tolist()

dates = df['crawled_date'].tolist()

unique_dates = set(dates)

change_list = []

precentage_change = []

offset_value = len(unique_urls)

limiting_value = len(link_list) - offset_value


def percentage_change(old_price, new_price):  # get the percentage change by accepting two inputes

    change_metric = new_price - old_price

    if change_metric == 0:

        price_change_percentage = 0
    else:

        price_change_percentage = (change_metric / old_price) * 100

        price_change_percentage = round(price_change_percentage, 2)

    return price_change_percentage


for count in range(len(link_list)):

    if count < offset_value:

        change = 0

        change_list.append(change)
        precentage_change.append(change)

    else:

        price1 = prices[count]

        next_count = count - offset_value

        if next_count < len(link_list):

            price2 = prices[next_count]

            change = price2 - price1

            change_list.append(change)

            get_change = percentage_change(price2, price1)

            precentage_change.append(get_change)

        else:

            pass

print(change_list)
print(precentage_change)

print(len(change_list))
