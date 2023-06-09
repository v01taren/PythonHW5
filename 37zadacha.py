# Задача №37. Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

def reverse_sequence(n):
    """
    Функция, которая выводит последовательность из N элементов в обратном порядке.
    """
    # Если N равно 0, то ничего не выводим
    if n == 0:
        return

    # Читаем следующее число от пользователя
    x = int(input())

    # Рекурсивно вызываем функцию для вывода оставшейся последовательности
    reverse_sequence(n - 1)

    # Выводим прочитанное число
    print(x)

# Читаем количество элементов от пользователя
n = int(input("Введите количество элементов: "))

# Вызываем функцию для вывода последовательности в обратном порядке
print("Введите последовательность:")
reverse_sequence(n)
