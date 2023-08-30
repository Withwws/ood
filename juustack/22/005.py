class Stack():

    def __init__(self, ls = None):
        self.items = ls
    
    def push(self, value):
        self.items.append(value)
        
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
def postFixeval(st):
    def perform_operation(operator, operand1, operand2):
        if operand1 == 'DUP':
            return operand1 * 2
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand2 - operand1
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand2 / operand1
        elif operator == 'POP':
            return stack.pop()
        elif operator == 'PSH':
            stack.append(operand1)
        else:
            raise ValueError("Invalid operator: " + operator)

    stack = []

    for token in st:
        if token.isdigit() or (token[0] == '-' and token.isdigit()):
            # If the token is a number (positive or negative), push it onto the stack.
            stack.append(float(token))
        else:
            # If the token is an operator, pop two operands from the stack and perform the operation.
            operand2 = stack.pop()
            operand1 = stack.pop()
            print(token, operand1, operand2)
            # result = perform_operation(token, operand1, operand2)
            # stack.append(result)

    # The final result will be the only item left on the stack.
    return stack[0]

            


print("* Stack Calculator *")

tok = list(input("Enter arguments : ").split())

juu = int(postFixeval(tok))
print(juu)