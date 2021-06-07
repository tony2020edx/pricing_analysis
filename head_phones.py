# code description - This code extracts data from headphones category from flipkart. If you want to change the category just change the urls
# the base url list


import requests

from bs4 import BeautifulSoup

import re

import csv

import time

begin = time.time()

all_elements = []

pagination_urls = []

product_urls = []

base_url = [
    "https://www.flipkart.com/search?q=headphones&sid=0pm%2Cfcn&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=headphones%7CHeadphones+%26+Earphones&requestId=6fdb854e-1a91-4a16-afc5-9fc38f88577c&as-searchtext=head&p%5B%5D=facets.brand%255B%255D%3DJBL&p%5B%5D=facets.brand%255B%255D%3DSkullcandy&p%5B%5D=facets.brand%255B%255D%3DSennheiser&p%5B%5D=facets.brand%255B%255D%3DBose&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DboAt&p%5B%5D=facets.brand%255B%255D%3DZEBRONICS&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3DJabra&p%5B%5D=facets.brand%255B%255D%3DBeats&p%5B%5D=facets.headphone_type%255B%255D%3DIn%2Bthe%2BEar&page=",
    "https://www.flipkart.com/search?q=headphones&sid=0pm%2Cfcn&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=headphones%7CHeadphones+%26+Earphones&requestId=6fdb854e-1a91-4a16-afc5-9fc38f88577c&as-searchtext=head&p%5B%5D=facets.brand%255B%255D%3DJBL&p%5B%5D=facets.brand%255B%255D%3DSkullcandy&p%5B%5D=facets.brand%255B%255D%3DSennheiser&p%5B%5D=facets.brand%255B%255D%3DBose&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DboAt&p%5B%5D=facets.brand%255B%255D%3DZEBRONICS&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3DJabra&p%5B%5D=facets.brand%255B%255D%3DBeats&p%5B%5D=facets.headphone_type%255B%255D%3DOn%2Bthe%2BEar&page=",
    "https://www.flipkart.com/search?q=headphones&sid=0pm%2Cfcn&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=headphones%7CHeadphones+%26+Earphones&requestId=6fdb854e-1a91-4a16-afc5-9fc38f88577c&as-searchtext=head&p%5B%5D=facets.brand%255B%255D%3DJBL&p%5B%5D=facets.brand%255B%255D%3DSkullcandy&p%5B%5D=facets.brand%255B%255D%3DSennheiser&p%5B%5D=facets.brand%255B%255D%3DBose&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DboAt&p%5B%5D=facets.brand%255B%255D%3DZEBRONICS&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3DJabra&p%5B%5D=facets.brand%255B%255D%3DBeats&p%5B%5D=facets.headphone_type%255B%255D%3DTrue%2BWireless&page=",
    "https://www.flipkart.com/search?q=headphones&sid=0pm%2Cfcn&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=headphones%7CHeadphones+%26+Earphones&requestId=6fdb854e-1a91-4a16-afc5-9fc38f88577c&as-searchtext=head&p%5B%5D=facets.brand%255B%255D%3DJBL&p%5B%5D=facets.brand%255B%255D%3DSkullcandy&p%5B%5D=facets.brand%255B%255D%3DSennheiser&p%5B%5D=facets.brand%255B%255D%3DBose&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DboAt&p%5B%5D=facets.brand%255B%255D%3DZEBRONICS&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3DJabra&p%5B%5D=facets.brand%255B%255D%3DBeats&sort=popularity&page=",
    "https://www.flipkart.com/search?q=headphones&sid=0pm%2Cfcn&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=headphones%7CHeadphones+%26+Earphones&requestId=6fdb854e-1a91-4a16-afc5-9fc38f88577c&as-searchtext=head&p%5B%5D=facets.brand%255B%255D%3DJBL&p%5B%5D=facets.brand%255B%255D%3DSkullcandy&p%5B%5D=facets.brand%255B%255D%3DSennheiser&p%5B%5D=facets.brand%255B%255D%3DBose&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DboAt&p%5B%5D=facets.brand%255B%255D%3DZEBRONICS&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3DJabra&p%5B%5D=facets.brand%255B%255D%3DBeats&sort=recency_desc&page="
    ]


retry_links = []

retry_paginatin_urls = []

def generate_page_url():  # function to generate the pagination urls and save it to the list pagination urls

    for i in range(len(base_url)):

        count = 0

        while count < 40:
            page_url = base_url[i] + str(count)  # generating the url

            print(page_url)

            pagination_urls.append(page_url)  # append to the list pagination urls

            print(count)

            count = count + 1


generate_page_url()


def get_data():  # function to get product page links

    for page in pagination_urls:

        response = requests.get(page)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'lxml')

            for link in soup.find_all('a', attrs={'class': 's1Q9rs'}):
                item_url = " https://www.flipkart.com" + link.get('href')

                item_url = re.split("&", item_url)

                item_url = item_url[0]

                print(f"The url is {item_url}")

                product_urls.append(item_url)
        else:

            retry_paginatin_urls.append(link)

get_data()

unique_urls = set(product_urls)


def get_title(soup):  # function to extract title #tested ok
    try:
        title = soup.find('span', attrs={'class': 'B_NuCI'}).text.strip()

        print(f" The is title {title}")

    except AttributeError:

        title = " Title not available"

    return title


def Convert(lst):  # This function converts consecutive items of a list into key value pairs. This comes in handy when we have extracted the td values on the get_spec function
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


def get_spec_list(soup):
    listofspecs = []

    clumns = soup.find_all('td')

    for col in clumns:
        listofspecs.append(col.text.strip())

    spec_dict = Convert(listofspecs)  # converting the list of specifications into key value pairs

    return spec_dict


def get_color(soup):
    dict_data = get_spec_list(soup)

    try:
        color = dict_data['Color']
        print(f" The color name is {color}")
    except Exception as e:
        color = "Not available"
        print(color)

    return color


def get_model(soup):
    dict_data = get_spec_list(soup)

    try:
        model = dict_data['Model Name']
        print(f"The model name is {model}")

    except Exception as e:
        model = "The model data is not available"
        print(model)

    return model


def get_headphone_type(soup):
    dict_data = get_spec_list(soup)

    try:
        headphone_type = dict_data['Headphone Type']
        print(f"the headphone type is {headphone_type}")

    except Exception as e:

        headphone_type = " Type not available"
        print(headphone_type)

    return headphone_type


def sweat_proof(soup):
    dict_data = get_spec_list(soup)

    try:
        sweat_proof_data = dict_data['Sweat Proof']
        print(sweat_proof_data)
    except Exception as e:
        sweat_proof_data = "Not available"
        print(f"The sweatpro0f data is {sweat_proof_data}")

    return sweat_proof_data


def water_resistant(soup):
    dict_data = get_spec_list(soup)

    try:

        wanter_restistance_data = dict_data['Water Resistant']
        print(f"The product {wanter_restistance_data} water restistant")

    except Exception as e:

        wanter_restistance_data = "Not available"
        print(wanter_restistance_data)

    return wanter_restistance_data


def microphone(soup):
    dict_data = get_spec_list(soup)
    try:
        microphone_data = dict_data['With Microphone']
        print(f"is microphone available? - {microphone_data}")
    except Exception as e:

        microphone_data = "Not available"
        print(f"is microphone data available? - {microphone_data}")
    return microphone_data


def connectivity(soup):
    dict_data = get_spec_list(soup)

    try:
        connectivity_data = dict_data['Connectivity']
        print(f"The connectivity is {connectivity_data}")

    except Exception as e:

        connectivity_data = " Not available"
        print(connectivity_data)

    return connectivity_data

def clean_battery_string(test_string):

    if "hrs" in test_string:

        data = test_string.replace("hrs", '')
        print(data)
    elif "hr" in test_string:
        data = test_string.replace("hr", '')
        print(data)
    else:
        data = test_string
        print(data)

    return data


def battery_life(soup):
    dict_data = get_spec_list(soup)
    try:
        battery_life_data = dict_data['Battery Life']
        battery_life_data = clean_battery_string(battery_life_data)
        print(f"The battery like is {battery_life_data} ")
    except Exception as e:

        battery_life_data = "Not available"
        print(battery_life_data)

    return battery_life_data


def get_brand(soup):  # tested and verified
    try:
        brand_name = soup.find('span', attrs={'class': 'B_NuCI'}).text
        brand = brand_name.split()
        brand = brand[0]
        print(f" The brand is {brand}")

    except AttributeError:
        brand = " Not Available"

    return brand


def get_mrp(soup):  # tested ok
    try:

        mrp = soup.find('div', attrs={'class': '_3I9_wc _2p6lqe'}).text.strip()
        mrp = re.split("₹", mrp)
        mrp = mrp[-1]
        mrp = mrp.replace(',', '')

        print(f"The mrp is {mrp}")

    except AttributeError:

        try:
            mrp = soup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}).text.strip()
            mrp = re.split("₹", mrp)
            mrp = mrp[-1]
            mrp = mrp.replace(',', '')

        except AttributeError:

            mrp = "0"

    return mrp


def get_sale_price(soup):  # tested ok
    try:
        sale_price = soup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}).text.strip()
        sale_price = re.split("₹", sale_price)
        sale_price = sale_price[-1]
        sale_price = sale_price.replace(',', '')
        print(f"The sale_price is {sale_price}")

    except AttributeError:

        sale_price = "0"

    return sale_price


def get_discount(soup):  # tested ok
    try:
        discount = soup.find('div', attrs={'class': '_3Ay6Sb _31Dcoz'}).text.strip()
        discount = re.findall(r'\d+', discount)
        discount = discount[0]
        print(f"The discount is {discount}")

    except AttributeError:
        discount = "0"
        print("DISCOUNT NOT AVAILABLE")

    return discount


def get_description(soup):
    try:
        description = soup.find('div', attrs={'class': '_2o-xpa'}).text.strip()
        print(f"The description is {description}")
    except AttributeError:
        description = "Description Not available"
        print(description)

    return description


def get_seller_name(soup):
    try:
        seller_name_string = soup.find('div', id="sellerName").text.strip()

        try:

            seller_name = seller_name_string.replace('.', '')

            seller_name = ''.join([i for i in seller_name if not i.isdigit()])

            print(seller_name)

        except Exception as e:

            seller_name = "Not available"
            print(seller_name)

    except AttributeError:

        seller_name = "Not available"
        print(seller_name)

    return seller_name


def get_seller_star_rating(soup):
    try:
        seller_string = soup.find('div', attrs={'class': '_3LWZlK _1D-8OL'}).text.strip()

        def convert(string):
            list1 = []
            list1[:0] = string
            return list1

        my_list = convert(seller_string)

        if '.' in my_list:

            seller_rating = my_list[-3] + '.' + my_list[-1]

            print(f"the seller_rating is a float {seller_rating}")

        else:

            seller_rating = my_list[-1]
            print(f" the seller_rating is integer {seller_rating}")

    except AttributeError:
        seller_rating = 0
        print(f"the rating is {seller_rating}")

    return seller_rating


def get_ratings(soup):
    try:
        number_of_ratings = soup.find('span', attrs={'class': '_2_R_DZ'}).text
        try:
            temp = number_of_ratings.split()
            ratings = temp[0].strip()
            ratings = ratings.replace(',', '')
            print(f" the ratings are {ratings}")
        except IndexError:
            ratings = "0"
    except AttributeError:
        ratings = "0"

    return ratings


def get_reviews_count(soup):
    try:

        user_string = soup.find('span', attrs={'class': '_2_R_DZ'}).text

        user_string = user_string.split()

        try:
            reviews = user_string[-2]

            reviews = reviews.replace(',', '')

            print(f" the reviews are {reviews}")

        except IndexError:

            reviews = "Not available"
            print(reviews)

    except AttributeError:

        reviews = "0"
        print(f" the review of the product is  {reviews}")

    return reviews


def get_star_rating(soup):
    try:

        star_rating = soup.find('div', attrs={'class': '_2d4LTz'}).text.strip()
        print(f" the star_rating is {star_rating}")

    except AttributeError:

        star_rating = "Not available"
        print(f" the star_rating is {star_rating}")

    return star_rating


def get_upc(link):
    try:

        upc = re.split("=", link)
        upc = upc[-1]
        upc = upc.replace(',', '')

        print(f"The upc is {upc}")

    except AttributeError:
        upc = "Not available"

    return upc


def parse_data():

    for link in unique_urls:

        new_page = requests.get(link)

        if new_page.status_code == 200:

            new_soup = BeautifulSoup(new_page.text, 'lxml')

            title_data = get_title(new_soup)
            brand_data = get_brand(new_soup)
            mrp_data = get_mrp(new_soup)
            sale_price_data = get_sale_price(new_soup)
            discount_data = get_discount(new_soup)
            description_data = get_description(new_soup)
            seller_name_data = get_seller_name(new_soup)
            seller_rating_data = get_seller_star_rating(new_soup)
            ratings_data = get_ratings(new_soup)
            reviews_data = get_reviews_count(new_soup)
            star_ratings_data = get_star_rating(new_soup)
            upc_data = get_upc(link)
            color = get_color(new_soup)
            model = get_model(new_soup)
            headphone_type = get_headphone_type(new_soup)
            sweat_proof_data = sweat_proof(new_soup)
            water_resistance = water_resistant(new_soup)
            microphone_data = microphone(new_soup)
            connectivity_data = connectivity(new_soup)
            battery_data = battery_life(new_soup)

            all_elements.append(  # saving all elements to a list
                {

                    "Product_url": link,
                    "brand": brand_data,
                    "Title": title_data,
                    "Description": description_data,
                    "Sale_price": sale_price_data,
                    "MRP": mrp_data,
                    "Discount_percentage": discount_data,
                    "Seller_name": seller_name_data,
                    "seller_rating": seller_rating_data,
                    "Number_of_ratings": ratings_data,
                    "Number_of_reviews": reviews_data,
                    "UPC": upc_data,
                    "Star_rating_of_the_product": star_ratings_data,
                    "Color": color,
                    "Model": model,
                    "Headphone Type": headphone_type,
                    "Is sweatproof": sweat_proof_data,
                    "Is water resistant": water_resistance,
                    "Microphon": microphone_data,
                    "Connectivity": connectivity_data,
                    "Battery life": battery_data

                })

            keys = all_elements[0].keys()

            with open('headphones.csv', 'w', newline='') as output_file:  # writing all elements to csv
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(all_elements)

        else:

            retry_links.append(link)


parse_data()
print(len(product_urls))
print(len(unique_urls))
print(len(retry_links))
print(retry_links)
end = time.time()
print(f"Total runtime of the program is {end - begin}")