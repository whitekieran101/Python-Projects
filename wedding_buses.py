import math

"""
UNDERSTAND:
Problem: Given the bride(s)/groom(s) names and number of guests, output the names of the
         couple, followed by how many buses are needed, and the number of extra people you
         could carry with those buses (empty seats)

MATCH:
MUNI assignment, digit swap assignment

PLAN:
1. input names
2. input number of guests
3. calculate buses_needed
4. calculate extra_people
5. output names of couple, buses_needed, extra_people in f-string format
6. respond to someone else for full credit
"""


def calculate_buses_needed(number_of_guests, bus_space):
    """Calculates how many buses are needed depending on the number of guests"""

    buses_needed = number_of_guests // bus_space


    extra_people_negative = number_of_guests % bus_space - bus_space
    extra_people = extra_people_negative * -1


    return f'The amount of buses needed to transport all guests is: {buses_needed} \nThe extra people you could take with the leftover room is: {extra_people}'





def main():
    couple_name_1 = input("Enter the first name: ")
    couple_name_2 = input("Enter the second name: ")
    number_of_guests = int(input("Enter number of guests: "))
    bus_space = 40

    print(f'The names of the couple are {couple_name_1} and {couple_name_2}.')
    print(calculate_buses_needed(number_of_guests, bus_space))



if __name__ == "__main__":
    main()