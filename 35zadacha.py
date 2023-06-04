# Задача №35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes

def prime_number(n):
    if n < 2:
        return False
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Введите число: "))

if prime_number(n):
    print("Да, число", n, "является простым")
else:
    print("Нет, число", n, "не является простым")
