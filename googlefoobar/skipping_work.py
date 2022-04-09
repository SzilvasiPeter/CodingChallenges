def solution_worker(x, y):
    additional_worker = set(x) - set(y)
    return additional_worker

def solution_salut(s):
    salut = 0
    print(s)
    for i, c in enumerate(s):
        print(c)
        if c == '>':
            for j in range(i, len(s)):
                if s[j] == '<':
                    salut += 1
                    
    return salut*2

if __name__ == '__main__':
    x = [13, 5, 6, 2, 5]
    y = [5, 2, 5, 13]

    additional_worker = solution_worker(x, y)
    print(additional_worker)

    s1 = ">----<"
    s2 = "<<>><"

    salut = solution_salut(s2)
    print(salut)