# KIERAN WHITE - CS110A - MUNI ASSIGNMENT

# CALCULATES AVERAGE MUNI RIDERSHIP GIVEN THE LINE, DAYS SURVEYED, AND RIDERS COUNTED

def calculate_average_daily_muni_riders():
   """Simulates a survey of Muni line attendance"""
   print("Welcome to the Muni Ridership Calculator")
   muni_line = input("Which Muni line did you survey? ")
   days_surveyed = int(input("How many days did you survey it? "))
   riders_counted = int(input("How many riders did you count? "))
   average_daily_riders = riders_counted // days_surveyed
   print(f'According to your survey, an average of {average_daily_riders:.1f} people rode the', muni_line)



def main():

    calculate_average_daily_muni_riders()



if __name__ == "__main__":
    main()

""" SAMPLE OUTPUTS:

#1 -  

Welcome to the Muni Ridership Calculator
Which Muni line did you survey? 31 Balboa
How many days did you survey it? 23
How many riders did you count? 1242
According to your survey, an average of 54.0 people rode the 31 Balboa

#2 - 

Welcome to the Muni Ridership Calculator
Which Muni line did you survey? 38R Geary
How many days did you survey it? 62
How many riders did you count? 9276
According to your survey, an average of 149.0 people rode the 38R Geary
"""