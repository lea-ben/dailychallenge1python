# answer = int(input("enter number : "))

# LOOP EXEMPLE 
# 
# for i in range (3):

#     guess = int(input("guess my number : "))
#     if guess == answer: 
#         print("correct")
#         break 
#     elif guess > answer :
#         print("too high")
#     else:
#         print("too low")

# DICTIONARY

# set = {"A","B","C"}

# person = {"name":"Jon" ,
#          "surname": "spiller",
#          "job":"teacher",
#          "pet_names": ["fluffy","jaws","robin"],
#          "work_experience" :{
#              "programmer" : "nedcore", 
#              "teacher": "Developers insitute",
#              "waiter": "burger king"
#          },
#          "parents": ("mom","dad"),
#          99:"red ballons",
#          ("A","B"): "The alphabet"
# }

# shopping_dict = {
#     0:"apples",
#     1:"oranges",
#     2:"bananas",
# },

# shopping_list = ["apples","oranges","bananas"],
# }

# # print(f"hello {person['name']} {person['surname']}")

# print(shopping_dict[0])

# sampleDict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# inventory = { 
#     "apples": 100, 
#     "oranges": 500,
#     "bananes": 200
# }


# print(inventory["oranges"] -= 1)

# print(inventory.get("bananes"))
# mykey = inventory.keys()
# print(mykey)
# myvalues = inventory.values()
# print(myvalues)
# myitems = inventory.items()
# myitems=list(myitems)
# print(myitems[1][1])
# # print(sampleDict["class"]["student"]["marks"]["history"])

# inventory = {
# 	"apples": 100,
# 	"oranges": 500,
# 	"bananas": 200
# }

# for name, number in inventory.items():
#     print(f"i have {number} of {name}")

# Loop through the dictionary and print:
# "I have <number> of <fruit>" for each line

# numbers = []
# for i in range (1,10000001):
#     numbers.append(i)

# print(numbers)

# Convert the two following lists, into dictionaries.
# Hint: Use the zip method


# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# phone_book = {
#     "a": {
#         "name1" : "adam",
#         "name2" : "alex",
#         "name3": "andrei",
#     },

        
#     "phone_number": 5039204920, 
    
# }

# print(phone_book["a"]["name1"])

# phone_book["email"]="lea@gmail.com"

# print(phone_book)

# phone_book["name"]="leo"
# print(phone_book)

# phone_book.pop("email")
# print(phone_book)

# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# zip_list = zip(keys,values)
# print(zip_list)

# for info in zip_list:
#     print(info)

# num_dict = {}

# for info in zip_list:
#     num_dict[info[0]] = info[1]

# print(num_dict) 

# dictionary =dict(zip(keys,values))
# print(dictionary)


brand = { "name": "Zara" ,
        "creation_date" : "1975",
        "creator_name": "Amancio Ortega Gaona",
        "type_of_clothes" : "men, women, children, home",
        "international_competitors": "Gap, H&M, Benetton ",
        "number_stores": "7000",
        "major_color" : "France -> blue, Spain -> red, US -> pink, green" ,
}
# Create a dictionary called brand, and translate the information above into keys and values.

# Change the number of stores to 2.

newvalue= brand['number_stores'] = '2'
print(newvalue)
print(brand)



# Print a sentence that explains who the clients of Zara are.

brand["new_sentence"] = "zara is good and cheap"
print(brand)
# Add a key called country_creation with a value of Spain to brand

brand["country_creation"] = "spain"
print(brand)


# If the key international_competitors is in the dictionary, add the store Desigual.

my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
}
x = "international_competitors"
while x     print("the" + x + "is" + y)

# Delete the information about the date of creation.
# Print the last international competitor.
# Print in a sentence, the major clothes’ colors in the US.
# Print the amount of key value pairs (length of the dictionary).
# Print only the keys of the dictionary.
# Create another dictionary called more_on_zara with the following information:
# creation_date: 1975 
# number_stores: 10 000 
# Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# Print the value of the key number_stores. What just happened ?