def quadratic_solve(a, b, c):
    D = b ** 2 - 4 * a * c
    if  D < 0:
        return 'Нет вещественных корней'
    elif D == 0:
        return -b/(2*a)
    else:
        return (-b - D**0.5)/(2*a), (-b + D**0.5)/(2*a)

# print(quadratic_solve(1,-4,-5))
L = list(map(float, input('Введите значения перменных a, b и c через пробел: ').split()))
print(quadratic_solve(*L))
