"""
import random

name = input("what is your name?")
tables = {

    "table_1" : random.choice([True,False]),
    "table_2" : random.choice([True,False]),
    "table_3" : random.choice([True,False]),
    "table_4" : random.choice([True,False])

}

print(f"Welcome {name} where would you like to sit today")

for table, occupied in tables.items():
    
    status = "occupied" if occupied else "available"
    print(f"{table} is currently {status}.")    

"""

prices = {

    "tea" : 10,
    "coffe" : 10,
    "slice of cake" : 45

}


