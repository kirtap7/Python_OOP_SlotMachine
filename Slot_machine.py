#!/usr/bin/env python
# coding: utf-8
# Author: Patrick Malatesta
# Date: 5 Nov 2018

# First import the emoji and define the faces we are going to use

#importing emoji 
import emoji
#importing random choice selector
from random import choice
#these are the 3 faces we will use in our slot machine
faces = [emoji.emojize(':red_apple:'), emoji.emojize(':pear:'), emoji.emojize(':tangerine:')]


# define the class that will handle the concept of the purse to keep track of the credit

class Purse:
    #__init__ method where we assume a standard initial credit of 10
    def __init__(self, amt=10):
        self.balance = amt
    # debit method that will decrease the balance of the purse by a given amount
    def debit(self, d):
        self.balance -= d
    # credit method will increase the balance of the purse by a given amount
    def credit(self, c):
        self.balance += c
    # get_balance will print the current balance of the purse
    def get_balance(self):
        if self.balance >= 2:
            print('You have:', self.balance)
        else:
            #since the minimum ber is defined as 2. When the purse balance is < 2 the user won't be able to bet
            print('Thank you for playing.')
          
# define the class that creates and handles the columns of the slot

class Column:
    # we initialize each column as an empty string
    def __init__(self):
        self.column = ""
    # the change face method will give to each column a random face    
    def change_face(self):
        self.column = choice(faces)


# define the slot class that handles the slot and the columns

class Slot:
    
    #by default each slot has 3 columns
    def __init__(self): 
        self.c1 = Column()
        self.c2 = Column()
        self.c3 = Column()
    #the take_bet method asks the user to input a bet and checks if the input is valid
    def take_bet(self):
        self.bet = input('How much do you bet?: ')
        # 'N' is the key to exit the game
        # if the input is different that "N" we check if can be converted into an int
        if self.bet != "N": 
            try:
                #we want only integers numbers as float numbers bet are not allowed
                self.bet = int(self.bet)
            except:
                #if the input can not be cast into a number we print an error
                print("That's not a valid bet! Try again")
                #and we assume that the bet has value "Null"
                self.bet = "Null" 
        else:
            #if user enters "N" we exit the game
            print("You decided to leave the game. Goodbye!")
     
    # the pull_handle method chages randomly the faces of the columns
    def pull_handle(self):
        self.c1.change_face()
        self.c2.change_face()
        self.c3.change_face()
        
    # the show slot prints the columns of the slot 
    def show_slot(self):
        print('{} {} {}'.format(self.c1.column, self.c2.column, self.c3.column))

    # the score slot calculates the score based on the columns match
    def score_slot(self):
        #initialize variable score to 0
        self.score = 0
        # if all column are the same the score is bet*2
        if self.c1.column == self.c2.column and self.c2.column == self.c3.column:
            self.score = 2*self.bet
            #we don't want many decimals so we round the result using 2 decimal numbers
            round(self.score, 2) 
            print('You score', self.score, '- ', end ="")
        # if all column are different the score is 0
        elif self.c1.column != self.c2.column and self.c2.column != self.c3.column and self.c1.column !=self.c3.column:
            self.score = 0
            print('You score', self.score, '- ', end ="")
        # if 2 columns are the same the score is bet*1.5
        else:
            self.score = 1.5*self.bet
            round(self.score, 2)
            print('You score', self.score, '- ', end ="")
   
# create the function that will handle the tre classes and run the slot

def run_slot_machine():
    # classes instantiation
    slot = Slot()
    purse = Purse()

    print('==========  SLOT MACHINE  =========')
    print('Minimum bet is 2. Type "N" to exit.')
    purse.get_balance() #prints initial balance (10 by default)
    print()
    
    #prompt user for the first bet
    slot.take_bet()
    
    #create first loop when the balance is > 2 and the input is different than the exit letter "N"
    while purse.balance > 2 and slot.bet != "N":
        #if the bet is not valid ("Null" from Slot class, or empty string)
        if slot.bet == "Null" or slot.bet == "":
            #prompt the user for another bet
            slot.take_bet()
        else:
            #if the bet is valid we go in a loop until the balance is > 2
            while purse.balance > 2:
                #we check if the bet is < 2, if needed we print an error and ask for another bet
                if slot.bet < 2:
                    print('The minimum bet is 2! Try again')
                    slot.take_bet()
                #we check if the bet is > than current balance, if needed we print an error and ask for another bet
                elif slot.bet > purse.balance:
                    print("You don't have enough funds! Try again")
                    slot.take_bet()
                #if the bet is valid we action the slot
                else:
                    purse.debit(slot.bet) #we debit the purse of the bet just made
                    slot.pull_handle() #we pull the handle to change the faces
                    slot.show_slot() #print the faces
                    slot.score_slot() #calculate and print the score
                    purse.credit(slot.score) #we credit the purse with the score
                    purse.get_balance() #we print the balance
                    print()
                    #we ask for another bet if the balance is > 2 after the slot run
                    if purse.balance > 2:
                        slot.take_bet()
                # we use a break statement to exit temporarily the loop 
                # thus, for each bet we can check if it's valid, a number or the exit command
                break 
    #when the program terminates it print the final balance 
    print('You are leaving with', purse.balance)

run_slot_machine()





