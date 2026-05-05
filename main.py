from calculator import Calculator
from input_handler import InputHandler

class CalculatorApp:
    def __init__(self):
        self.calculator = Calculator()
        self.input_handler = InputHandler()

    def run(self):
        while True:
            try:
                operation = self.input_handler.get_operation_choice()
                num1 = self.input_handler.get_number("Enter the first number: ")
                num2 = self.input_handler.get_number("Enter the second number: ")
                result = self.calculator.perform_operation(operation, num1, num2)
                print(f"Result: {result}")
            except ValueError as e:
                print(e)
            except ZeroDivisionError as e:
                print(e)
                
            if operation == "5":
                num1 = self.input_handler.get_number("Enter base: ")
                num2 = self.input_handler.get_number("Enter exponent: ")
            else:
                num1 = self.input_handler.get_number("Enter the first number: ")
                num2 = self.input_handler.get_number("Enter the second number: ")