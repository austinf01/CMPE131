def calculator(num1,num2,oper):
     if oper == '+':
             return num1 + num2
     if oper == '-':
             return num1 - num2
     if oper =='*':
             return num1 * num2
     if oper == '/':
             return num1 / num2
     if oper == '//':
             return num1 // num2
     if oper == '**':
             return num1 ** num2

def parse_input():
        equation  = input("Enter equation: ")     #user input, ex. "10 + 5"
        eq = equation.split(' ')                #creates list [num1, oper, num2]
        num1 = float(eq[0])
        num2 = float(eq[2])
        oper = eq[1]
        print(calculator(num1,num2,oper)) #prints result

