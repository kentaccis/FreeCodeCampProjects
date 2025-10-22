
operators = set("+-")


def arithmetic_arranger(problems, show_answers=False):
    # checking if the input is valid
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Lists to store each line of the output
    top_line = []
    bottom_line = []
    dashes = []
    answers = []

    for problem in problems:
        left, operator, right = problem.split()
    # checking if the input is valid
        if operator not in operators:
            return "Error: Operator must be '+' or '-'."
        if not left.isdigit() or not right.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(left) > 4 or len(right) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # deciding on the width of elements
        width = max(len(left), len(right)) + 2
        top_line.append(left.rjust(width))
        bottom_line.append(operator + " " + right.rjust(width-2))
        dashes.append("-"*width)
        if show_answers:
            if operator == '+':
                answer = str(int(left) + int(right))
            else:
                answer = str(int(left) - int(right))
            answers.append(answer.rjust(width))

    arranged_problems = '    '.join(top_line) + '\n' + \
        '    '.join(bottom_line) + '\n' + \
        '    '.join(dashes)
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)
    return arranged_problems


print(
    f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
