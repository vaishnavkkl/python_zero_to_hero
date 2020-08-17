# basics(variables)
price = 30
print(price)
rating = 7.0  # float
name = "vaishanv"  # string
is_true = False  # bool
name2 = input('What is your name')  # taking input from user and saves in variable name2
print('hi' + " " + name2)  # concatenation of string(eg a+b = ab)

# exercise 1
name = input('What is your name ')
color = input("What is your favourite color ")
print(name + " likes " + color)

# calculating age
birth = input('birth year : ')
print(type(birth))  # this prints what type of variable we have entered(for eg string,integer,bool)

age = 2020 - int(birth)
print(age)  # print your current age

# convertion of pounds into kg
weight = input("Enter your weight: ")
weight_inkg = float(weight) * .454  # 1 pound = .45kg
print(weight_inkg)

# Basic Strings manipulations

email = ''' hi everyone ,
hoe are you'''  # when strings are placed in btw triple quotes we can write strings line by line
another = email[:]
print(email)
print(email[1])
print(email[-1])
print(email[0:5])
print(another)  # run the above code and observe the string variations

first = 'vaishnav'
last = 'm'
print(f'hi {first} . {last}')  # formatted string
print(first.upper())  # convertion of string to uppper case
k = len(first)  # using len function we can find length of a string
print(k)
print(first.find('av'))  # find index of the given keyword
print(first.replace('a', 'A'))  # replace the letter a with A(first is a variable that store the string)
print(
    'vaishnav' in first)  # check for the given string is given in the variable
# ( is a bool function means returns true or false)

# arithmetic operations
import math  # math library

math.acosh(4)  # cosine method
print(2 / 3)  # give float
print(2 // 3)  # give integer
print(3 % 2)  # gives reminder
print(3 ** 2)  # power
# x = x+3 is same as x+=3
x = 5.4
print(round(x))  # round to nearest integer

# if statements
price = 1000000
good_credit = False
if good_credit:  # check good_credit true or false
    print(price * 0.1)
else:
    print(price * .2)

# elif statements (for 2 or more conditions)
temparature = input("enter the temparature of this location: ")
if int(temparature) > 30:
    print('its hotter today')
elif int(temparature) < 10:
    print('its colder today')
else:
    print('neither cold nor hot')

# checking length of a string and checking for good strings
name = len('nv')
if name < 3:
    print('bad')
elif name > 30:
    print('so bad ')
else:
    print('good')

# convertion of weight according to input kg or pounds
weight = input('enter your weight: ')
converter = input('(L)bs or (k)g: ')
if converter == 'L' or converter == 'l':
    print(int(weight) * .45)
elif converter == 'K' or converter == 'k':
    print(int(weight) * 2)
else:
    print('invalid input')

# while loop

i = -1
while i < 10:
    print(i)
    i += 1
# a guess game using while
guess = 9  # set the answer no as 9
count = 0  # count starts from 0
count_limit = 3  # count limit as 3 (for 3 chances)
while count < count_limit:  # limit exeeds count_limit while stops
    gos = input('Guess; ')  # variable to store guessed no
    count += 1  # increase count
    if int(gos) == 9:  # if input equals the answer
        print('won')
        break  # stops if ans is correct
else:
    print('you loss')

# a basic game refer it in mosh python video for better understanding
command = ''
startcount = 1
stopcount = 1
while True:
    command = input('>').lower()
    if command == 'start':
        while startcount < 2:
            print('ready to go')
            startcount += 1
            break
        else:
            print('already started')
    elif command == 'stop':
        while stopcount < 2:
            print('stop the car')
            stopcount += 1
            break
        else:
            print('already stopped')
    elif command == 'help':
        print('''
        start - strts the car
        stop - stops the car
        quit - exit the car  ''')
    elif command == 'quit':
        break

# for loops
total = 0  # intialize total and set to 0
for item in range(0, 10):  # item is variable in for loop in which first loop
    # item will be 1 ,second loop items will be 2 and so on
    total += item
print(total)

# nested for looop
for countx in range(0, 5):  # run these code for basic understanding of nested for loop
    for county in range(0, 2):
        print(countx, county)

# print x in form of given list values
numbers = [5, 2, 5, 2, 2]
for items in numbers:
    print(items * 'x')
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
        print(output)

# lists
names = ['john', 'bob']

names[0] = 'jon'  # changing john to jon
print(names)

# finding largest number in a list
lists = [4, 3, 4, 5, 6, 7, 8, 9]
max = lists[0]  # setting the first number as max
for number in lists:  # for loop to traverse the whole list
    if max > number:  # checking the max
        max = number  #
print(number)

# 2dimensnional lists

matrix = [
    [1, 2, 3],
    [3, 4, 5],
    [6, 7, 9]
]
print(matrix[0][2])
for row in matrix:
    for items in row:
        print(items)

# program to copy all elements from one list to another list(important)
numbers = [2, 3, 5, 2, 1]
numbers2 = []
for number in numbers:
    if number not in numbers2:
        numbers2.append(number)
print(numbers2)

# tuple
cordinates = (1, 2, 3)
x, y, z = cordinates
print(x, y, z)

# dictionaries
customer = {
    "name": "vaishnav",
    "age": 21,
    "bool": True
}
print(customer["name"])  # print string corresponding to name
print(customer.get(
    "name"))  # same as above line but if we try to acces a element
# which is not present in dictionary get method doesnt show error o
print(customer.get("birth", "march"))  # adding default value to the dictionary(default value added is march)

# integer to String Converter
phone = input('phone: ')  # takes the phone number from user
numbers = {  # creating dictionary
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five"
}
output = ''  # initializing output
for ch in phone:
    output += numbers.get(ch, '!')  # takes coresponding value for integer and saves to output
print(output)

# split = split with a condition given in it produces a list with that condition
names = 'vaishnav, sanjay, irshad, shabeeb'
print(names)
splitting = names.split(',')
print(splitting)
joined = ','.join(splitting)
print(joined)  # run these codes to get basic understanding of split function


# functions
def welcome_user():
    print('everyone')


print('hi')
welcome_user()


# basic function sample taking 1 argument
def welcome(name):
    print(f'hi {name}')


welcome('vaishnav')


# function taking 2 arguments
def welcome1(first_name, last_name):
    print(f'hi {first_name} {last_name}')


name = input('enter your name')
welcome1(first_name=name, last_name='m')


# function to find square of a number
def square(number):
    sq = number * number  # when we create a function return value must be given
    return sq


number = input('enter the number')  # taking input number
print(square(int(number)))  # pass the input to function by converting to string

# exceptions
try:
    age = int(input('enter your age '))
    print(age)
except ValueError:
    print('invalid input')  # the use of try and except is if we enter invalid input the terminal doesnt show error
    # instead it outputs the message given in except method


#  Basic class

class Points:
    def write(self):
        print('writting')

    def draw(self):
        print('drawing')


doing = Points()
doing.draw()


#  Class with constructors

class Person:
    def __init__(self, name):  # defining constructor always use __init__
        self.x = name

    def talk(self):
        print(f'the person {self.x}is talking')


person = Person('vaishnav')
print(person.talk())
print(person.x)

# inheritance

# class Mamal:
#     def walk(self):
#         print("walking")


# class Dog(Mamal):
#     pass
#
#
# class Cat:
#     def walk(self):
#         print('walking')
#
#
# jimmy = Dog()
# jimmy.walk()


# finding  greatest number in a list using function
numbers = [0, 2, 5, 4, 9]


def greatest(numbers):
    max = numbers[0]
    for items in numbers:
        if items > max:
            max = items
    return max


print(greatest(numbers))

import random  # importing random method

members = ['vaishnav', 'sanjay', 'nivedh']
leader = random.choice(members)
print(leader)  # run these codes to get basic idea

# another random example
import random


class Dice:
    def roll(self):
        dice1 = (1, 2, 3, 4, 5, 6)
        x = random.choice(dice1)
        y = random.choice(dice1)
        print(f'({x},{y})')


dice = Dice()
print(dice.roll())

# program to find the given number is prime or not
number = input('enter the number')
count = 0
for numbers in range(1, 10):
    modulo = int(number) % numbers
    if modulo == 0:
        count += 1
if count > 2:
    print('not prime')
else:
    print('prime number')

# program to check weather the given input is vowels or not

char = input('enter the character')
vowels = ('a', 'e', 'i', 'o', 'u')
for items in vowels:
    if char == items:
        print('vowel')
    else:
        print('not vowels')

#
# factorial of a given number
number = input('enter the number')
fact = 1
for count in range(1, int(number) + 1):
    fact = fact * count
print(fact)


# more about class
class Computer1:

    def __init__(self, name):
        self.x = name

    def spec1(self):
        print(self.x)


name = input('enter the specs')

cla = Computer1(name)
cla.spec1()


# another class example
class Computer:

    def __init__(self):
        self.name = "vaishnav"
        self.age = 21

    def compare(self, x):
        if self.age == x.age:
            return True


c1 = Computer()
c1.age = 21
c2 = Computer()

if c1.compare(c2):
    print('they are same')


# class samples
class Car:
    wheels = 4  # class variables

    def __init__(self):
        self.mileage = 20
        self.com = 'bmw'


Car.wheels = 5  # changing class variables

c1 = Car()
c2 = Car()
print(c1.mileage, c2.com)  # these are instance variables


#
class Student:
    school = 'barton '

    def __init__(self, m1, m2, m3):
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    def avg(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3

    def get_marks(self):
        return self.marks1

    @classmethod
    def information(cls):  # using class variables important
        return cls.school

    @staticmethod
    def college():
        print('college name')


s1 = Student(3, 4, 5)
s2 = Student(1, 3, 4)

print(s1.avg(), s2.avg())
print(s1.get_marks())
print(Student.information())
Student.college()  # for better understanding refer telusko pyhton tutorial about class


# class samples
class Person:
    def __init__(self, initialAge):
        if initialAge >= 0:
            self.age = initialAge
        else:
            self.age = 0
            print("Age is not Valid, setting age to 0")

        # Add some more code to run some checks on initialAge

    def amIOld(self):
        if self.age < 13:
            print("You are Young")
        elif self.age >= 13 and self.age < 18:
            print('you are teenager')
        else:
            print('you are old')
        # Do some computations in here and print out the correct statement to the console

    def yearPasses(self):
        self.age = self.age + 1
        # Increment the age of the person in here


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    #     p.amIOld()
    print("")

# seperate odd and even indexed letters in string
string_cases = int(input())  # taking how much strings user need to input
for i in range(string_cases):  # for loop to take n strings
    strings = input()
    even = ''  # intializing odd and even variables
    odd = ''
    for j in range(len(strings)):
        if j % 2 == 0:  # even indexed letters store in even
            even = even + strings[j]
        else:
            odd = odd + strings[j]  # odd indexed letters store in odd
    print(f'{even} {odd}')


# n = int(input())
# arr = list(map(int, input().rstrip().split()))
#
# reverse = []
# for i in range(n-1,-1,-1):
#     reverse.append(arr[i])
#
# output = ''
# for j in range(len(reverse)):
#     output+=str(reverse[j])+ ' '
# print(output)

# a = int(input())
# b = int(input())
# c = a/b
# print(round(c))
# print(float(c))


# leap year

def is_leap(year):
    leap = True
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return leap
            else:
                return not (leap)
        else:
            return leap
    else:
        return not (leap)


year = int(input())
print(is_leap(year))

n = int(input())
sum = ''
for i in range(1, n + 1):
    sum += str(i)
print(sum)

# dictionary sample
import sys

n = int(sys.stdin.readline().strip())
book = {}
for i in range(n):
    entry = sys.stdin.readline().strip().split()
    book[entry[0]] = entry[1]

query = input()
while query:
    no = book.get(query)
    print(str(query) + '=' + str(no))

else:
    print('Not Found')
query = input()

# factorial
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)

# convertion of decimal into binary

n = int(input())  # taking input from user
rem = ''  # initialize reminder
while n > 0:  # condition
    rem = str(n % 2) + rem  # store the reminder value in reverse order
    # (for storing correct order we actually use rem = rem + str(n%2)
    n = n // 2  # divide the input by 2 and store in n
print(rem)

# DATE TIME modules
import datetime  # importing

today = datetime.date.today()  # using datetime method saving todays date in variable 'today'
birthday = datetime.date(1999, 3, 22)  # saving the input date into birthday
print(today - birthday)  # calculation of current age
date = datetime.datetime.strptime('march 09, 2019', '%B %d, %Y')  # date format
print(date)


# inheritance

class A:  # super class
    def feature1(self):
        print('feature ones is working')

    def feature2(self):
        print('feature two is working')


class B(A):  # subclass
    def feature3(self):
        print('feature three is working')

    def feature4(self):
        print('feature four is working')


# ABSTRACT method

from abc import ABC, abstractmethod  # importing abstract library


class Computer(ABC):  # abstract classes cannot use objects
    @abstractmethod
    def process(self):
        print('runing')


class Laptop(Computer):
    def process(self):
        print('running')


com = Laptop()
com.process()

a = A()
b = B()
a.feature1()
b.feature3()

# hackerank day 13 solution
from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(): pass


# Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Price: {self.price}')


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
