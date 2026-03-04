class Calculator:
    def __init__(self, num1, num2):
        # Constructor
     
        if not (-100 <= num1 <= 100) or not (-100 <= num2 <= 100): 
            raise ValueError("Number must be between -100 and 100.")
        self.num1 = num1
        self.num2 = num2
        self.history = []
    
    def sum (self):
        # Adds two numbers between -100 and 100.
        
        result = self.num1 + self.num2
        self.history = self.history + [str(self.num1) + " + " + str(self.num2) + " = " + str(result)]
        print(self.history[-1])
        return result
    
    def multiply(self):
        # Multiplies two numbers between -100 and 100.
    
        result = self.num1 * self.num2
        self.history = self.history + [str(self.num1) + " * " + str(self.num2) + " = " + str(result)]
        print(self.history[-1])
        return result
    
    def subtract(self):
        # Subtracts two numbers between -100 and 100.
        
        choice = input("Which number would you like it to be subtracted by (n1 or n2)? ").strip().lower()
        if choice == "n1":
            result = self.num2 - self.num1
            self.history = self.history + [str(self.num2) + " - " + str(self.num1) + " = " + str(result)]
            print(self.history[-1])
            return result
        elif choice == "n2":
            result = self.num1 - self.num2
            self.history = self.history + [str(self.num1) + " - " + str(self.num2) + " = " + str(result)]
            print(self.history[-1])
            return result
        else:
            raise ValueError("Incorrect Response.")

    def divide(self):
        # Divides two numbers between -100 and 100.

        choice = input("Which number would you like it to be divided by (n1 or n2)? ").strip().lower()
        if choice == "n1":
            result = self.num2 / self.num1
            self.history = self.history + [str(self.num2) + " / " + str(self.num1) + " = " + str(result)]
            print(self.history[-1])
            return result
        elif choice == "n2":
            result = self.num1 / self.num2
            self.history = self.history + [str(self.num1) + " / " + str(self.num2) + " = " + str(result)]
            print(self.history[-1])
            return result
        else:
            raise ValueError("Incorrect Response.")
            
statement = False
while statement == False:
    # Main program.

    print("Welcome to the Calculator!")
    print("You can add, multiply, divide and subtract certain numbers in this game! All numbers will be stored for each game!")
    num1 = int(input("Enter first number (-100 to 100): "))
    num2 = int(input("Enter second number (-100 to 100): "))
    obj = Calculator(num1, num2)
    while True:
        print("Enter an operation:")
        print("1) Add the numbers\n2) Multiply the numbers\n3) Divide the numbers\n4) Subtract the numbers\n5) Print the numbers\n6) Enter new numbers\n7) Stop")
        methodChoice = int(input("Enter your choice: "))
        if methodChoice == 1:
            answer = obj.sum()
        elif methodChoice == 2:
            answer = obj.multiply()
        elif methodChoice == 3:
            answer = obj.divide()
        elif methodChoice == 4:
            answer = obj.subtract()
        elif methodChoice == 5:
            print("All operations so far:")
            for i in obj.history:
                print(i)
        elif methodChoice == 6:
            break
        elif methodChoice == 7:
            statement = True
            break
        else:
            raise ValueError("Invalid Choice.")

print("Thank you for playing!")