""" UNDERSTAND:

use loops to manually reverse a list. Do not use splicing or reverse() function

input: list
output: reversed list
match: digit swap assignment

    PLAN:

1. take list1 from input
2. create list2 and leave it empty
3. initialize index at 0
4. create a for loop to iterate through list1
    4.1 reverse and append each item of the list1 to list2 by calling the index - 1
        and updating index -= (-1)
    4.2 return list2
"""



def flip_list(list1):
    """Reverses a list using a loop"""

    list2 = []
    index = 0

    for i in list1:
        list2.append(list1[index - 1])
        index += (-1)

    return list2


def main():


    list1 = ["cat", "dog", "mouse", "bunny"]

    print(flip_list(list1))



if __name__ == '__main__':
    main()

