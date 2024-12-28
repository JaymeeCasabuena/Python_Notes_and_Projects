"""
Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
Numbers should be right-aligned.
There should be four spaces between each problem.
There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

"""


def arithmetic_arranger(problems, show_answers=False):

    top_line = ""
    operator_line = ""
    dash_line = ""
    result_line = ""

    if len(problems) > 5:
        return f'Error: Too many problems.'

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if len(operand1) > 4 or len(operand2) > 4:
            return f'Error: Numbers cannot be more than four digits.'
        
        if not operand1.isnumeric() or not operand2.isnumeric():
            return f'Error: Numbers must only contain digits.'
        
        if operator == "+":
            result = int(operand1) + int(operand2)
        elif operator == "-":
            result = int(operand1) - int(operand2)
        else:
            return f"Error: Operator must be '+' or '-'."
        
        width = max(len(str(operand1)), len(str(operand2))) + 2
        
        top_line += f"{str(operand1).rjust(width)}    "
        operator_line += f"{operator} {str(operand2).rjust(width - 2)}    "
        dash_line += "-" * width + "    "
        if show_answers: 
            result_line += f"{str(result).rjust(width)}    "
        else:
            result_line = ""
    
    arranged_problems = f"{top_line.rstrip()}\n{operator_line.rstrip()}\n{dash_line.rstrip()}"
    if show_answers:
        arranged_problems += f"\n{result_line.rstrip()}"

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 + 2", "45 + 43", "1234 + 49"])}')