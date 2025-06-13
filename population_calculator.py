 # KIERAN WHITE - CS110A - JACKALOPE POPULATION ASSIGNMENT

""" UNDERSTAND:
Calculate the final population given the initial population and number of generations.

input: initial population, number of generations 
output: final population total
restrictions: use for loop to calculate, use a while loop to iterate until told to stop, and round all numbers. 
match: previous looping assignments

    PLAN:
1. receive inputs from user
2. create a for loop to calculate the total population 
3. create a while loop to iterate until told not to
"""


def calc_populations(birth_rate, death_rate):
    """Creates a model to calculate the total population, based on initial population
       number of generations, and the birth/death rate."""
    starting_population = int(input('Starting population: '))
    generations = int(input('Number of generations: '))


    for gen in range(generations):
        starting_population += round(starting_population * birth_rate)
        starting_population -= round(starting_population * death_rate)
    print(f'Total population is: {starting_population}')

    repeat = input('Do you want to calculate another population? If yes enter "y", if no enter "n" - ')

    while repeat != 'n':
        starting_population = int(input('Starting population: '))
        generations = int(input('Number of generations: '))

        for gen in range(generations):
            starting_population += round(starting_population * birth_rate)
            starting_population -= round(starting_population * death_rate)
        print(f'Total population is: {starting_population}')
        repeat = input('Do you want to calculate another population? If yes enter "y", if no enter "n" - ')
    print('Calculation are finished.')


def main():

    birth_rate = 0.10           #read into main to generalize model
    death_rate = 0.02
    print(calc_populations(birth_rate, death_rate))




if __name__ == '__main__':
    main()


""" SAMPLE OUTPUTS:
#1 -

Starting population: 200
Number of generations: 1
Total population is: 216
Do you want to calculate another population? If yes enter "y", if no enter "n" - y
Starting population: 132
Number of generations: 2
Total population is: 153
Do you want to calculate another population? If yes enter "y", if no enter "n" - n
Calculation are finished.

#2 - 

Starting population: 100
Number of generations: 10
Total population is: 214
Do you want to calculate another population? If yes enter "y", if no enter "n" - y
Starting population: 30
Number of generations: 5
Total population is: 42
Do you want to calculate another population? If yes enter "y", if no enter "n" - y
Starting population: 10
Number of generations: 30
Total population is: 104
Do you want to calculate another population? If yes enter "y", if no enter "n" - n
Calculation are finished.

#3 -

Starting population: 2300
Number of generations: 7
Total population is: 3890
Do you want to calculate another population? If yes enter "y", if no enter "n" - y
Starting population: 3700
Number of generations: 10
Total population is: 7843
Do you want to calculate another population? If yes enter "y", if no enter "n" - n
Calculation are finished.
"""