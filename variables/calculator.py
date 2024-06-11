# Functions for Operations

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference when y is subtracted from x."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient when x is divided by y. Raise a ValueError if y is zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# Calculate Function

def calculate(operation, x, y):
    """Call the appropriate arithmetic function based on the operation."""
    if operation == 'add':
        return add(x, y)
    elif operation == 'subtract':
        return subtract(x, y)
    elif operation == 'multiply':
        return multiply(x, y)
    elif operation == 'divide':
        return divide(x, y)
    else:
        raise ValueError("Invalid operation!")

# Main Function

def main():
    try:
        print("Addition:", calculate('add', 10, 5))             # Output: 15
        print("Subtraction:", calculate('subtract', 10, 5))     # Output: 5
        print("Multiplication:", calculate('multiply', 10, 5))  # Output: 50
        print("Division:", calculate('divide', 10, 5))          # Output: 2.0
        print("Division:", calculate('divide', 10, 0))          # This will raise an error
    except ValueError as e:
        print(e)

# Run the main function
if __name__ == "__main__":
    main()
