

# Below are the paired ratings for Red Lobster and Jake's Seafood Restaurant for 10 respondents for each 
# of three different restaurant features.
# The 7-point ratings were obtained on a questionnaire that instructed respondents to rate each 
# restaurant from low (1) to high (7) prices, slow (1) to fast (7) service, and wide (1) to limited (7) menu.

#  a.Input these responses into an SPSS for Windows dataset (File-New-Data) and save the file for future 
# use; make sure anddefine an ID number for each respondent (1-10). b.In the variable view window, 
# provide the following for each of the six variables (prices, service, menu for each restaurant):

#  i.Variable name:Should be able to uniquely identify individual variable in data view ii.Variable 
# label:Should describe in detail the variable in variable view iii.Values(e.g., 1): Ensure labeled values are 
# entered for each variableas specified iv.Value labels(e.g., slow).:

# Make sure to use the value labels as specifiedfor each variable c.NOTE:Values & value labels will be the 
# same for each restaurant but different for each variable d.NOTE:Use the same variable names provided
#  in the example below. e.Include a screenshot of the data view and variable view windows of the data
#  editor in your assignment submission.

import csv
import random

# Define the number of respondents
num_respondents = 10

# Generate random ratings for each respondent and feature
data = []
for i in range(num_respondents):
    respondent_id = i + 1
    red_prices = random.randint(1, 7)
    red_service = random.randint(1, 7)
    red_menu = random.randint(1, 7)
    jake_prices = random.randint(1, 7)
    jake_service = random.randint(1, 7)
    jake_menu = random.randint(1, 7)
    data.append([respondent_id, red_prices, red_service, red_menu, jake_prices, jake_service, jake_menu])

# Save the data to a CSV file
output_file_path = 'C:/Users/user/Downloads/spssLab/restaurant_ratings2.csv'
with open(output_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Respondent', 'Red_Lobster_Prices', 'Red_Lobster_Service', 'Red_Lobster_Menu',
                     'Jake_Seafod_Prices', 'Jake_Seafod_Service', 'Jake_Seafod_Menu'])
    for row in data:
        writer.writerow(row)

print(f"Data has been saved to: {output_file_path}")

