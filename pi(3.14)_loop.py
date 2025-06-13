""" UNDERSTAND:

input = n
output = pi's value

n = 5, 5th term = 4/(10 * 11 * 12) = 4/ (2n * (2n + 1) * (2n + 2))


    PLAN:

1. input n
2. initialize pi = 3
3. for numbers up to n:
        3.1 - If terms % 2 != 0:
                add 4/ (2 * terms * (2 * terms + 1) * (2 * terms + 2)) to pi
        3.2 - else:
                subtract 4/ (2 * terms * (2 * terms + 1) * (2 * terms + 2)) from pi
4. return pi
"""






def calculate_pi(n = 10):
    """Returns Pi's value based on the """
    pi = 3

    for i in range(1, n + 1):
        if i % 2 != 0:
            pi +=  4 /(2 * i * (2 * i + 1) * (2 * i + 2))
        else:
            pi -= 4/(2 * i * (2 * i + 1) * (2 * i + 2))
    return pi

def calculate_pi2(n = 10, decimal_points = 3):
    """Returns Pi's value based on the """
    pi = 3

    for i in range(1, n + 1):
        if i % 2 != 0:
            pi +=  4 /(2 * i * (2 * i + 1) * (2 * i + 2))
        else:
            pi -= 4/(2 * i * (2 * i + 1) * (2 * i + 2))
    return float(f'{pi:.{decimal_points}f}')



if __name__ == '__main__':
    print(calculate_pi(5))
    print(calculate_pi(20))
    print(calculate_pi())
    print(calculate_pi2())


