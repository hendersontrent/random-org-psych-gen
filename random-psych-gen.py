#----------------------------------------------
# This script builds an application to generate
# a random organisational psychology-related
# title for a LinkedIn profile headline
#----------------------------------------------

#-----------------------------------------
# Author: Trent Henderson, 5 November 2020
#-----------------------------------------

import random

#------------------ DEFINE TERMS TO INCLUDE ----------

# Define a vector of first word options

first_words = ("Organisational", "Operational", "Workplace", "OCM", "Diversity",
"Org", "Behavioural", "Leadership", "Mental Health", "Wellbeing")

# Define a vector of second word options

second_words = ("Change", "Management", "Consulting", "Supervisory", "Advisory",
"Neuroscience", "Specialist", "Wellbeing", "Leadership")

# Define a vector of last word options

third_words = ("Psychologist")

#------------------ BUILD THE GENERATOR --------------

# Define a function that takes user-inputted number of words

def my_org_psych_headline(num_words):
    if (num_words < 1) or (num_words > 3):
        raise ValueError("Generator expects either 2 or 3 words to generate.")
    elif num_words == 2:
        # Randomly generate words
        my_first = random.choice(first_words)
        my_third = third_words
        # Join the generated words together
        my_title = (my_first + " " + my_third)
        print(my_title)
    else:
        # Randomly generate words
        my_first = random.choice(first_words)
        my_second = random.choice(second_words)
        my_third = third_words
        # Catch cases where first and second words are the same
        # and to avoid duplicitous terms of OCM/Change/Management
        if my_first == my_second:
            my_second = random.choice(second_words)
            # Join the generated words together
            my_title = (my_first + " " + my_second + " " + my_third)
        elif my_first == "OCM" and my_second == "Change":
            my_second = random.choice(second_words)
            # Join the generated words together
            my_title = (my_first + " " + my_second + " " + my_third)
        elif my_first == "OCM" and my_second == "Management":
            my_second = random.choice(second_words)
            # Join the generated words together
            my_title = (my_first + " " + my_second + " " + my_third)
        else:
            # Join the generated words together
            my_title = (my_first + " " + my_second + " " + my_third)
        print(my_title)

#------------------ RUN THE GENERATOR ----------------

my_org_psych_headline(num_words = int(input("Enter either 2 or 3 words to generate: ")))
