# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def func(x, y, z):
    print(f'при значении: x = {x}, y = {y}, z = {z}, выражение - {-(x*y*z) == -x+-y+-z}')

func(False, False, False)
func(False, False, True)
func(False, True, False)
func(False, True, True)

func(True, False, False)
func(True, False, True)
func(True, True, False)
func(True, True, True)

