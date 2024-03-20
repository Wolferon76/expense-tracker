#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#
import json


# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
expenses_file = open('expenses.json') # opening JSON file
expenses = json.load(expenses_file) # returns JSON object as a dictionary
expenses_file.close()


while True:
    command = input("\nChoose command:")
    if command == "1":

        name = input("the name of product: ")
        sum = int(input("The sum is: "))
        category = input("the name of category: ")
        expense = {"name": name, "sum": sum, "category": category}
        expenses.append(expense)
        print(expenses)
        with open("expenses.json", "w") as outfile:
            json.dump(expenses, outfile)
        pass
    if command == "2":
        def sort_sum(expense):
            return int(expense["sum"])
        expenses.sort(key = sort_sum, reverse = True)
        print(expenses[:11])
        pass
    if command == "3":
        def sort_sum(expense):
            return int(expense["sum"])
        expenses.sort(key = sort_sum, reverse = False)
        print(expenses[:11])
        pass
    if command == "e":
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass

