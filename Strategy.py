
# Патерн "Стратегія"
# Стратегія - це поведінковий патерн програмування,
# який дозволяє використовувати різні алгоритми
# для виконання однієї задачі.

import math


# Обчислення середнього арифметичного
def arithmetic_mean(numbers):
    return sum(numbers) / len(numbers)


# Обчислення середнього геометричного
def geometric_mean(numbers):
    product = 1

    for number in numbers:
        if number <= 0:
            raise ValueError("Числа повинні бути додатними")
        product *= number

    return product ** (1 / len(numbers))


# Обчислення середнього гармонічного
def harmonic_mean(numbers):
    if any(number <= 0 for number in numbers):
        raise ValueError("Числа повинні бути додатними")

    return len(numbers) / sum(1 / number for number in numbers)


# Обчислення середнього квадратичного
def quadratic_mean(numbers):
    return math.sqrt(sum(number ** 2 for number in numbers) / len(numbers))


# Функція вибору стратегії, яка дає мінімальне значення
# Повертає кортеж: (індекс стратегії, мінімальне значення)
def min_strategy(numbers, strategies):

    if not numbers:
        raise ValueError("Масив не повинен бути порожнім")

    results = []

    # Виконання кожного алгоритму на однаковому масиві
    for strategy in strategies:
        results.append(strategy(numbers))

    # Визначення мінімального значення
    min_value = min(results)

    # Пошук індексу алгоритму з мінімальним значенням
    min_index = results.index(min_value)

    return min_index, min_value


def main():

    # Масив даних для всіх алгоритмів
    numbers = [2, 4, 8, 16]

    # Список стратегій (алгоритмів розрахунку)
    strategies = [
        arithmetic_mean,
        geometric_mean,
        harmonic_mean,
        quadratic_mean
    ]

    # Назви алгоритмів для виведення результату
    strategy_names = [
        "Середнє арифметичне",
        "Середнє геометричне",
        "Середнє гармонічне",
        "Середнє квадратичне"
    ]

    print("Масив даних:", numbers)
    print("\nРезультати розрахунків:")

    # Виведення результату кожної стратегії
    for i, strategy in enumerate(strategies):
        print(f"{i}. {strategy_names[i]}: {strategy(numbers):.4f}")

    # Пошук стратегії з мінімальним значенням
    min_index, min_value = min_strategy(numbers, strategies)

    print("\nРезультат роботи min_strategy:")
    print("Індекс алгоритму:", min_index)
    print("Назва алгоритму:", strategy_names[min_index])
    print("Мінімальне середнє значення:", round(min_value, 4))


if __name__ == '__main__':
    main()