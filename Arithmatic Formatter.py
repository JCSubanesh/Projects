new_list  =['32 - 698', '1 - 3801', '45 + 43', '123 + 49']
def arithmetic_arranger(problems,show = False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_numbers = list()
    second_numbers = list()
    operators = list()
    for i in range(0,len(problems)):
        first_numbers.append(problems[i].split()[0])
        second_numbers.append(problems[i].split()[2])
        operators.append(problems[i].split()[1])
    
    # Checks
    for i in range(0,len(first_numbers)):
        if (operators[i] != "+" and operators[i] != "-"):
            return "Error: Operator must be '+' or '-'."
    # Checks
        if not (first_numbers[i].isdigit() and second_numbers[i].isdigit()):
            return "Error: Numbers must only contain digits."
    # Checks
        if len(first_numbers[i]) and len(second_numbers[i]) > 4:
            return "Error: Numbers cannot be more than four digits."
    
    first_line = list()
    second_line = list()
    dashes_line = list()
    answer_line = list()
    for i in range(0,len(problems)):
        if len(first_numbers[i]) >=len(second_numbers[i]):
            first_line.append("  "+first_numbers[i])
        else:
            first_line.append(" "*(len(second_numbers[i])-len(first_numbers[i])+2)+ first_numbers[i])

        if len(second_numbers[i])>=len(first_numbers[i]):
            second_line.append(operators[i]+" "+second_numbers[i] )
        else:
            second_line.append(operators[i]+" "*(len(first_numbers[i])-len(second_numbers[i])+1)+second_numbers[i])
        
    for i in range(0,len(first_line)):
        dashes_line.append("-" * (max(len(first_numbers[i]), len(second_numbers[i]))+2))
    
    if show:
        for i in range(0,len(first_line)):
            if operators[i] == "+":
                ans = int(first_numbers[i])+int(second_numbers[i])
                answer_line.append((" "*(len(dashes_line[i]) -len(str(ans))))+str(ans))
            else:
                ans = int(first_numbers[i])- int(second_numbers[i])
                answer_line.append((" "*(len(dashes_line[i]) -len(str(ans))))+str(ans))
        arranged_problems = "    ".join(first_line)+"\n"+"    ".join(second_line)+"\n"+"    ".join(dashes_line)+"\n"+"    ".join(answer_line)

    else:
        arranged_problems = "    ".join(first_line)+"\n"+"    ".join(second_line)+"\n"+"    ".join(dashes_line)
    return arranged_problems


print(arithmetic_arranger(new_list))
