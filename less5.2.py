word = (input("Введите слово: ")) 
a = word.count('a') 
e = word.count('e') 
i = word.count('i') 
o = word.count('o') 
u = word.count('u') 
if a == 0: 
    print("a = False") 
if e == 0: 
    print("e = False") 
if i == 0: 
    print("i = False") 
if o == 0: 
    print("o = False") 
if u == 0: 
    print("u = False") 
print(f"Гласных: {a + e + i + o + u}") 
print(f"Согласных: {len(word) - (a + e + i + o + u)}") 