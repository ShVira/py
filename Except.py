
# Виняткові ситуації - перехід режиму виконання програми
# від послідовного до аварійного. Якщо виняток
# оброблюється, то робота програми відновлюється в
# точці прийняття винятку, якщо ні - то програма
# завершується помилкою.
# Необхідність винятків - у зупинці роботи конструкторів,
# які іншим способом зупинити неможна. Для інших задач
# це зручність, яка може бути замінена іншими схемами.


def throw_value_error():
    # ValueError - неправильне значення аргументу
    raise ValueError("Invalid value")


def throw_type_error():
    # TypeError - операція виконана з неправильним типом даних
    raise TypeError("Something went wrong...")


def throw_os_error():
    # OSError - помилка, пов'язана з операційною системою
    raise OSError("Operating system error")


def throw_index_error():
    # IndexError - звернення до індексу, якого не існує
    numbers = [1, 2, 3]
    print(numbers[5])


def throw_key_error():
    # KeyError - звернення до неіснуючого ключа словника
    student = {"name": "Anna"}
    print(student["age"])


def throw_zero_division_error():
    # ZeroDivisionError - ділення на нуль
    result = 10 / 0


def throw_attribute_error():
    # AttributeError - звернення до неіснуючого атрибута
    number = 10
    number.append(5)


def no_throw():
    pass


def main():
    # Список доступних винятківв
    exceptions = {
        1: ("TypeError", throw_type_error),
        2: ("ValueError", throw_value_error),
        3: ("OSError", throw_os_error),
        4: ("IndexError", throw_index_error),
        5: ("KeyError", throw_key_error),
        6: ("ZeroDivisionError", throw_zero_division_error),
        7: ("AttributeError", throw_attribute_error)
    }

    while True:
        print("\nВиберіть тип винятку:")
        print("1. TypeError")
        print("2. ValueError")
        print("3. OSError")
        print("4. IndexError")
        print("5. KeyError")
        print("6. ZeroDivisionError")
        print("7. AttributeError")
        print("0. Exit")

        try:
            choice = int(input("> "))

            if choice == 0:
                print("Програму завершено.")
                break

            if choice not in exceptions:
                print("Невірний вибір. Спробуйте ще раз.")
                continue

            exception_name, throw_function = exceptions[choice]

            try:
                # Створення вибраної виняткової ситуації
                throw_function()

            except ValueError:
                print("У програмі оброблено ValueError")

            except TypeError:
                print("У програмі оброблено TypeError")

            except OSError:
                print("У програмі оброблено OSError")

            except IndexError:
                print("У програмі оброблено IndexError")

            except KeyError:
                print("У програмі оброблено KeyError")

            except ZeroDivisionError:
                print("У програмі оброблено ZeroDivisionError")

            except AttributeError:
                print("У програмі оброблено AttributeError")

            else:
                print("'Else' block executed")

            finally:
                print("Finally block executed")

        except ValueError:
            print("Помилка введення! Введіть ціле число.")


if __name__ == '__main__':
    main()



