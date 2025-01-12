from Calculator import Calculator
import os, sys, time

class UI:
    def __init__(self):
        self.calculator = Calculator()
        self.running = True
        self.operator = ""
        self.operators = ["*", "/", "-", "+"]
        self.numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.value1 = 0
        self.value2 = 0
        self.ans = 0
        self.timesToCalculate = 100


    def Run(self):
        while (self.running):
            self.HandleInput()
            self.PrintResult()


    def HandleInput(self):
        print("Enter calcualtion with the format\nvalue1 {+ | - | * | /} value2")
        input_ = input()

        if (input_.isalpha()): # Checks if it contains letters
            os.system("CLS") # Clear console, like in CPP
            print("Invalid input: Input contains letters. Please enter numbers and operators only.\n")
            self.HandleInput()

        if (" " not in input_):
            os.system("CLS")
            print("Invalid input: Must contain spaces between the operator and numbers.\n")
            self.HandleInput()
        
        if ((operator in input_ for operator in self.operators) and (number in input_ for number in self.numbers)): # Checks each element in the operators array
            if (self.SplitString(input_) is False):
                os.system("CLS")
                print("Parsing falied because of wrong format.\n")
                self.HandleInput()

            return
        
        os.system("CLS")
        print("Invalid input")
        self.HandleInput()


    def PrintResult(self):
        if (self.value2 == 0 and self.operator == "/"): # Handle errors in case the user tries to divide by zero.
            print("Error: Can't divide by zero.")
        else:
            totalTime = 0

            for i in range(self.timesToCalculate):
                startTime = time.perf_counter()
                self.ans = self.calculator.Calculate(self.value1, self.value2, self.operator)
                endTime = time.perf_counter()
                elapsed = endTime - startTime
                totalTime += elapsed
        
        averageTime = totalTime / self.timesToCalculate
        print(f"{self.value1} {self.operator} {self.value2} = {self.ans}\n")
        print(f"\nPerformed operation {self.timesToCalculate} times. Average time: {averageTime} seconds ({averageTime * 1000} milliseconds).\n")
        

    def SplitString(self, input_:str):
        parts = input_.split(" ")
        #  -- Before splitting --
        #  Format: number1 operator number2
        #  Example: "526 + 141"
        #
        #  -- After splitting --
        #    [0]       [1]        [2]
        #  number1   operator   number2
        #    526        +         141

        if len(parts) != 3:
            return False
        
        # Try to parse, catch the error if it fails. Returning true means it worked, false means error.
        try:
            self.value1 = float(parts[0])
            self.operator = parts[1]
            self.value2 = float(parts[2])
            return True
        except:
            return False