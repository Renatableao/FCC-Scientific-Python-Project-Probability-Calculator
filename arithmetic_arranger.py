import re
import operator

def arithmetic_arranger(problems, result=False):
  arranged_problems = []
  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:

    # error of operand is not + or -
    if not re.search('^.+\s*[+-]\s*.+$', problem):
      return "Error: Operator must be '+' or '-'."

    # error if operands does not contain only digits
    if not re.search('^[0-9]+\s*[+-]\s*[0-9]+$', problem):
      return "Error: Numbers must only contain digits."

    #error if operands are longer than four digits
    if not re.search('^[0-9]{1,4}\s*[+-]\s*[0-9]{1,4}$', problem):
      return "Error: Numbers cannot be more than four digits."

  # get first and second operands and operators
  first_op = re.findall('([0-9]+)[\s]*[+-]', str(problems))
  second_op = re.findall('[+-]\s*([0-9]+)', str(problems))
  operators = re.findall('[+-]', str(problems))

  # add to list first line with operands
  for i in range(len(operators)): 
    # calculate problem width
    char_count = len(str(max(int(first_op[i]), int(second_op[i])))) + 2
    arranged_problems.append((char_count - len(first_op[i])) * " ")
    arranged_problems.append(first_op[i])
    
    if i < (len(operators) -1):
      arranged_problems.append("    ")

  # add to list new line
  arranged_problems.append("\n")

  # add to list line with operators and operands
  for i in range(len(operators)): 
    # calculate problem width
    char_count = len(str(max(int(first_op[i]), int(second_op[i])))) + 2
    arranged_problems.append(operators[i])
    arranged_problems.append((char_count - len(second_op[i]) - 1) * " ")
    arranged_problems.append(second_op[i])
    
    if i < (len(operators) -1):
      arranged_problems.append("    ")

  # add to list new line
  arranged_problems.append("\n") 

  # add to list dashes
  for i in range(len(operators)):
    # calculate problem width
    char_count = len(str(max(int(first_op[i]), int(second_op[i])))) + 2
    arranged_problems.append(char_count * "-")
    
    if i < (len(operators) -1):
      arranged_problems.append("    ")

  # add results
  if result == True:
    arranged_problems.append("\n") 
    for i in range(len(operators)):
      # calculate problem width
      char_count = len(str(max(int(first_op[i]), int(second_op[i])))) + 2
      problem_result = str(eval(first_op[i] + operators[i] + second_op[i]))
      arranged_problems.append((char_count - len(problem_result)) * " " + problem_result)
      
      if i < (len(operators) -1):
        arranged_problems.append("    ")
    



  return ''.join(arranged_problems)
