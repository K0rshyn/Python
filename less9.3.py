n = input("Введите последовательность чисел через пробел: ")
x = map(int, n.split())
seq = set()
for i in x:
    if i in seq:
        print(f"{i} - YES")
    else:
        print(f"{i} - NO")
        seq.add(i)
        