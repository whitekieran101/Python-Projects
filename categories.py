""" UNDERSTAND:
Given the names and ages of two people, write a Python program to return if one, both,
or neither people are between 18 and 64 years old (inclusive).

inputs: name/ages of two people
outputs: return whether one (or), both (and), or neither (not) people are:

>= 18 years AND <= 64 years.

"""


def print_age_eligibility(first_name, first_age, second_name, second_age):
    """Determines whether one, both, or neither people are between 18 and
       64 years old (inclusive)."""

    if (first_age >= 18 and first_age <= 64) and (second_age >= 18 and second_age <= 64):
        return f'Both {first_name} and {second_name} are between 18 and 64.'

    elif (first_age >= 18 and first_age <= 64) or (second_age >= 18 and second_age <= 64):
        if first_age >= 18 and first_age <= 64:
            return f'{first_name} is between 18 and 64, but {second_name} is not.'
        elif second_age >= 18 and second_age <= 64:
            return f'{second_name} is between 18 and 64, but {first_name} is not.'

    else:
        return f'Neither {first_name} or {second_name} are between 18 and 64.'


def main():
    first_name = input("Please enter the name of the first person: ")
    first_age = int(input("Please enter the age of first person: "))
    second_name = input("Please enter the name of the second person: ")
    second_age = int(input("Please enter the age of second person: "))

    print(print_age_eligibility(first_name, first_age, second_name, second_age))


if __name__ == "__main__":
    main()

