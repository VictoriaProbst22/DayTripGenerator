
#########--- AS OF 5/5 
# *Find the ability to randomly Re-Select any of the strings
# *Make Confirmatin Prompt and Display Entirity in console to confirm
# * Final GoodBye Prompt


#welcome message string to welcome users/start the game. 

welcome_message = ' Welcome to The Mystical Trip Agency, where we help you plan the most spectacular Day Trip!'
print(welcome_message)

import random
destinations_string = ['Inner Earth' , ' Glove World' , ' Atlantis' , ' Reptar World']

def destination_function():
    destination = random.choice(destinations_string)
    print(f' Here is your suprise destination, {destination}!')
    user_input = input('DO you like this? y/n ')
    if user_input == 'y':
        return destination
    elif user_input == 'n':
        destination_function()

print('Well, ')
destination_function()

    
second_prompt = 'Now that we have our Destination, Lets try their cuisine!'
print(second_prompt)
#
import random
restraunts_string = [' The Candy Bar' , ' Maclarens' , 'The Krusty Burger' , 'Chokey Chiken']

def restraunts_function():
    restraunts = random.choice(restraunts_string)
    print(f'Here is one of the restraunts in town, Intrested in {restraunts}?')
    user_input = input('Do you like this restraunt? y/n ')
    if user_input == 'y':
        return restraunts
    elif user_input == 'n':
        restraunts_function()

print('Well, ')
restraunts_function()
 
third_prompt = 'This All Sounds So Fantastic. How Would You Like To Get There?'
print(third_prompt)

import random
transportation_string = [ 'Bus' , ' Train ' , ' Hot Air Balloon' ,  ' Ferry']

def transportation_funtion():
    transportation = random.choice(transportation_string)
    print(f'Theres a Few Available Options for Transportation! Do You Like {transportation}?')
    user_input = input('Do you like this mode of travel? y/n ')
    if user_input == 'y':
        return transportation
    elif user_input == 'n':
        transportation_funtion()

print('Well ')
transportation_funtion()
 
fourth_prompt = 'Theres a Few Special Events Taking Place While Youre There!'
print(fourth_prompt)

import random
entertainment_string = [ ' The DimaDome' , 'Fair' ,  ' Posidens Island ' ,  ' Horse Ranch']
def entertainment_function():
    entertainment = random.choice(entertainment_string)
    print(f' {entertainment}?')
    user_input = input('Looking For Something Different? y/n ')
    if user_input == 'n':
        return entertainment
    elif user_input =='y':
        entertainment_function()

print('Hows ')
entertainment_function()

second_to_last_question = 'Can you please look over your plans and confirm?'
print(second_to_last_question)


import random
final_plan_list = [ '{destination} , {restraunts} , {transportation} , {entertainment}']

def final_confirmation_function():
    final_plan = random.choice(final_plan_list) 
    user_input = input("To Change Your Destination press 'a', Restruant press 'b', Travel Options press 'c' or Event press 'd' or 'n' to Skip!")
    if user_input == 'y':
        return final_plan
    elif user_input == 'a':
        destination_function()
    elif user_input == 'b':
        restraunts_function()
    elif user_input == 'c':
        transportation_funtion()
    elif user_input == 'd':
        entertainment_function()
    elif user_input == 'n':
        print('Great!')

print(random.choice(destinations_string))
print(random.choice(restraunts_string))
print(random.choice(transportation_string))
print(random.choice(entertainment_string))

confirm_message = 'Lookin Good?'
print(confirm_message)
final_confirmation_function()

after_confirmation_prompt = 'Awesome, Heres Your Planned Vacation Details!'
print(after_confirmation_prompt)

#print('List Of Strings')

closing_prompt = 'Thanks So Much For Using Our Services for Your Private Trip Needs. See Ya Next Time!'
print(closing_prompt)
