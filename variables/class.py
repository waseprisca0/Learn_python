class Calculator:
    def add(self, x, y):
         return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

def main():
    calculator = Calculator()
    
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    try:
        if operation == '+':
            result = calculator.add(x, y)
        elif operation == '-':
            result = calculator.subtract(x, y)
        elif operation == '*':
            result = calculator.multiply(x, y)
        elif operation == '/':
            result = calculator.divide(x, y)
        else:
            raise ValueError("Invalid operation!")
        
        print(f"The result of {x} {operation} {y} = {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
