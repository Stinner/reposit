print("Введите первую точку")

x1 = float(input('X: '))

y1 = float(input('Y: '))

print("\nВведите вторую точку")

x2 = float(input('X: '))

y2 = float(input('Y: '))



x_diff = x1 - x2

y_diff = y1 - y2

k = x_diff / y_diff


b = y2 - k * x2



print("Уравнение прямой, проходящей через эту2 точки:")

print("y = ", k, " * x + ", b)