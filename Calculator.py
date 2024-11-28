class Calculator:
    def Calculate(self, value1, value2, operation):
        if (operation == "+"):
           return value1 + value2
          
        if (operation == "-"):
            return value1 - value2
          
        if (operation == "*"):
           return value1 * value2
          
        if (operation == "/" and value2 != 0):
           return value1 / value2
        else:
            return 0
          

    def Power(self, value, exponent):
        result = value
        for i in range(exponent):
            result *= value

        return result