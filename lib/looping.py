#!/usr/bin/env python3

def happy_new_year():
    for i in range(10):
        print(10 - i)
        if i == 9:
            print("Happy New Year!")

def square_integers(int_list):
    return [i*i for i in int_list]

def fizzbuzz():
    for i in range(100):
        if (i+1) % 3 == 0 and (i+1) % 5 == 0:
            print("FizzBuzz")
        elif (i+1) % 3 == 0:
            print("Fizz")
        elif (i+1) % 5 == 0:
            print("Buzz")
        else:
            print(i+1)
