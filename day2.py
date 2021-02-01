# numbers = [2,1,3,4]
# print(numbers)

# new_numbers= sorted(numbers)

# print(new_numbers)

# sorted_numbers = numbers.sort()

# numbers.sort()
# print(numbers)

# numbers = [2,1,3,4]
# print(numbers)

# mixed = ["bob",5,"apples",100]

# letters = ["A","B","D","E"]

# new_letters = letters.insert("C")

# print(new_letters)

# letters.sets

##sets are not ordered and containes duplicates

# list.append () -> adds to the end 
# set.append() -~> not possible because no end but can do set.add
 

# create a list of email adresss
# list contain duplicates 
# how cast the list to a set to remove duplicates

# listmail = ["lea@gmail.com","henri@gmail.com","laurent@gmail.com","lea@gmail.com"]

# newmail = set(listmail)

# print("without doublon", newmail)

# mylist = ["a","b","c","d","e"]

# new = mylist[::-3]

# print(new)

# TURPLE


# my_tuple = (5,6,7)

# print (my_tuple[0])

# daysoftheweek= ("lundi","mardi","mercredi")

# list_of_names = ["adam", "bob", "charlie", "dave"]

# for name in list_of_names:
#     if name == "bob":
#         print("robert")
#     else:
#         print(name)

# range(start,stop,step)

# for i in range(10,0,-1):
#     print(i)


# string slicing [start:stop:step]
# for loops = range(start,stop,step)

# num =  0 

# while num < 10: 
#     print(num)
#     num+= 1 

# my_fav_numbers = {14,26,5}

# mynewhobby = my_fav_numbers.add(2)

# print(mynewhobby)

# Create a set called my_fav_numbers with your favorites numbers.
# Add two new numbers to it.
# Remove the last one.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to our_fav_numbers.

# letters = ["l","a","b", "g", "k"]
# nums = [1,2,4,5,6,7,8,8]

# new = sorted(letters)
# print(new)
# print(letters)

# names[1] = "antho"

# print(names)

# names.append("leore")

# print(names)

# list1 = [5, 10, 15, 20, 25, 50, 20]

# list1.pop(0)

# print(list1)
# exercise 1

# my_fav_numbers = {14,12,4,26}
# print(my_fav_numbers)

# my_fav_numbers.add(12)
# my_fav_numbers.add(13)

# print(my_fav_numbers)

# my_fav_numbers.remove(26)
# print(my_fav_numbers)

# friend_var_numbers = {34,45,55}

# newone = friend_var_numbers | my_fav_numbers

# print(newone)


# exercise 2

# my_numbers = (5,6,7)

# #  tuple you can just print
# oktuple = ("coca", "sprite", "icetea")
# print(oktuple)

# exercise 3

# numbers = range (1,21)
# for number in numbers:
#     print(number)

# exercise 4


# floate= ["1,5" ,"2,5" ,"3,3" "5,4", "4.5" , "5" ]

# floate2 = int(floate)

# print(floate2)

# Exercise 5: Shopping List


# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# print(basket)

# basket.pop()

# print(basket)

# basket.extend(['kiwi'])
# print(basket)

# basket.insert(0,'Apples')
# print(basket)

# substring= "Apples"
# count = basket.count(substring)
# print("the count is:", count)

# exercise 6

# Write a while loop that will keep asking the user for input
#  until the input is the same as your name.

# name = print(input("your name"))
# for x in range(5):
#   if x == "lea": break
#   print("again")
# else:
#   print("Finally finished!")

# i = "your name"             DONT WORK
# while i != len("lea"):
#     print(i)
#     i += 1
# else :
#   print("congraaatt")

# EXERCISE 7 


# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

# for x in range(30):
#   if x == %3 : break
#   print(x)
# else:
#   print("Finally finished!")

movie_ticket = 0

familly= ["lea", "alec", "arry"]

for member in familly:
    age_familly = int(input("how hols is", member))


    if age <= 3 :
    movie_ticket = "lucky its free"
    elif age <= 12 :
    movie_ticket = 10
    elif age > 12 : 
    movie_ticket = 15


print(movie_ticket + member)