# Напечатайте номер заказа
# Напечатайте адрес отправки
# Напечатайте описание посылки, ее стоимость и кол-во
# Сконвертируйте yaml файл в json
# Создайте свой yaml файл

import yaml
import json


def order_number():
    """Print the number of order"""
    with open("order.yaml") as f:
        templates = yaml.safe_load(f)
        txt = templates["invoice"]
        print("The number of order: ", txt)


def sending_address():
    """Print sending address"""
    with open("order.yaml") as f:
        templates = yaml.safe_load(f)
        txt = templates["bill-to"]["address"]
        print("Sending address:", txt)


def parcel_data():
    """Print parcel description, price and quantity"""
    with open("order.yaml") as f:
        templates = yaml.safe_load(f)
        txt_1 = templates["product"][0]
        print("The first parcel:", txt_1)
        txt_2 = templates["product"][1]
        print("The second parcel:", txt_2)


def convert_to_json():
    """Convert file yaml in file json"""
    in_file = "order.yaml"
    out_file = "order.json"

    with open(in_file, "r") as i:
        data = yaml.safe_load(i)
    with open(out_file, "w") as o:
        json.dump(data, o, indent=4)


def create_yaml():
    """Create own yaml file with datas about tv-show "Black mirror"""
    yaml_str = """\
    Black Mirror:
        episod1: 
            name: The National Anthem
            release date: 2011-12-4
        episod2:
            name: Fifteen Million Merits
            release date: 2011-12-11
        episod3:
            name: The Entire History of You
            release date: 2011-12-18
                
    """

    data = yaml.safe_load(yaml_str)
    print(data)


print(order_number())
print()
print(sending_address())
print()
print(parcel_data())
print()
print(convert_to_json())
print()
print(create_yaml())


