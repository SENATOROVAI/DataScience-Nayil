# Создаем список
example_list = [2, 2.25, "Python"]
print("Initial list:", example_list)

# Преобразуем строку в список
str_list = list("help")
print("String to list:", str_list)

# Создаем новый список с кубами нечетных чисел от 0 до 19
cubes_of_odds = [x ** 3 for x in range(20) if x % 2 == 1]
print("Cubes of odd numbers:", cubes_of_odds)

# Длина списка
print("Length of cubes_of_odds:", len(cubes_of_odds))

# Проверка принадлежности элемента
print("Is 2 in example_list?", 2 in example_list)
print("Is 'Java' not in example_list?", "Java" not in example_list)

# Конкатенация списков
concat_list = example_list + str_list
print("Concatenated list:", concat_list)

# Повторение списка
repeated_list = example_list * 2
print("Repeated list:", repeated_list)

# Доступ к элементам по индексу
print("First element:", example_list[0])
print("Last element:", example_list[-1])

# Срезы
print("Slice of example_list:", example_list[0:2])
print("Slice with step:", example_list[::2])

# Минимальный и максимальный элементы
numeric_list = [2, 2.25, 1.5]
print("Minimum in numeric_list:", min(numeric_list))
print("Maximum in numeric_list:", max(numeric_list))

# Замена элемента
example_list[1] = 3.14
print("List after replacement:", example_list)

# Замена среза
example_list[0:2] = [1, 1.5]
print("List after slice replacement:", example_list)

# Удаление элементов среза
del example_list[0:2]
print("List after deleting slice:", example_list)

# Использование методов списков
# Добавление элемента
example_list.append("New Item")
print("List after append:", example_list)

# Подсчет количества элементов
print("Count of 'Python':", example_list.count("Python"))

# Расширение списка
example_list.extend([4, 5])
print("List after extend:", example_list)

# Индекс элемента
print("Index of 'Python':", example_list.index("Python"))

# Вставка элемента
example_list.insert(1, "Inserted Item")
print("List after insert:", example_list)

# Извлечение и удаление элемента
removed_item = example_list.pop(2)
print("Removed item:", removed_item)
print("List after pop:", example_list)

# Обратный порядок
example_list.reverse()
print("Reversed list:", example_list)

# Сортировка
sorted_list = sorted([5, 2, 3, 1, 4])
print("Sorted list:", sorted_list)
