#Author: Madelyn Baldree
#Date: 6/11/2024
#Description: Convert pseudo code to python code

#1. convert user input to all caps and print
#get user input as a string
user_input = input("Enter a string: ")

#while loop to make sure user input is a string
while not isinstance(user_input, str):
    print("Invalid input. Please enter a string.")
    user_input = input("Enter a string: ")

#convert input to all caps and print results
print(user_input.upper())


#2. have the user gove two numbers and add the result
#get user input as integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#while loop to make sure user input is an integer
while not isinstance(num1, int) or not isinstance(num2, int):
    print("Invalid input. Please enter integers.")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

#add the two numbers and print the result
result = num1 + num2
print("The sum of the two numbers is:", result)


#3. get an unknown amount of numbers from the user and add them together
#declare local variables
option = 1
total = 0

#while loop to get and add numbers until user stops
while option != 0:
    num = int(input("Enter a number to add: "))

    #while loop to make sure user input is an integer
    while not isinstance(num, int):
        print("Invalid input. Please enter an integer.")
        num = int(input("Enter a number to add: "))

    #add number to total
    total += num
    #ask user if they want to exit
    option = int(input("Enter 1 to add another number or 0 to stop: "))

    #while loop to make sure input is either 1 or 0
    while option not in [0, 1]:
        print("Invalid input. Please enter 1 to add another number or 0 to stop.")
        option = int(input("Enter 1 to add another number or 0 to stop: "))

#print total
print("The total is:", total)


#4. pritn a random number between 0 and user defined maximum
#import random
import random

#declare local variables
option = 1

#while option is not 0
while option != 0:
    #get user input as an integer
    max_num = int(input("Enter the maximum number: "))

    #while loop to make sure user input is an integer
    while not isinstance(max_num, int):
        print("Invalid input. Enter an integer.")
        max_num = int(input("Enter the maximum number: "))

    #generate a random number between 0 and max_num
    random_num = random.randint(0, max_num)
    print("The random number is:", random_num)

    #ask user if they want to exit
    option = int(input("Enter 1 to play again or 0 to stop: "))

    #while loop to make sure input is either 1 or 0
    while option not in [0, 1]:
        print("Invalid input. Enter 1 to play again or 0 to stop.")
        option = int(input("Enter 1 to play again or 0 to stop: "))


#5. generate 10 random numbers and print "right" of the number is even and "left" if it is odd
#declare local variables
right = 0
left = 0

#for loop to generate 10 numbers and keep track of how many are right and left
for _ in range(10):
    num = random.randint(0, 100)
    if num % 2 == 0:
        print("right")
        right += 1

    else:
        print("left")
        left += 1

#print results
print("Total right: ", right)
print("Total left: ", left)