
#########--- AS OF 5/5 
# *Find the ability to randomly Re-Select any of the strings
# *Make Confirmatin Prompt and Display Entirity in console to confirm
# * Final GoodBye Prompt


#welcome message string to welcome users/start the game. 

welcome_message = ' Welcome to The Mystical Trip Agency, where we help you plan the most spectacular Day Trip!'
print(welcome_message)


# Figure out how user is able to randomly select functions
#  random.choice(string_name)  (?)


first_prompt = 'Which Sight appeases your eyes?'
print(first_prompt)
# {insert Destinations String}
import random

destinations_string = ['Inner Earth' , ' Glove World' , ' Atlantis' , ' Reptar World']
destination = random.choice(destinations_string)
print(destination)

def determine_destination_approval(destinations_string):
    
#FIND THE ABILITY TO RESELECT RANDOM OPTINONS

#Second Prompt 
second_prompt = 'Now that we have our Destination, Lets try their cuisine!'
print(second_prompt)

import random
restraunts_string = [' The Candy Bar' , ' Maclarens' , 'The Krusty Burger' , 'Chokey Chiken']
restraunt = random.choice(restraunts_string)
print(restraunt)

#Third Prompt 
third_prompt = 'This All Sounds So Fantastic. How Would You Like To Get There?'
print(third_prompt)

import random
transportation_string = [ 'Bus' , ' Train ' , ' Hot Air Balloon' ,  ' Ferry']
transport = random.choice(transportation_string)
print(transport)

#fourth prompt pulls up 'Theres a few special events to choose from while your there! Which one seems like you would have the most fun?'
# {insert Entertain String}
fourth_prompt = 'Theres a Few Special Events Taking Place While Youre There! Which One Seems Like You Would Have The Most Fun?'
print(fourth_prompt)

import random
entertainment_string = [ ' The DimaDome' , 'Fair' ,  ' Posidens Island ' ,  ' Horse Ranch']
special_event = random.choice(entertainment_string)
print(special_event)
#  {Insert possibility to look over and confirm responses}

#Final Prompt (?)
# last_question = 'Can I start making Reservations? Or do you want change an event?'


##Maybe Insert Final Closing response?
#closing_prompt = 'Thanks So Much For Using Our Services for Your Private Trip Needs. See Ya Next Time!'
#print(closing_promt)
