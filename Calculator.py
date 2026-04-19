import ast
class Calculator:
    def __init__(self):
        # Constructor
        self.history = []
        self.variables = {}

    def add_history(self, entry):
        # Helper function for history.
        self.history.append(entry)

    def add(self, a, b):
        # Adds two numbers.
        return a + b
    
    def subtract(self, a, b):
        # Subtracts two numbers.
        return a - b
    
    def multiply(self, a, b):
        # Multiplies two numbers.
        return a * b
       
    def divide(self, a, b):
        # Divides two numbers.
        if b == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        return a / b
    
    def exponent(self, a, b):
        # Raises a number to the exponent.
        return a ** b
    
    def negate(self, a):
        # Negates a number.
        return -a
    
    def evaluate(self, expression):
        # Converts expression into AST tree for logical math.
        try:
            tree = ast.parse(expression, mode='exec')
            last = None
            for node in tree.body:
                
                if isinstance(node, ast.Assign):
                    var = node.targets[0].id
                    value = self._eval(node.value)
                    self.variables[var] = value
                    self.add_history(f"{var} = {value}") 
                    last = value
                elif isinstance(node, ast.Expr):
                    result = self._eval(node.value)
                    self.add_history(f"{expression} = {result}") 
                    last = result
            return last
        except Exception as e:
            return str(e)
    
    def _eval(self, node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Name):
            if node.id in self.variables:
                return self.variables[node.id]
            else:
                raise NameError(f"Undefined Variable: {node.id}")
        elif isinstance(node, ast.BinOp):
            left = self._eval(node.left)
            right = self._eval(node.right)

            if isinstance(node.op, ast.Add):
                return self.add(left, right)
            
            elif isinstance(node.op, ast.Sub):
                return self.subtract(left, right)
            
            elif isinstance(node.op, ast.Mult):
                return self.multiply(left, right)
            
            elif isinstance(node.op , ast.Div):
                return self.divide(left, right)
            
            elif isinstance(node.op, ast.Pow):
                return self.exponent(left, right)
            
        elif isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.USub):
                return self.negate(self._eval(node.operand))
            elif isinstance(node.op, ast.UAdd):
                return self._eval(node.operand)
        raise TypeError("Invalid Expression")
    
    def show_history(self):
        # Shows history
        for i in self.history:
            print(i)

# Main Method
if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to the Calculator! (type 'exit' to quit)")
    while True:
        exp = input("Enter expression: ")
        
        if exp.lower() == "exit":
            break
        result = calc.evaluate(exp)
        print("=", result)
    print("\nHistory")
    calc.show_history()
