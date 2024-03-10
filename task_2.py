try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    if num2 == 0:
        print("Друге число не може бути рівним нулю. Спробуйте ще раз.")
    else:
        result = num1 / num2
        print("Результат ділення:", result)

except ValueError:
    print("Введено некоректне значення. Будь ласка, введіть число.")
except Exception as e:
    print("Сталася помилка:", e)


try:
    my_list = ["apple", "banana", "cherry", "date"]

    index = int(input("Введіть індекс елемента списку: "))

    element = my_list[index]
    print("Елемент зі списку за вказаним індексом:", element)

except IndexError:
    print("Ви ввели недійсний індекс. Введіть число в межах від 0 до", len(my_list) - 1)
except ValueError:
    print("Введено некоректне значення. Будь ласка, введіть ціле число.")
except Exception as e:
    print("Сталася помилка:", e)


while True:
    try:
        number = float(input("Будь ласка, введіть число: "))
        print("Ви ввели число:", number)
        break
    except ValueError:
        print("Неможливо перетворити введений рядок у число. Будь ласка, введіть коректне число.")
    except Exception as e:
        print("Сталася помилка:", e)