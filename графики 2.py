import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons
import ipywidgets as widgets
from IPython.display import display

def f(x):
    return np.sin(x) * np.cos(x ** 2 + 5)

x_values = np.linspace(0, 5, 100)
y_values = f(x_values)

initial_x = 0.0
show_tangent = False

fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.3)

# График функции
line, = ax.plot(x_values, y_values, label='f(x) = sin(x) * cos(x^2 + 5)', color='blue')
ax.set_title('График функции')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_xlim(0, 5)
ax.set_ylim(-1, 1)
ax.axhline(0, color='black', linewidth=0.5, ls='--')
ax.axvline(0, color='black', linewidth=0.5, ls='--')
ax.grid()
ax.legend()

# Слайдер для перемещения точки
slider_ax = plt.axes([0.1, 0.1, 0.75, 0.03])
slider = Slider(slider_ax, 'x', 0, 5, valinit=initial_x)

# Флажок для отображения касательной
check_ax = plt.axes([0.75, 0.15, 0.2, 0.1])
check = CheckButtons(check_ax, ['Показать'+'\n'+'касательную'], [show_tangent])

# Кнопка для сброса положения точки
button_ax = plt.axes([0.1, 0.2, 0.1, 0.05])
button = Button(button_ax, 'Сбросить')

# Радиокнопки для изменения цвета и стиля линии графика
#radio_ax = plt.axes([0.3, 0.2, 0.15, 0.1])
radio = widgets.RadioButtons(
    options=['blue', 'green', 'red'],
    description='Цвет линии:',
)


# Функция для обновления графика
def update(val):
    x = slider.val
    y = f(x)

    # Обновление точки на графике
    ax.scatter(x, y, color='red')

    # Если касательная включена, рисуем её
    if check.get_status()[0]:
        slope = np.cos(x) * np.cos(x ** 2 + 5) - np.sin(x) * (2 * x * np.sin(x ** 2 + 5))
        tangent_line = slope * (x_values - x) + y
        ax.plot(x_values, tangent_line, color='orange',alpha=0.5)
        ax.legend()

    plt.draw()


# Функция для сброса положения точки
def reset(event):
    slider.set_val(initial_x)

# Функция для изменения цвета линии графика
def change_color(change):
    line.set_color(change['new'])
    plt.draw()

slider.on_changed(update)
check.on_clicked(update)
button.on_clicked(reset)
radio.observe(change_color, names='value')

plt.show()
