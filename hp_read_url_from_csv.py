import requests
import random
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

begin = time.time()


product_title_list = []
brand_name_list = []
mrp_list = []
sale_price_list = []
product_discount_list = []
product_description_list = []
seller_name_list = []
seller_rating_list = []
product_ratings_list = []
reviews_count_list = []
star_ratings_list = []
upc_list = []
color_list = []
model_list = []
headphone_type_list = []
sweat_proof_list = []
water_resistance_list = []
microphone_data_list = []
connectivity_data_list = []
battery_data_list = []

headers_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
]


def time_delay():  # code to add a time delay between requests
    list1 = [1, 2, 2.6, 2.8, 3.1, 3.6, 4, 4.5, 5.5, 6]
    x = random.choice(list1)
    time.sleep(x)


user_agent = random.choice(headers_list)

headers = {'User-Agent': user_agent}

data = pd.read_csv("headphonesV1.csv")

link_list = data['Product_url'].tolist()

def get_title(soup):  # function to extract title #tested ok
    try:
        title = soup.find('span', attrs={'class': 'B_NuCI'}).text.strip()

        print(f" The is title {title}")

    except AttributeError:

        title = " Title not available"

    return title


def convert(lst):  # This function converts consecutive items of a list into key value pairs. This comes in handy when we have extracted the td values on the get_spec function
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


def get_spec_list(soup):

    listofspecs = []

    columns = soup.find_all('td')

    for col in columns:

        listofspecs.append(col.text.strip())

    spec_dict = convert(listofspecs)  # converting the list of specifications into key value pairs

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
        print(f"The sweat proof data is {sweat_proof_data}")

    return sweat_proof_data


def water_resistant(soup):

    dict_data = get_spec_list(soup)

    try:

        water_resistance_data = dict_data['Water Resistant']
        print(f"The product {water_resistance_data} water resistant")

    except Exception as e:

        water_resistance_data = "Not available"
        print(water_resistance_data)

    return water_resistance_data


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

        def convert_list(string):
            list1 = []
            list1[:0] = string
            return list1

        my_list = convert_list(seller_string)

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

count_of_links = 0

def parse_data():

    for link in link_list:

        count_of_links = count_of_links +1

        percentage_completion = (count_of_links/len(link_list))*100

        print(f"The percentage completion is {percentage_completion} %")

        new_page = requests.get(link, headers=headers, timeout=5)

        if new_page.status_code == 200:

            new_soup = BeautifulSoup(new_page.text, 'lxml')

            title_data = get_title(new_soup)
            product_title_list.append(title_data)

            brand_data = get_brand(new_soup)
            brand_name_list.append(brand_data)

            mrp_data = get_mrp(new_soup)
            mrp_list.append(mrp_data)

            sale_price_data = get_sale_price(new_soup)
            sale_price_list.append(sale_price_data)

            discount_data = get_discount(new_soup)
            product_discount_list.append(discount_data)

            description_data = get_description(new_soup)
            product_description_list.append(description_data)

            seller_name_data = get_seller_name(new_soup)
            seller_name_list.append(seller_name_data)

            seller_rating_data = get_seller_star_rating(new_soup)
            seller_rating_list.append(seller_rating_data)

            ratings_data = get_ratings(new_soup)
            product_ratings_list.append(ratings_data)

            reviews_data = get_reviews_count(new_soup)
            reviews_count_list.append(reviews_data)

            star_ratings_data = get_star_rating(new_soup)
            star_ratings_list.append(star_ratings_data)

            upc_data = get_upc(link)
            upc_list.append(upc_data)

            color = get_color(new_soup)
            color_list.append(color)

            model = get_model(new_soup)
            model_list.append(model)

            headphone_type = get_headphone_type(new_soup)
            headphone_type_list.append(headphone_type)

            sweat_proof_data = sweat_proof(new_soup)
            sweat_proof_list.append(sweat_proof_data)

            water_resistance = water_resistant(new_soup)
            water_resistance_list.append(water_resistance)

            microphone_data = microphone(new_soup)
            microphone_data_list.append(microphone_data)

            connectivity_data = connectivity(new_soup)
            connectivity_data_list.append(connectivity_data)

            battery_data = battery_life(new_soup)
            battery_data_list.append(battery_data)

            dict1 = {'Product_url':link, 'Title': product_title_list, 'Brand': brand_name_list, 'MRP': mrp_list,
                     'Sales_Price': sale_price_list, 'Discount': product_discount_list,
                     'Description': product_description_list, 'Seller_name': seller_name_list,
                     'Seller_star_rating': seller_rating_list, 'Ratings_count': product_ratings_list,
                     'Reviews_count': reviews_count_list, 'Product_Star_ratings': star_ratings_list, 'UPC': upc_list,
                     'Color': color_list, 'Model': model_list,
                     'Headphone_type': headphone_type_list, 'Is_sweat_proof': sweat_proof_list,
                     'Is_water_resistant': water_resistance_list, 'Microphone': microphone_data_list,
                     'Connectivity': connectivity_data_list, 'Battery_life': battery_data_list}

            df = pd.DataFrame(dict1)

            df.to_csv('headphones_pandas2.csv')

        else:

            pass

        time_delay()


parse_data()

end = time.time()
print(f"Total runtime of the program is {end - begin}")