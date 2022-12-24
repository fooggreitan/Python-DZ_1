# 2. Напишите программу для проверки истинности утверждения F1 = ¬(X ⋁ Y ⋁ Z), F2 = ¬X ⋀ ¬Y ⋀ ¬Z, F1 = F2 для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x or  y or z) == (not x and not y and not z): print('Истино')
            else: print('Ложь')
            

