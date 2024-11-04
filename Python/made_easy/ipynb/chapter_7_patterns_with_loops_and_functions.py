# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---
"""Глава 7.

Рисунки из символов с помощью циклов и функций.
"""

# # Глава 7. Рисунки из символов с помощью циклов и функций
#
# ## 7.1. Рисунки с помощью символа * (звездочка)
#
# ### 7.1.1. Прямоугольный треугольник
#
# - Создание треугольника, где количество звездочек равно номеру строки
# - Использование вложенных циклов
# - Применение функций для повторного использования кода

# +
# 7.1.1. Прямоугольный треугольник


def pattern_t(height: int) -> None:
    """Создаёт прямоугольный треугольник из звездочек.

    Args:
        height: Количество строк для печати
    """
    for row_idx in range(height):
        print("* " * (row_idx + 1))


# Результат:
# *
# * *
# * * *
# * * * *
pattern_t(4)
# -

# ### 7.1.2. Перевернутый прямоугольный треугольник
#
# - Создание перевернутого треугольника
# - Управление отступами
# - Обратный порядок вывода

# +
# 7.1.2. Перевернутый прямоугольный треугольник


def pattern_t_inverse(height: int) -> None:
    """Создаёт перевернутый прямоугольный треугольник.

    Args:
        height: Количество строк для печати
    """
    indent_size = (height - 1) * 2
    for row_idx in range(height):
        stars = "* " * (row_idx + 1)
        print(" " * indent_size + stars)
        indent_size -= 2


# Результат:
#       *
#     * *
#   * * *
# * * * *
pattern_t_inverse(4)
# -

# ### 7.1.3. Равносторонний треугольник
#
# - Создание равностороннего треугольника
# - Расчет правильных отступов
# - Центрирование фигуры

# +
# 7.1.3. Равносторонний треугольник


def pattern_rt(height: int) -> None:
    """Создаёт равносторонний треугольник.

    Args:
        height: Количество строк для печати
    """
    indent_size = height - 1
    for row_idx in range(height):
        stars = "* " * (row_idx + 1)
        print(" " * indent_size + stars)
        indent_size -= 1


# Результат:
#    *
#   * *
#  * * *
# * * * *
pattern_rt(4)
# -

# ## 7.2. Рисунки с помощью цифр
# ### 7.2.1. Прямоугольный треугольник

# +
# 7.2.1. Треугольник из повторяющихся цифр


def numpattern1(height: int) -> None:
    """Создаёт треугольник из повторяющихся цифр.

    Args:
        height: Количество строк для печати
    """
    for row_num in range(1, height + 1):
        print(f"{row_num} " * row_num)


# Результат:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
numpattern1(4)
# -

# ### 7.2.2. Прямоугольный треугольник с последовательными числами

# +
# 7.2.2. Треугольник с последовательными числами


def numpattern2(height: int) -> None:
    """Создаёт треугольник с последовательными числами.

    Args:
        height: Количество строк для печати
    """
    for row_idx in range(1, height + 1):
        numbers = " ".join(str(num) for num in range(1, row_idx + 1))
        print(numbers)


# Результат:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
numpattern2(4)
# -

# ### 7.2.3. Треугольник с повторяющимися цифрами в обратном порядке

# +
# 7.2.3. Треугольник с повторяющимися цифрами в обратном порядке


def numpattern3(height: int) -> None:
    """Создаёт треугольник с повторяющимися цифрами в обратном порядке.

    Args:
        height: Количество строк для печати
    """
    current_num = 1
    for row_size in range(height, 0, -1):
        print(f"{current_num} " * row_size)
        current_num += 1


# Результат:
# 1 1 1 1
# 2 2 2
# 3 3
# 4
numpattern3(4)
# -

# ### 7.2.4. Треугольник из обратных чисел

# +
# 7.2.4. Треугольник из обратных чисел


def numpattern4(height: int) -> None:
    """Создаёт треугольник с убывающими числами в строках.

    Args:
        height: Количество строк для печати
    """
    for row_idx in range(1, height + 1):
        numbers = " ".join(str(num) for num in range(row_idx, 0, -1))
        print(numbers)


# Результат:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
numpattern4(4)
# -

# ### 7.2.5. Треугольник из квадратов обратных чисел

# +
# 7.2.5. Треугольник из квадратов обратных чисел


def numpattern5(height: int) -> None:
    """Создаёт треугольник из квадратов чисел в обратном порядке.

    Args:
        height: Количество строк для печати
    """
    for row_idx in range(1, height + 1):
        squares = " ".join(str(num**2) for num in range(row_idx, 0, -1))
        print(squares)


# Результат:
# 1
# 4 1
# 9 4 1
# 16 9 4 1
numpattern5(4)
# -

# ### 7.2.6. Ромб из чисел

# +
# 7.2.6. Ромб из чисел


def numpattern6(height: int) -> None:
    """Создаёт ромб из чисел.

    Args:
        height: Количество строк для печати
    """
    # Верхняя часть
    for row_num in range(1, height + 1):
        spaces = " " * (height - row_num)
        numbers = f"{row_num} " * row_num
        print(spaces + numbers)

    # Нижняя часть
    for row_num in range(height - 1, 0, -1):
        spaces = " " * (height - row_num)
        numbers = f"{row_num} " * row_num
        print(spaces + numbers)


# Результат:
#    1
#   2 2
#  3 3 3
# 4 4 4 4
#  3 3 3
#   2 2
#    1
numpattern6(4)
# -

# ## 7.3. Резюме
#
# - Научились создавать различные узоры с помощью циклов
# - Изучили работу с отступами для формирования фигур
# - Познакомились с функциями для повторного использования кода
# - Рассмотрели варианты узоров из символов и цифр
# - Научились создавать базовые геометрические фигуры
