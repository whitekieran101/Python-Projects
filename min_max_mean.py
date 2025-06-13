"""
    UNDERSTAND:

Given a dataset, create an algorith to find the minimum, maximum, and mean.

inputs: the dataset
outputs: minimum, maximum, and mean.
match: reverse list

    PLAN:
1. import random
2. create an empty list and append a random number 0-100 one million times.
3. create an algorithm to return the local maximum, minimum, and mean.
    3.1 - maximum =  max(data_set)
    3.2 - minimum = min(data_set)
    3.3 - mean = sum(data_set) / len(data_set)
"""


import random, statistics

def access_data(data_set):
    """Accesses the minimum, maximum, mean, median, and sum of given dataset - assigns them to an easily callable index"""

    minimum = min(data_set)
    maximum = max(data_set)
    mean = sum(data_set) / len(data_set)
    median = statistics.median(data_set)
    total = sum(data_set)

    data_set.insert(0, minimum)
    data_set.insert(1, maximum)
    data_set.insert(2, mean)
    data_set.insert(3, median)
    data_set.insert(4, total)


def main():

    data_set = []

    for i in range(1000000 + 1):
        data_set.append(random.randint(0, 100))

    access_data(data_set)
    print(data_set[0])
    print(data_set[1])
    print(data_set[2])
    print(data_set[3])
    print(data_set[4])


if __name__ == '__main__':
    main()



"""
Name a data type you used in your code other than an int - list 
Write a statement you used in your code other than an assignment statement - if __name__ == '__main__':
Write an operator you used and respective operand(s) in your code - operator: +, operands: 1000000 + 1
Write a formal and an actual parameter you used in your function - formal: data_Set, informal:  data_set = [] for i in range(1000000 + 1): data_set.append(random.randint(0, 100))
Analyze the run time for access to each entity in your data structure for both the best case and worst case - WILL FINISH LATER

"""