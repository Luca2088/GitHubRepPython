def arithmetic_arranger(problems, show_answers=False):
    final_op1 = ""
    final_op2 = "\n"
    final_dash = "\n"
    final_result = "\n"
    #Problems more than 5
    if len(problems) > 5:
        return "Error: Too many problems."      
    for problem in problems:
    #Div or mult errors
        if "*" in problem:
            return "Error: Operator must be '+' or '-'."
        elif "/" in problem:
            return "Error: Operator must be '+' or '-'."
        problem_spaceless = problem.replace(" ","")
        #Sum path div
        if "+" in problem:
            operands = problem_spaceless.split("+")
            if operands[0].isdigit() and operands[1].isdigit():
                if len(operands[0])>4 or len(operands[1]) > 4:
                    return 'Error: Numbers cannot be more than four digits.'
                else:
                    #CONVERITR EL FORMATO
                    #4 variables op1, op2, linea, res
                    digit_op1 = len(operands[0])
                    digit_op2 = len(operands[1])
                    cant_lineas = 2 + max(digit_op1,digit_op2)
                    line_op1 = " "*(cant_lineas - digit_op1) + operands[0]
                    line_op2 = "+" + " "*(cant_lineas-digit_op2-1) + operands[1]
                    line_dash = "-"*cant_lineas
                    result = int(operands[0])+int(operands[1])
                    digit_result = len(str(result))
                    line_result = " "*(cant_lineas-digit_result)+str(result)
                    final_op1 += line_op1+"    "
                    final_op2 += line_op2+"    "
                    final_dash += line_dash+"    "
                    final_result += line_result+"    "
            else:
                return "Error: Numbers must only contain digits."

#Substraction path div
        if "-" in problem:
            operands = problem_spaceless.split("-")
            if operands[0].isdigit() and operands[1].isdigit():
                if len(operands[0])>4 or len(operands[1]) > 4:
                    return 'Error: Numbers cannot be more than four digits.'
                else:
                    #CONVERITR EL FORMATO
                    #4 variables op1, op2, linea, res
                    digit_op1 = len(operands[0])
                    digit_op2 = len(operands[1])
                    cant_lineas = 2 + max(digit_op1,digit_op2)
                    line_op1 = " "*(cant_lineas - digit_op1) + operands[0]
                    line_op2 = "-" + " "*(cant_lineas-digit_op2-1) + operands[1]
                    line_dash = "-"*cant_lineas
                    result = int(operands[0])-int(operands[1])
                    digit_result = len(str(result))
                    line_result = " "*(cant_lineas-digit_result)+str(result)
                    final_op1 += line_op1+"    "
                    final_op2 += line_op2+"    "
                    final_dash += line_dash+"    "
                    final_result += line_result+"    "

            else:
                return "Error: Numbers must only contain digits."
    if show_answers==True:
        return final_op1[0:-4] + final_op2[0:-4] + final_dash[0:-4] + final_result[0:-4]
    if show_answers==False:
        return final_op1[0:-4] + final_op2[0:-4] + final_dash[0:-4]

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')

