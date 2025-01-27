import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# функция и её производные
def f(x):
    return np.sin(x) * np.cos(x**2 + 5)

def f_prime(x):
    return np.cos(x) * np.cos(x**2 + 5) - 2*x * np.sin(x) * np.sin(x**2 + 5)

def f_double_prime(x):
    return -np.sin(x) * np.cos(x**2 + 5) - 2 * (np.cos(x) * np.sin(x**2 + 5) + 2 * x * np.cos(x) * np.cos(x**2 + 5))

# отрезок
a = 0
b = 5
x_values = np.linspace(a, b, 400)
y_values = f(x_values)

# 1. График функции и её производные
plt.figure(figsize=(15, 10))

# График функции
plt.subplot(2, 2, 1)
plt.plot(x_values, y_values, label='f(x)', color='r')
plt.title('График функции f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# График первой производной
plt.subplot(2, 2, 2)
plt.plot(x_values, f_prime(x_values), label="f'(x)", color='g')
plt.title('График первой производной f\'(x)')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.grid(True)
plt.legend()

# График второй производной
plt.subplot(2, 2, 3)
plt.plot(x_values, f_double_prime(x_values), label="f''(x)", color='b')
plt.title('График второй производной f\'\'(x)')
plt.xlabel('x')
plt.ylabel('f\'\'(x)')
plt.grid(True)
plt.legend()

# 2. Найти наибольшее и наименьшее значение функции на отрезке
y_min = f(a)
y_max = f(a)
min_point = a
max_point = a

for x in np.linspace(a, b, 100):
    y = f(x)
    if y < y_min:
        y_min = y
        min_point = x
    if y > y_max:
        y_max = y
        max_point = x

# Отобразим на графике 1 наименьшее и наибольшее значения
plt.subplot(2, 2, 1)
plt.plot(min_point, y_min, 'o', color='b', label='min')
plt.plot(max_point, y_max, 'o', color='m', label='max')
plt.legend()

# 3. Уравнение касательной и нормали
x_tangent = 1  #касательная в точке х= 1
y_tangent = f(x_tangent)
slope = f_prime(x_tangent)

# Уравнение касательной
def tangent_line(x):
    return slope * (x - x_tangent) + y_tangent
# Уравнение нормали
def normal_line(x):
    return -1/slope * (x - x_tangent) + y_tangent

# касательная и нормаль на графике 1
plt.subplot(2, 2, 1)
plt.plot(x_values, tangent_line(x_values), color='orange', label='Касательная')
plt.plot(x_values, normal_line(x_values), color='purple', label='Нормаль')
plt.legend()

# 4. Построение касательных расслоений
plt.subplot(2, 2, 4)
plt.plot(x_values, y_values, label='f(x)', color='r')
plt.title('Касательное расслоение')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

points = [0,1,2,3,4,5]
x_tangent = np.linspace(0, 5, 400)
for x0 in points:
    y0 = f(x0)
    slope = f_prime(x0)
    tangent_line = slope * (x_tangent - x0) + y0
    plt.plot(x_tangent, tangent_line, label=f'Tangent at x={x0}', alpha=0.5)

# 5. Найти длину кривой через интеграл
def integrand(x):
    return np.sqrt(1 + (f_prime(x))**2)
length, _ = quad(integrand, a, b)
print(f'Длина кривой на отрезке [{a}, {b}] составляет: {length:.4f}')

plt.tight_layout()
plt.show()
