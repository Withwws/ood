class Calculator:
    def __init__(self):
        self.stack = []

    def run(self, instructions):
        def perform_operation(operator):
            operand2 = self.stack.pop()
            operand1 = self.stack.pop()
            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand2 - operand1
            elif operator == '*':
                result = operand1 * operand2
            elif operator == '/':
                result = operand2 // operand1
            else:
                raise ValueError("Invalid instruction: " + operator)
            self.stack.append(result)

        for instruction in instructions.split():
            if instruction.isdigit() or (instruction[0] == '-' and instruction[1:].isdigit()):
                # If the instruction is a number (positive or negative), push it onto the stack.
                self.stack.append(int(instruction))
            elif instruction == '+':
                perform_operation(instruction)
            elif instruction == '-':
                perform_operation(instruction)
            elif instruction == '*':
                perform_operation(instruction)
            elif instruction == '/':
                perform_operation(instruction)
            elif instruction == 'DUP':
                if len(self.stack) >= 1:
                    self.stack.append(self.stack[-1])
                else:
                    raise ValueError("Not enough operands for DUP.")
            elif instruction == 'POP':
                if len(self.stack) >= 1:
                    self.stack.pop()
                    if len(self.stack) == 0:
                        return "eiei"
                else:
                    raise ValueError("Not enough operands for POP.")
            else:
                return("Invalid instruction: " + instruction)

    def getValue(self):
        if len(self.stack) > 0 :
            return self.stack[-1] 
        # elif len(self.stack) == 0 :
        #     return "0"
        else: return 0
    
if __name__ == "__main__":
    print("* Stack Calculator *")
    arg = input("Enter arguments : ")
    machine = Calculator()
    machine.run(arg)
    juu = machine.getValue()
    if juu == 0:
        juu = machine.run(arg)
    if juu == "eiei":
        juu =0
    print (juu)
