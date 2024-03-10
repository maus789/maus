def resilient_calculator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            print(f"Виникла помилка: {e}. Перевірте вираз.")
            return None
    return wrapper

def calculate(expression):
    return eval(expression)

expression = "2 + 3 * 5"
print(calculate(expression))

expression = "10 / 0"
print(calculate(expression))