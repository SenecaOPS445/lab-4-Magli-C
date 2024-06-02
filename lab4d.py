#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string):
    five = string[0:5]
    return five

def last_seven(string):
    seven = string[-7:]
    return seven

def middle_number(number):
    string_number = str(number)
    middle = string_number[1:3]
    return middle

def first_three_last_three(string1, string2):
    first_three = string1[0:3]
    last_three = string2[-3:]
    first_last = first_three + last_three
    return first_last

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))