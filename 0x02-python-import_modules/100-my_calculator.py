#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    num_of_args = len(sys.argv[1:])
    if num_of_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    expression = sys.argv[1:]
    first_arg = int(expression[0])
    third_arg = int(expression[2])
    operator = expression[1]
    if operator == '+':
        print(f"{first_arg} + {third_arg} = {add(first_arg, third_arg )}")
    elif operator == '-':
        print(f"{first_arg} - {third_arg} = {sub(first_arg, third_arg)}")
    elif operator == '*':
        print(f"{first_arg} * {third_arg} = {mul(first_arg, third_arg)}")
    elif operator == '/':
        print(f"{first_arg} / {third_arg} = {div(first_arg, third_arg)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
