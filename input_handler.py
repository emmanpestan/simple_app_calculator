class InputHandler:
    def get_operation(self):
        print("\n Calculator via python")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponent")

        choice = input("Choose an operation: ")

        if choice not in ["1","2","3","4","5"]:
            raise ValueError("Select only from the the operation choice")
    
        return choice
    
    def get_numbers(self, message):
        while True:
            try:
                num = float(input(message))
                return num
            except ValueError:
                print("Invalid input. Please enter a valid number.")
