# Define a function that performs basic arithmetic operations.
# This function, perform_operation, will be imported and used in a separate main.py script
#+ which will be provided

def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                print("Can not divide by 0")
            elif:
                return num1 / num2
