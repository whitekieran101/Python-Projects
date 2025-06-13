
"""Understand:

Create a function that adds to a total instead of multiplying

inputs: both operands
output: total of operands multiplied

    PLAN:
1. collect inputs from user
2. create an empty list
3. create a for loop to append the value of num1 to the empty list, iterating the amount of times of num2
4. take the sum of the list

"""

def calculate_addition(num1, num2):
    """Finds the equivalent of multiplying a number through using ONLY addition"""

    working_list = []

    for i in range(num2):
        working_list.append(num1)

    final_number = sum(working_list)

    print(final_number)


def main():

    num1 = int(input('Enter your integer: '))
    num2 = int(input('Enter your multiplier: '))
    calculate_addition(num1, num2)




if __name__ == '__main__':
    main()


