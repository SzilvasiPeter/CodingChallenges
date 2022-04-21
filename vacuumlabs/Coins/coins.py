import math


def who_win(n):
    positions = subtract_perfect_squares(n)
    return 'Pat' if positions[n] == 1 else 'Mat'


def subtract_perfect_squares(n):
    if n <= 0:
        return 1
    
    is_winning_case = []

    is_winning_case.append(1)
    is_winning_case.append(1)
    is_winning_case.append(0)

    for i in range(3, n+1):
        is_winning_case.append(0)
        for num in range(1, math.isqrt(i)+1):
            perfect_square = num * num
            if i - perfect_square == 0 or not is_winning_case[i - perfect_square]:
                is_winning_case[i] = 1
                break
            
    return is_winning_case


def generate_triangle(res):
    arr = []
    for i in range(1, len(res)):
        arr.append(res[i])

        if is_perfect_sqrt(i):
            print(str(arr).center(200))
            arr = []


def is_perfect_sqrt(n):
    sqrt = math.isqrt(n)

    return True if sqrt**2 == n else False


if __name__ == "__main__":
    substract_square_triangle = subtract_perfect_squares(1024)
    generate_triangle(substract_square_triangle)

    coins = []
    with open('test.in') as file:
        coins = list(map(int, file.read().splitlines()))

    for coin in coins:
        with open('test.out', 'a') as file:
            file.write(who_win(coin) + '\n')
        
    