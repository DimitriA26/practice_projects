ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import sys

# add new data
def add_data():
    # get first name
    def get_first_name():
        print("Enter your first name. ")
        #check name status
        while True:
            first_name_valid = True
            first_name = input("First name: ")
            if first_name.strip() == "":
                print("Invalid. Please enter first name.")
                continue
            
            for char in first_name:
                if char in ascii_letters:
                    continue
                else:
                    print("Invalid characters, please use only letters. ")
                    first_name_valid = False

            if first_name_valid == True:
                while True:
                    check_first_name = input(f"First name is {first_name}. Is this correct?\n")
                    if check_first_name in ["Yes", "YES", "yes", "yEs", "yeS", "YEs", "yES", "YeS"]:
                        print("First name confirmed. \n")
                        return first_name 
                        
                    elif check_first_name in ["No", "no", "NO", "nO"]:
                        print("Please re-enter First name. ")
                        break
                    else:
                        print("I don't understand. Please respond yes or no.")
                        continue
                
    #get_first_name()

     # get last name
    def get_last_name():
        print("Enter your last name. ")
        #check name status
        while True:
            last_name_valid = True
            last_name = input("Last name: ")
            if last_name.strip() == "":
                print("Invalid. Please enter last name.")
                continue
            
            for char in last_name:
                if char in ascii_letters:
                    continue
                else:
                    print("Invalid characters, please use only letters. ")
                    last_name_valid = False

            if last_name_valid == True:
                while True:
                    check_last_name = input(f"Last name is {last_name}. Is this correct?\n")
                    if check_last_name in ["Yes", "YES", "yes", "yEs", "yeS", "YEs", "yES", "YeS"]:
                        print("Last name confirmed. \n")
                        return last_name
                        
                    elif check_last_name in ["No", "no", "NO", "nO"]:
                        print("Please re-enter Last name. ")
                        break
                    else:
                        print("I don't understand. Please respond yes or no.")
                        continue
        
    #get_last_name()

    def get_age():
        print("Please enter your age. ")
        while True:
            check_age = True
            age = input("Age: ")
            try: 
                int(age)
                
            except:
                print("Invalid value. Please input your age in numeric form. *Note that the age limit is 18+.* ")
                check_age = False

            if check_age == False:
                continue
                
            if check_age == True:
                while True:
                    check_age = input(f"Your age is {age}. Is this correct? \n")
                    if check_age in ["Yes", "YES", "yes", "yEs", "yeS", "YEs", "yES", "YeS"]:
                        print("Age confirmed. \n")
                        if 18 <= int(age) < 120:
                            return age
                        else:
                            print ("Invalid age, we apologize for the inconvenience. ")
                            check_age = False
                            sys.exit()

                            
                    elif check_age in ["No", "no", "NO", "nO"]:
                        print("Please re-enter age. ")
                        break
                    else:
                        print("I don't understand. Please respond yes or no.")
                        continue

                if check_age == False:
                    break      
    #get_age()


    
    def append_file(file, contents):
        try:
            with open(file, "a") as file:
                file.write(f"\n{contents}")
            print(f"Data successfully transfered to {file}. ")

        except Exception as e:
            print(f"Error: {e} ") 

       
    filename = "./data.txt"
    data = (get_first_name()+","+get_last_name()+","+get_age()) 
    append_file(filename, data)

            
#add_data()


def show_data(file):
    try:
        with open(filename, "r") as file:
            contents = file.readlines()
            for i in range(len(contents)):
                print(f"Line #{str(i+1)}: " + str(contents[i]))
    except Exception as e:
                print(f"Error: {e} ")


filename = "./data.txt"

#show_data(filename)


def get_linenumber(file):
    try:
        with open(file, "r") as file:
            contents = file.readlines()
            
    
    except Exception as e:
                print(f"Error: {e} ")

    while True:
        line_number = input("Enter line number you wish to remove.\n")
        for i in contents:
            try:
                if int(line_number) == contents.index(i)+1:
                    return line_number
                
                else:
                    continue
            except:
                continue
        print("Invalid line number. Please try again.\n")

    #row_list = str(range(len(contents)))

def delete_data(filepath, linenumber):
    # get data from file
    temp_list = []

    try:
        with open(filepath, "r") as file:
            contents = file.readlines()
            # move data into list without given row
            for i in contents:

                if contents.index(i) == int(linenumber)-1:
                    continue
                temp_list.append(i)
            #print(temp_list)
            
        #write list to file
        with open(filepath, "w") as file:
            for item in temp_list:
                file.write(str(item))
            # move data into list without given row
            

    except Exception as e:
                print(f"Error: {e} 1212")
    # with open(filename, "r") as file:
    #         contents = file.readlines()
    #         for i in range(len(contents)):with open(filename, "r") as file:
    #         contents = file.readlines()
    #         for i in range(len(contents)):
    #             #print(f"Line #{str(i+1)}: " + str(contents[i]))
    #             #print(f"Line #{str(i+1)}: " + str(contents[i]))
    print(f"Line {linenumber} successfuly removed. ")




        
filename = "./data.txt"
###get_linenumber(filename)
#delete_data(filename, get_linenumber(filename))



print("Main menu.\n Please choose from list of options:\n1: Read data.\n2: Add data.\n3: Remove data.\n4. Quit")
while True:
    response = input("Option:")

    if response == "1":
        show_data(filename)

    elif response == "2":
        add_data()

    elif response == "3":
        delete_data(filename, get_linenumber(filename))

    elif response == "4":
        print("Closing Menu.")
        sys.exit()
        break

    else:
        print("Invalid option. Please try again.")
        continue
