import requests
import numpy as np
import json
import geonamescache
import matplotlib.pyplot as plt
import os
import sys









ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

gc = geonamescache.GeonamesCache()
cities = gc.get_cities()

us_cities = [city['name'] for city in cities.values() if city['countrycode'] == 'US']







def get_city():
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

        return query_city





def get_year():
    print("What year are you looking for?")
    while True:
        response_year = input("Year:")

        if response_year.strip() == "":
            print("Invalid input. Please try again")
            continue

        if len(response_year) != 4:
            print("Invalid input. Please try again")
            continue

        for i in response_year:
            if i.isdigit() == False:
                print("Invalid input. Please try again")
                continue               
        if int(response_year) > 2025:
            print("Invalid input. Please try again")
            continue

        return response_year


def get_month():
    print("What month are you looking for?")
    while True:
        response_month =input("Month: ")
        if response_month.strip() == "":
            print("Invalid input. Please try again")
            print("Strip")
            continue

        if len(response_month) not in (1,2):
            print("Invalid input. Please try again")
            print("length")
            continue

        for i in response_month:
            if i.isdigit() == False:
                print("Invalid input. Please try again")
                print("digit")
                continue               
        if int(response_month) > 12:
            print("Invalid input. Please try again")
            print("Greater")
            continue
        if int(response_month) == 0:
            print("Invalid input. Please try again")
            continue

        else:
            return response_month
        
def get_day():
    print("What day are you looking for?")
    while True:
        response_day =input("Day: ")
        if response_day.strip() == "":
            print("Invalid input. Please try again")
            continue

        
        for i in response_day:
            if i.isdigit() == False:
                print("Invalid input. Please try again")
                print("digit")
                continue               

        if int(response_day) > 31:
            print("Invalid input. Please try again")
            continue

        if int(response_day) < 1:
            print("Invalid input. Please try again")
            continue


        else:
            return response_day



def get_date():
    historical_date = get_year()+"-"+get_day()+"-"+get_month()
    return historical_date


def ask_date():
    print(" are you looking for a specific date?")
    while True:
        date_response = input("Yes or No: ")

        if date_response in ["Yes", "YES", "yes", "yEs", "yeS", "YEs", "yES", "YeS"]:
            historical_date_query = get_date()
            print(historical_date_query)
            return historical_date_query

        if date_response in ["No","no","NO","nO"]:
            return None
            
        else:
            print("Invalid input. Please respond with Yes or No")






def get_data():

    try:
        os.mkdir("results")
    
    except:
        pass

    api_key = "fe20495282cee3be06f5caeb0a08c173"
    url = f"https://api.weatherstack.com/current?access_key={api_key}"
    city=get_city()
    date=ask_date()
    if date == None:
        params_values = {"query":city, "units":"f", "hourly":"1", "interval":"1"}
        response = requests.get(url, params=params_values)
        json_data = response.json()
    
    if date != None:
        params_values = {"query":city, "units":"f","historical_date":date}
        response = requests.get(url, params=params_values)
        json_data = response.json()
        
    
    


    print("What would you like to name your file?")
    while True:
        filename = input("File name: ")
        filename_valid = True
        if filename.strip() == "":
            print("Invalid filename, please try an other")
            continue
        for i in filename:
            if i not in ascii_letters:
                print("Invalid filename, please try an other.")
                filename_valid = False
                break
        if filename_valid == True:
            break
        
    print(url, params_values)
    
    with open(f"./results/{filename}.json", "w") as file:
        file.write(f"{json_data}")

    with open(f"./results/{filename}.json", "r") as read_file:
        contents = read_file.read()
        contents = contents.replace("\'","\"")

    with open(f"./results/{filename}.json", "w") as file:
        file.write(f"{contents}")

    

        
    print(f"Data successfully transfered to {file.name}. ")


def plot_temp():
    file_list = os.listdir("./results")
    print("What file do you wish to graph? ")
    while True:
        file_response = input("Filename: ")
        file_response_json = f"{file_response}.json"
        if file_response_json not in file_list:
            print("File not found. Please try again.")
            continue

        elif file_response_json in file_list:
            print(f"Plotting temperature from file: {file_response_json}")
            break

        else:
            print("Invalid input, please try again.")
            continue
        

    with open(f"./results/{file_response_json}", "r") as file:
        json_data = json.load(file)

        temp = json_data["current"]["temperature"]
        unit = json_data["request"]["unit"]
        city = json_data["location"]["name"]


    plt.bar([1],temp, color = "blue")
    plt.grid(True)
    plt.title(f"Temperature in {city}")
    print(1)
    plt.xticks([1])
    print(2)
    plt.yticks(np.arange(0,120,5))
    plt.xlim(0,2)
    plt.ylim(0,120)
    plt.xlabel("Today")
    plt.ylabel(f"Temperature in {unit}* ")
    plt.show()



print("Main menu.\n Please choose from list of options:\n1: Generate new query.\n2: Graph data.\n3. Quit")
while True:
    
    response = input("Option:")

    if response == "1":
        get_data()

    elif response == "2":
        plot_temp()

    elif response == "3":
        print("Closing Menu.")
        sys.exit()
        break

    else:
        print("Invalid option. Please try again.")
        continue
    n = input("Press enter to continue: ")
    print("Main menu.\n Please choose from list of options:\n1: Read data.\n2: Graph data.\n3. Quit")