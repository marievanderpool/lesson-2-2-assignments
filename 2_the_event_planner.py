# Objective:
# To practice the use of shorthand if statements in determining event-related decisions.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to help in event planning, but it has errors.
#  Identify and fix them.

attendees = int(input("Enter number of attendees: "))
venue = "large hall" or "conference room"

if attendees >= 100:
    venue == "large hall"
elif attendees <= 100:
     venue == 'conference room'
print("We have a great", venue, "for your party!")

# Task 2: Catering Choices
# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if 
# yes, otherwise recommend "Gourmet Meals Caterers" using an inline if else statement.

vegetarian_food = input("Do you want vegetarian food: yes or no?")
caterers= "Veggie Delight Caterers" or "Gourmet Meals Caterers"

if vegetarian_food == "yes":
     caterers == 'Veggie Delight Caterers'
elif vegetarian_food == 'no':
    caterers == 'Gourmet Meals Caterers'
print("We recommend", caterers, "for your event")