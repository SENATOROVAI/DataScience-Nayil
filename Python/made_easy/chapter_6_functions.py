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
"""Глава 6.

Функции.
"""


# # 6. Функции
#
# ## 6.1. Определение функций
# - Именованный блок кода, который выполняется при вызове
# - Группа связанных операторов для определенной задачи
# - В Python функции являются объектами
# - Можно передавать данные через параметры
# - Может возвращать результат
#
# ## 6.2. Типы функций
# - Встроенные - уже определены в Python
# - Пользовательские - создаются программистом
#
# ## 6.3. Встроенные функции
# ### Полный список встроенных функций:
# ```python
# # Математические и числовые функции
# # abs()       divmod()    max()       min()       pow()       round()      sum()
# # complex()   float()     int()       hex()       oct()
#
# # Операции с последовательностями и коллекциями
# # dict()      list()      set()       tuple()     frozenset()
# # len()       range()     reversed()  sorted()    slice()     enumerate()
# # filter()    map()       next()      zip()       iter()
#
# # Проверки и преобразования типов
# # all()       any()       ascii()     bin()       bool()
# # isinstance() issubclass() type()     hash()      id()
#
# # Работа с атрибутами и объектами
# # getattr()   setattr()   delattr()   hasattr()
# # vars()      dir()       globals()   locals()
#
# # Строковые операции
# # chr()       ord()       str()       repr()      format()
#
# # Создание и управление объектами
# # object()    property()  staticmethod() classmethod()
# # super()     memoryview() bytearray()  bytes()    callable()
#
# # Ввод-вывод и системные функции
# # input()     print()     open()      help()      __import__()
# # breakpoint() compile()   eval()      exec()
# ```
#
# ### 6.3.1. Описание некоторых встроенных функций с примерами
#
# #### Математические операции:
# ```python
# # abs(x) - абсолютное значение
# abs(-5)  # 5
# abs(3.14)  # 3.14
#
# # round(number[, ndigits]) - округление
# round(3.14159, 2)  # 3.14
# round(3.5)  # 4
#
# # max(), min() - максимум/минимум
# max(1, 2, 3)  # 3
# min([1, 2, 3])  # 1
# ```
#
# #### Преобразование типов:
# ```python
# # int([x]) - в целое число
# int("123")  # 123
# int(3.14)  # 3
#
# # float([x]) - в число с плавающей точкой
# float("3.14")  # 3.14
# float(3)  # 3.0
#
# # str() - в строку
# str(123)  # "123"
# ```
#
# #### Проверки и идентификация:
# ```python
# # isinstance(object, classinfo) - проверка типа
# isinstance(5, int)  # True
# isinstance("hello", str)  # True
#
# # id(object) - идентификатор объекта
# x = [1, 2, 3]
# id(x)  # уникальный номер объекта
#
# # type(object) - тип объекта
# type(123)  # <class 'int'>
# type("hello")  # <class 'str'>
# ```
#
# #### Работа с последовательностями:
# ```python
# # len(s) - длина объекта
# len([1, 2, 3])  # 3
# len("Python")  # 6
#
# # sorted(iterable) - сортировка
# sorted([3, 1, 2])  # [1, 2, 3]
# sorted("python")  # ['h', 'n', 'o', 'p', 't', 'y']
# ```
#
# #### Кодировка и символы:
# ```python
# # chr(i) - символ по коду Unicode
# chr(97)  # 'a'
# chr(8364)  # '€'
#
# # ord(c) - код символа Unicode
# ord("a")  # 97
# ord("€")  # 8364
# ```
#
# #### Системные и вспомогательные:
# ```python
# # dir([object]) - список атрибутов
# dir(str)  # список методов строк
# dir()  # список локальных имён
#
# # help([object]) - справка
# help(print)  # документация по print()
#
# # any(iterable) - проверка на истинность
# any([True, False, False])  # True
# any([False, False, False])  # False
# ```
#
# #### Ввод-вывод:
# ```python
# # print(*objects, sep=' ', end='\n')
# print("Hello", "World", sep=", ")  # Hello, World
#
# # input([prompt]) - ввод пользователя
# name = input("Введите имя: ")  # запрос ввода
#
# # open(file) - работа с файлами
# f = open("text.txt", "r")  # открытие файла
# ```
#
# #### Функции высшего порядка:
# ```python
# # map(function, iterable)
# list(map(str, [1, 2, 3]))  # ['1', '2', '3']
#
# # filter(function, iterable)
# list(filter(bool, [0, 1, "", "hello"]))  # [1, "hello"]
# ```
#
# ## 6.4. Пользовательские функции
# ### 6.4.1. Зачем создавать функции?
# - Избежание повторного кода
# - Модульная структура программы
# - Упрощение разработки и понимания кода
#
# ### 6.4.2. Создание и вызов функций
# ```python
# # Определение функции
# def greeting():
#     print("Good Morning")
#
#
# # Вызов функции
# greeting()  # Good Morning
# ```
#
# ### 6.4.3. Входные параметры и аргументы
# #### 6.4.3.1. Параметры
# ```python
# def Lemonade_Stall(price):  # price - параметр
#     if price == 5:
#         print("Лимонад сделан из:")
#         print("Лимонный сок")
#         print("Вода")
#         print("Соль")
#         print("Сахар")
# ```
#
# #### 6.4.3.2. Аргументы
# ```python
# # 50 - это аргумент
# Lemonade_Stall(50)
# ```
#
# #### 6.4.3.3. Количество аргументов
# ```python
# def my_name(first_name, last_name):
#     print(first_name, last_name)
#
#
# my_name("Nilabh", "Nishchhal")  # Должно быть два аргумента
# ```
#
# ### 6.4.4. Возврат значений из функций
# ```python
# def fib(n):  # просто печатает значения
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         a, b = b, a + b
#     print()
#
#
# def fib2(n):  # возвращает список
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a + b
#     return result
# ```
#
# ## 6.5. Варианты передачи аргументов
# ### 6.5.1. Аргументы со значением по умолчанию
# ```python
# def my_address(city, state, country="India"):
#     print("I live in", city, ",", state, ",", country)
#
#
# my_address("Mumbai", "Maharashtra")  # country будет "India"
# my_address("Sydney", "New South Wales", "Australia")  # указали другую страну
# ```
#
# ### 6.5.2. Произвольное число аргументов (*args)
# ```python
# def fruit_basket(*fruit):
#     print(fruit)
#
#
# fruit_basket("apple", "grapes", "strawberry")
# # ('apple', 'grapes', 'strawberry')
# ```
#
# ### 6.5.3. Именованные аргументы
# ```python
# def parrot(volt, state="мертв", act="оживет", type="Норвежский голубой"):
#     print("- Этот попугай не", act, end=" ")
#     print("даже если пропустить", volt, "вольт через него.")
#     print("- Какое оперение!", type)
#     print("- Он", state, "!")
# ```
#
# ### 6.5.4. Произвольное число именованных аргументов (**kwargs)
# ```python
# def try_function(*args, **kwargs):
#     print("args:", args)
#     print("kwargs:", kwargs)
#
#
# try_function(
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     fourth="Thursday",
#     fifth="Friday",
#     weekend1="Saturday",
#     weekend2="Sunday",
# )
# ```
#
# ## 6.6. Генераторы
# ### 6.6.1. Определение генератора
# ```python
# def inclusive_range(*args):
#     numargs = len(args)
#     start = 0
#     step = 1
#
#     if numargs < 1:
#         raise TypeError("Expected at least one argument")
#     elif numargs == 1:
#         stop = args[0]
#     elif numargs == 2:
#         (start, stop) = args
#     elif numargs == 3:
#         (start, stop, step) = args
#     else:
#         raise TypeError("Expected at most 3 arguments")
#
#     i = start
#     while i <= stop:
#         yield i
#         i += step
# ```
#
# ### 6.6.2. Пояснение к примеру
# - Генератор создает последовательность
# - Поддерживает итерацию
# - Экономит память
# - Использует yield вместо return
#
# ## 6.7. Резюме
# - Функции - мощный инструмент структурирования кода
# - Позволяют избежать повторений
# - Делают код модульным и читаемым
# - Поддерживают разные способы передачи параметров
# - Генераторы предоставляют эффективный способ создания итераторов

# # 6.8. Упражнения
#
# ## 6.8.1. Вопросы и ответы
#
# **Вопрос 1: В чем различие между функцией и методом?**
# Функция - это самостоятельный блок кода, а метод - это функция, принадлежащая объекту или классу.
#
# **Вопрос 2: Как создание своих функций помогает программисту в работе?**
# - Избавляет от повторного написания кода
# - Делает программу модульной
# - Упрощает тестирование и отладку
# - Улучшает читаемость и понимание кода
#
# **Вопрос 3: Чем ограничено тело функции?**
# Тело функции ограничено отступами (отступ определяет блок кода, принадлежащий функции).
#
# **Вопрос 4: Можно ли использовать функцию, находящуюся внутри модуля, за пределами модуля?**
# Да, можно использовать через импорт модуля, если функция является доступной (не приватной).
#
# **Вопрос 5: В чем сходство и различие параметров и аргументов функции?**
# - Параметры - переменные в определении функции
# - Аргументы - значения при вызове функции
# - Сходство: связаны друг с другом при выполнении
#
# **Вопрос 6: Зачем в определении функции нужен оператор return? Что вернет функция, если в ее определении нет оператора return?**
# Return нужен для возврата значения из функции. Без return функция возвращает None.
#
# **Вопрос 7: Как обозначается произвольное количество аргументов? Когда они используются?**
# - *args - для произвольного количества позиционных аргументов
# - **kwargs - для произвольного количества именованных аргументов
# - Используются, когда количество аргументов заранее неизвестно
#
# **Вопрос 8: Что такое функция-генератор? Чем она отличается от обычных функций?**
# Функция-генератор:
# - Возвращает итератор
# - Использует yield вместо return
# - Сохраняет состояние между вызовами
#
# **Вопрос 9: В чем разница между args и kwargs? Что это такое?**
# - args - позиционные аргументы (собираются в кортеж)
# - kwargs - именованные аргументы (собираются в словарь)
#
# ## 6.8.2. Утверждения и их истинность
#
# **Утверждение 1: Чтобы вернуть значение из функции, нужно использовать оператор return.**
# Правда
#
# **Утверждение 2: Каждый оператор return в функции может возвращать свое значение.**
# Правда
#
# **Утверждение 3: Функция обязательно должна возвращать какое-то значение.**
# Ложь
#
# **Утверждение 4: Функция, которая не возвращает никакого значения, возвращает None.**
# Правда
#
# **Утверждение 5: При определении функции нужно указать хотя бы один параметр.**
# Ложь
#
# **Утверждение 6: Имя *args - это всего лишь соглашение. Вместо args можно использовать любое другое имя.**
# Правда
#
# **Утверждение 7: Функция, которая выводит значения на экран, аналогична функции, возвращающей эти значения.**
# Ложь
#
# **Утверждение 8: Различные виды аргументов в одной функции определять нельзя.**
# Ложь
#
# **Утверждение 9: При использовании именованных аргументов их порядок не имеет значения.**
# Правда
#
# **Утверждение 10: В функции-генераторе нужно использовать оператор yield вместо оператора return.**
# Правда

# # 6.8.3. Практические задания

# + [markdown] vscode={"languageId": "plaintext"}
# ### 1. Напишите функцию, которая проверяет, является ли год високосным.
# -


# Задача 1: Проверка високосного года
def is_leap(year: int) -> bool:
    """Check if a year is leap."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# ### 2. Напишите функцию f(х), возвращающую простые множители любого числа х (пример простых множителей: 36 - [2,2,3,3], 30 - [2,3,5]).


# Задача 2: Напишите функцию f(х), возвращающую простые множители люб. числа х
# (пример простых множителей: 36 - [2,2,3,3], 30 - [2,3,5])
def get_prime_factors(number: int) -> list[int]:
    """Return prime factors of a number.

    Args:
        number: The number to factorize
    Returns:
        list[int]: List of prime factors

    Example:
        >>> get_prime_factors(36)
        [2, 2, 3, 3]
        >>> get_prime_factors(30)
        [2, 3, 5]
    """
    factors = []
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    if number > 1:
        factors.append(number)

    return factors


# ### 3. Напишите функцию для преобразования температуры из градусов Цельсия в градусы Фаренгейта. Напишите еще одну функцию для обратного преобразования.


# +
# Задача 3: Конвертация температуры
def to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5 / 9


# -

# ### 4. Напишите функцию для вычисления факториала любого числа.


# Задача 4: Вычисление факториала
def calculate_factorial(number: int) -> int:
    """Calculate factorial of a number."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if number == 0:
        return 1
    return number * calculate_factorial(number - 1)


# ### 5. Напишите функцию преобразования любого числа от 1 до 100 в римское число.


def to_roman(number: int) -> str:
    """Convert decimal number to Roman numeral (1-100)."""
    if not 1 <= number <= 100:
        raise ValueError("Number must be between 1 and 100")

    roman_values = [
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = ""
    for value, numeral in roman_values:
        while number >= value:
            result += numeral
            number -= value
    return result


# ### 6. Напишите функцию f(х), которая возвращает таблицу умножения числа х.


# Задача 6: Таблица умножения
def get_multiplication_table(num: int) -> None:
    """Print multiplication table for a number."""
    print(f"\nMultiplication table for {num}:")
    for i in range(1, 11):
        result = num * i
        print(f"{num} × {i} = {result}")


# ### 7. Напишите функцию, которая принимает в качестве входных данных список и возвращает его перевернутый вариант.


def reverse_sequence(data: list[int]) -> list[int]:
    """Return reversed version of a list."""
    return data[::-1]


# ### 8. Напишите функцию для расчета сложных процентов.


# Задача 8: Расчет сложных процентов
def calculate_interest(
    principal: float,
    rate: float,
    years: int,
    comp_per_year: int = 12,
) -> float:
    """Calculate compound interest."""
    return principal * (1 + rate / comp_per_year) ** (comp_per_year * years)


# ### 9. Напишите функцию f(х), где х - любое 6-значное число, а функция возвращает сумму его цифр.


# Задача 9: Сумма цифр шестизначного числа
def get_digits_sum(number: int) -> int:
    """Calculate sum of digits in a 6-digit number."""
    if not 100000 <= number <= 999999:
        raise ValueError("Number must be 6 digits")
    return sum(int(digit) for digit in str(number))


# ### 10. Напишите функцию, которая проверяет, является ли переданное число простым.


# Задача 10: Проверка простого числа
def is_prime(number: int) -> bool:
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
