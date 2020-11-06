#----------------------------------------------
# This script builds an application to generate
# a random organisational psychology-related
# title for a LinkedIn profile headline
#----------------------------------------------

#-----------------------------------------
# Author: Trent Henderson, 6 November 2020
#-----------------------------------------

import random
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#------------------ DEFINE TERMS TO INCLUDE ----------

# Define a vector of first word options

first_words = ("Organisational", "Operational", "Workplace", "OCM", "Diversity",
"Org", "Behavioural", "Leadership", "Mental Health", "Wellbeing")

# Define a vector of second word options

second_words = ("Change", "Management", "Consulting", "Supervisory", "Advisory",
"Neuroscience", "Specialist", "Wellbeing", "Leadership", "Training")

# Define a vector of last word options

third_words = ("Psychologist")

#------------------ MAIN APPLICATION -----------------

# Instantiate the app

app = dash.Dash(__name__)
server = app.server
the_word_options = (2,3)

# Layout and components

app.layout = html.Div([
    # Title, text, and some styling

    html.H1('Org Psych LinkedIn Title Generator'),
    html.Hr(),
    html.P("This app generates a random LinkedIn title based off the types of wording used by graduates of organisational psychology programs. "),

    # Input option selector
    html.H4("Select the number of words in the title you want to generate:"),
    html.Div(dcc.RadioItems(id = 'word_selector', options = [{'label': i, 'value': i} for i in the_word_options],
                           value = 2)),

    # Output text that is generated

    html.Br(),
    html.Div(id = 'org_psych_title_output'),
    html.Br(),

    # Authorship

    html.Hr(),
    html.Div(dcc.Markdown("© [Trent Henderson](https://twitter.com/trentlikesstats). Code available on [GitHub](https://github.com/hendersontrent/random-org-psych-gen)."))
    ])

# Final app spec

@app.callback(
    Output('org_psych_title_output', 'children'),
    [Input('word_selector', 'value')]
)

#------------------ BUILD THE GENERATOR --------------

# Define a function that takes user-inputted number of words

def my_org_psych_headline(value):

    # Convert to integer

    value = int(value)

    if value == 2:
        # Randomly generate words
        my_first = random.choice(first_words)
        my_third = third_words
        # Join the generated words together
        my_title = (my_first + " " + my_third)
        return(my_title)
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
        return(my_title)

if __name__ == '__main__':
    app.run_server(debug = True, host = '127.0.0.1')
