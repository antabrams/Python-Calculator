class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addNums(self):
        return self.x + self.y

    def MultiplyNums(self):
        return self.x * self.y

    def SubNums(self):
        return self.x - self.y

    def DivideNums(self):
        if self.y != 0:
            return self.x / self.y
        else:
            return "Error: Division by zero is not allowed."

def get_input():
    try:
        x = float(input("Enter the first number (x): "))
        y = float(input("Enter the second number (y): "))
        return Calculator(x, y)
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return None

# Example usage
if __name__ == "__main__":
    calc = get_input()
    if calc:
        print(f"Addition: {calc.addNums()}")
        print(f"Multiplication: {calc.MultiplyNums()}")
        print(f"Subtraction: {calc.SubNums()}")
        print(f"Division: {calc.DivideNums()}")