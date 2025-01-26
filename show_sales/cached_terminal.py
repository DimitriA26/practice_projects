ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
import sys

# add new data
def add_data():
    # get name
    def get_name():
        print("Enter your name. ")
        #check name status
        while True:
            name_valid = True
            name = input("Name: ")
            if name.strip() == "":
                print("Invalid. Please enter name.")
                continue
            
            for char in name:
                if char in ascii_letters:
                    continue
                else:
                    print("Invalid characters, please use only letters. ")
                    name_valid = False

            if name_valid == True:
                while True:
                    check_name = input(f"Name is {name}. Is this correct?\n")
                    if check_name in ["Yes", "YES", "yes", "yEs", "yeS", "YEs", "yES", "YeS"]:
                        print("Name confirmed. \n")
                        return name 
                        
                    elif check_name in ["No", "no", "NO", "nO"]:
                        print("Please re-enter Name. ")
                        break
                    else:
                        print("I don't understand. Please respond yes or no.")
                        continue
                
    #get_name()

     # get last name
    def get_salary():
        print("Please enter your salary. ")
        while True:
            check_salary = True
            salary = input("Salary: ")
            try: 
                int(salary)
                
            except:
                print("Invalid value. Please input your salary in numeric form. ")
                check_salary = False

            if check_salary == False:
                continue
                
            if check_salary == True:
                while True:
                    check_salary = input(f"Your salary is {salary}. Is this correct? \n")
                    if check_salary in ["Yes", "YES", "yes", "yEs", "yeS", "YEs", "yES", "YeS"]:
                        print("salary confirmed. \n")
                        if 0 < int(salary) <= 1000000:
                            return salary
                        else:
                            print ("Invalid salary, please input a value between 1 and 1000000 ")
                            check_salary = False
                            continue

                            
                    elif check_salary in ["No", "no", "NO", "nO"]:
                        print("Please re-enter salary. ")
                        break
                    else:
                        print("I don't understand. Please respond yes or no.")
                        continue

                if check_salary == False:
                    break
        
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
            print(f"Data successfully transfered to {file.name}. ")

        except Exception as e:
            print(f"Error: {e} ") 

       
    filename = "./data.csv"
    data = (get_name()+","+get_salary()+","+get_age()) 
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


filename = "./data.csv"

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




        
filename = "./data.csv"
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
    n = input("Press any key to continue: ")
    print("Main menu.\n Please choose from list of options:\n1: Read data.\n2: Add data.\n3: Remove data.\n4. Quit")