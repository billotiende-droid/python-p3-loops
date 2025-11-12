# !/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter >= 1:
        print(counter)
        counter -= 1
           
    print("Happy New Year!")    
         
    # code goes here!

    pass


def square_integers(int_list):
    squared_list = []

    for num in int_list:
        squared_list.append(num * num)

    return squared_list 

print(square_integers([1, 2, 3, 4, 5]))   
    
 # code goes here!

def fizzbuzz():
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:   # check if divisible by 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0 :       # check if divisible by 3
            print("Fizz") 
        elif i % 5 == 0 :       # check if divisible by 5
            print ("Buzz")
        else:
            print(i)       

fizzbuzz()

    # code goes here!
pass

# print(happy_new_year())