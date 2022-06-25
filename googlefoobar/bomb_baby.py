def solution(x, y):
    generation = 0
    mach, facula = int(x), int(y)

    while mach > 0 and facula > 0:
        if facula == 1 and mach == 1:
            return str(generation)

        if facula > mach:
            times_bigger = 1 if mach == 1 else facula//mach
            facula = facula - mach * times_bigger
            generation += times_bigger
        else:
            times_bigger = 1 if facula == 1 else mach//facula
            mach = mach - facula * times_bigger
            generation += times_bigger

    return "impossible"

def solution1(x, y):
    generation = 0
    mach, facula = int(x), int(y)
    bigger, smaller = max(mach, facula), min(mach, facula)

    while smaller > 0:
        generation += bigger//smaller
        bigger, smaller = smaller, bigger % smaller

    if bigger != 1:
        return "impossible"

    return str(generation - 1)


if __name__== '__main__':
    print(solution('10000', '10001'))
