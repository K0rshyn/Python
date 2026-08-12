def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)

def factorials(n):
    fact_n = fac(n)
    print(f"Факториал числа {n} равен: {fact_n}")
    factor = []
    for i in range(fact_n, 0, -1):
        factor.append(fac(i))
    return factor

num = int(input('Введите число: '))
res = factorials(num)
print(res)