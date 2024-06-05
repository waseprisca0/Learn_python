class Calculator:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mult(self,x,y):
        return x*y
    def div(self,x,y):
        if y == 0:
            return ("can't be divided")
        return x/y
    

def main():
   
    x = float(input("enter number 1st:"))
    y = float(input("enter number 2nd:"))
    operation = input("choose operation(:x,-,*,/):")

    calculator = Calculator()

    try:
        if operation == '+':
            result = calculator.add(x,y)
        elif operation == '-':
            result = calculator.sub(x,y)
        elif operation == '*':
            result = calculator.mult(x,y)
        elif operation == '/':
            result = calculator.div(x,y)
        else:
            raise ValueError("invalide operation")

        print(f"{x} {operation} {y} = {result}")
        
    except ValueError as e:
        print(e)

if __name__ =="__main__":
    main()
