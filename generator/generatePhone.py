##
# @author Yamao Cuzou <yamao.cuzou@ynov.com>
 # @file Description
 # @desc Created on 2023-10-23 7:12:08 pm
 # @copyright Cuzou Corporation
 #

import random

def generate_random_french_phone_number():
    prefix = ["06", "07"]
    phone_number = prefix[random.randint(0, 1)]
    for _ in range(8):
        phone_number += str(random.randint(0, 9))
    return phone_number

phone_numbers = [generate_random_french_phone_number() for _ in range(1000)]

with open("numeros_telephone_francais.csv", "w") as file:
    file.write("Tel\n")
    for phone_number in phone_numbers:
        file.write(f"{phone_number}\n")
