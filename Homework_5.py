import random

class EncapsulatedMath:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def perform_operation(self):
        operator = random.choice(['+', '-', '*', '/'])
        if operator == '+':
            return self.num1 + self.num2
        elif operator == '-':
            return self.num1 - self.num2
        elif operator == '*':
            return self.num1 * self.num2
        elif operator == '/':
            return self.num1 / self.num2 if self.num2 != 0 else "Ділення на нуль!"

    def __str__(self):
        result = self.perform_operation()
        return f"Результат операції: {result}"

encapsulated_math = EncapsulatedMath(10, 5)
print(encapsulated_math)