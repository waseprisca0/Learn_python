# Functions for Operations
<<<<<<< HEAD

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
=======
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
>>>>>>> 37379f5d0b91e51162e2b147de04f414ebe9d177
        return divide(x, y)
    else:
        raise ValueError("Invalid operation!")

# Main Function
<<<<<<< HEAD

def main():
    try:
        print("Addition:", calculate('add', 10, 5))             # Output: 15
        print("Subtraction:", calculate('subtract', 10, 5))     # Output: 5
        print("Multiplication:", calculate('multiply', 10, 5))  # Output: 50
        print("Division:", calculate('divide', 10, 5))          # Output: 2.0
        print("Division:", calculate('divide', 10, 0))          # This will raise an error
    except ValueError as e:
        print(e)
=======
def main():
    #try:
        print("Addition:", calculate('+', 10, 5))             
        print("Subtraction:", calculate('-', 10, 5))     
        print("Multiplication:", calculate('*', 10, 5))  
        print("Division:", calculate('/', 10, 5))          
        #print("Division:", calculate('/', 10, 0))          
    #except ValueError as e:
        #print(e)
>>>>>>> 37379f5d0b91e51162e2b147de04f414ebe9d177

# Run the main function
if __name__ == "__main__":
    main()
<<<<<<< HEAD
=======
    
>>>>>>> 37379f5d0b91e51162e2b147de04f414ebe9d177
