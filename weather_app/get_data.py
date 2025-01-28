import requests
import pandas as pd
# Temporarily display all rows and columns
pd.set_option("display.max_rows", None)  # Show all rows
pd.set_option("display.max_columns", None)  # Show all columns
import numpy as np
import json
import geonamescache



gc = geonamescache.GeonamesCache()
cities = gc.get_cities()

us_cities = [city['name'] for city in cities.values() if city['countrycode'] == 'US']

# for i in us_cities:
#     if i[0] == "N":
#         print(i)



#import matplotlib.pyplot as plt



def get_data():

    api_key = "fe20495282cee3be06f5caeb0a08c173"
    url = f"https://api.weatherstack.com/current?access_key={api_key}"
    params_values = {"query":"New York", "u":"f"}
    response = requests.get(url, params=params_values)
    json_data = response.json()

    with open("data.json", "a") as file:
        file.write(f"{json_data}")
        
    print(f"Data successfully transfered to {file.name}. ")


with open("data.json", "r") as file:
    data=json.load(file)



df = pd.json_normalize(data)
filterd_data=df[["request.type","request.query"]]
#df_filtered=data["request.city"]

#print(df)
#print(filterd_data)
#print(df["request.location"])




print("What city would you like to query? *type \"List\" to see list of Cities.\n")
while True: 
    query_city = input("City:")
    if query_city.strip() == "":
        print("Invalid input. Please try again")
        continue
    

    int_check=False
    for i in query_city:
        try:
            int(i)
            print("Invalid input. Please try again")
            int_check = True
            break
        except Exception as e:
            continue
    

    if query_city not in  us_cities:
        if query_city == "List":
            print(us_cities)
            continue
        else:
            print("Invalid input. Please try again")
            continue






    if int_check == False:
        print(f"City Selected: {query_city}")

    if query_city == "List":
        print(us_cities)
        continue

    break


    



print(" are you looking for a specific date?")
date_response = input("Yes or No:")
if date_response in ["Yes", "YES", "yes", "yEs", "yeS", "YEs", "yES", "YeS"]:
    print("What year are you looking for?")
    while True:
        response_year = input("Year:")

        if response_year.strip == "":
            print("Invalid input. Please try again")
            continue

        if len(response_year) != 4:
            print("Invalid input. Please try again")
            continue

        for i in response_year:
            if i.isdigit == False:
                print("Invalid input. Please try again")
                continue               
        if int(response_year) > 2025:
            print("Invalid input. Please try again")
            continue

        break

if date_response in ["No","no","NO","nO"]:
    date_response = False

if date_response != False:
    print(response_year)

