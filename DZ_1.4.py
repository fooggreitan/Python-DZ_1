# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input("Ведите номер четверди: ")) 

if num == 1: print("x > 0 и y > 0")
elif num == 2: print("x < 0 и y > 0")
elif num == 3: print("x < 0 и y < 0")
elif num == 4:  print("x > 0 и y < 0")

else: print("Ошибка вывода")

