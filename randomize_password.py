""" UNDERSTAND:

Create a random 16-character password, 8 characters from CPU and 8 characters from user.
Need at least 1 number, punctuation mark, and letter, and characters may not repeat.


inputs: user_list, cpu_list
output: randomized 16-character password
match: population calculator

    PLAN:
1. create 3 lists to hold each type of character, a 4th for the user's input, and leave a 5th list empty for the final password.

        numbers = []
        letters = list(string.ascii_letters)
        punctuation = list(string.punctuation)
        password = []
        user_input = list(input('Enter an 8-character long phrase: '))

2. create a function to randomize 8 characters from the first 3 lists, and append this to the empty list

        for i in range(8):
            num = random.randint(1, 3)

            if num == 1:
                index = random.randint(0, len(numbers) - 1)
                password.append(numbers[index])
                numbers.pop(index)

            elif num == 2:
                index = random.randint(0, len(letters) - 1)
                password.append(letters[index])
                letters.pop(index)

            else:
                index = random.randint(0, len(punctuation) - 1)
                password.append(punctuation[index])
                punctuation.pop(index)


        return password

3. create a function to concatenate the user's input + randomized CPU list

        unmerged = user_input + randomize_character(numbers, letters, punctuation, password)
        merged = ''.join(unmerged)
        return merged

4. create a final loop to call this password 20 times

        for i in range(21):
"""

import string
import random


def randomize_character(numbers, letters, punctuation, password):
    """Chooses random characters, and adds them to a list to create the CPU generated half"""

    for i in range(8):
        num = random.randint(1, 3)

        if num == 1:
            index = random.randint(0, len(numbers) - 1)
            password.append(numbers[index])
            numbers.pop(index)

        elif num == 2:
            index = random.randint(0, len(letters) - 1)
            password.append(letters[index])
            letters.pop(index)

        else:
            index = random.randint(0, len(punctuation) - 1)
            password.append(punctuation[index])
            punctuation.pop(index)


    return password






def final_password(user_input, numbers, letters, punctuation, password):
    """Joins random characters list and user input list through concatenation"""
    unmerged = user_input + randomize_character(numbers, letters, punctuation, password)
    merged = ''.join(unmerged)
    return merged





def main():

    for i in range(21):
        numbers = []
        letters = list(string.ascii_letters)
        punctuation = list(string.punctuation)                                       #creates lists to sort different data
        password = []
        user_input = list(input('Enter an 8-character long phrase: '))

        for num in range(10):
            numbers.append(str(i))



        result = final_password(user_input, numbers, letters, punctuation, password)

        print(f'Your randomized password is: {result}')




if __name__ == '__main__':
    main()



""" SAMPLE OUTPUT:
 
Enter an 8-character long phrase: 1;bvja4'=
Your randomized password is: 1;bvja4'=(b00iVDI

Enter an 8-character long phrase: 63kvuahv
Your randomized password is: 63kvuahvm1*1>(bM

Enter an 8-character long phrase: 8t64dov42
Your randomized password is: 8t64dov42oF2_2["I

Enter an 8-character long phrase: dvohyvkj9
Your randomized password is: dvohyvkj93;)W}l3+

Enter an 8-character long phrase: frjf.bl3[
Your randomized password is: frjf.bl3[4A4}44f-

Enter an 8-character long phrase: iqndja-1
Your randomized password is: iqndja-1?[C{qL^"

Enter an 8-character long phrase: dnvje-qk
Your randomized password is: dnvje-qkBX`!6g6.

Enter an 8-character long phrase: vhangk2
Your randomized password is: vhangk2"+(7X:/7

Enter an 8-character long phrase: vjancvkci
Your randomized password is: vjancvkciJ]88=#h\

Enter an 8-character long phrase: sjvuanwng
Your randomized password is: sjvuanwng9%9t9pj&

Enter an 8-character long phrase: f7164912
Your randomized password is: f716491210hCt10`k%

Enter an 8-character long phrase: e0je381h
Your randomized password is: e0je381h`?+.aY1111

Enter an 8-character long phrase: vnalc;e]
Your randomized password is: vnalc;e]Q[1212b121212

Enter an 8-character long phrase: cvuyfigt
Your randomized password is: cvuyfigt131313$m13t13

Enter an 8-character long phrase: fjiec243
Your randomized password is: fjiec24314A1414pb}w

Enter an 8-character long phrase: 96iub83va
Your randomized password is: 96iub83va|1515$"(Zn

Enter an 8-character long phrase: 831ufkewk
Your randomized password is: 831ufkewkQ16c(q16r@

Enter an 8-character long phrase: 9vjwnd2s
Your randomized password is: 9vjwnd2s17@z}Lkve

Enter an 8-character long phrase: dhjcoanw
Your randomized password is: dhjcoanwm18$18#18_Q

Enter an 8-character long phrase: 2i2namfed
Your randomized password is: 2i2namfed19^191919f:19

Enter an 8-character long phrase: 185hfnas
Your randomized password is: 185hfnas202020!x20^h
"""