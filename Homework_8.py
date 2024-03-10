result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a має бути більше або рівне b")
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе")
        if b > 100:
            raise IndexError("b не може бути більше 100")
        return a / b
    except ValueError as ve:
        print(f"Помилка ValueError: {ve}")
    except ZeroDivisionError as zde:
        print(f"Помилка ZeroDivisionError: {zde}")
    except IndexError as ie:
        print(f"Помилка IndexError: {ie}")
    except Exception as e:
        print(f"Інша помилка: {e}")

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)