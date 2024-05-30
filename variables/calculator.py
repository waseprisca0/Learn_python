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

# Main Function
def main():
    #try:
        print("Addition:", calculate('+', 10, 5))             
        print("Subtraction:", calculate('-', 10, 5))     
        print("Multiplication:", calculate('*', 10, 5))  
        print("Division:", calculate('/', 10, 5))          
        #print("Division:", calculate('/', 10, 0))          
    #except ValueError as e:
        #print(e)

# Run the main function
if __name__ == "__main__":
    main()
    
