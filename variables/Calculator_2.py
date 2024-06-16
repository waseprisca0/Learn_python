# Functions for Operations
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
     return x * y
def divide(x, y):
    if y == 0:
        raise ValueError("Can not be divided by zero!")
    else:
        return x / y

# Calculate Function
def calculate(operation, x, y):
    if operation == '+':
        return add(x,y)
    elif operation == '-':
        return subtract(x,y)
    elif operation == '*':
        return multiply(x,y)
    elif operation == '/':
        return divide(x, y)
    else:
        raise ValueError("Invalid operation!")


def main():
   
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    operation = input("choose an operation (+, -, *, /): ")

    
    
    result = calculate(operation, x, y)
    print(f"{x} {operation} {y} = {result}")
    
    
        
if __name__ == "__main__":
    main()
