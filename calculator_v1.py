import math


#method to read operation
def select_operation(operations):
    for i, operation in enumerate(operations):
        print(f"{i}): {operation}")
    print('Type an operation number or a negative number to leave:')
    op = int(input())
    return op

#method to do calculation
def calculator(op, a, b=None):
    #execute the operation
    if b:
        if op == 0:
            return a+b
        elif op == 1:
            return a*b
        elif op == 2:
            return a-b
        elif op == 3: 
           return a**b
        elif op == 4:
            #verify if number is different from 0
            if a > 0:
                return math.log10(a)
            else:
                return None
        else:
            None
    else:
        if op == 4:
            #verify if number is different from 0
            if a > 0:
                return math.log10(a)
            else:
                return None
        else:
            None
    
    
#initialize with the name of operations
operations = ['Sum', 'Mul', 'Sub', 'Pow', 'Log10']

op = select_operation(operations)


#calculator main loop, exiting when any another option is selected
while(op in list(range(len(operations)))):
    
    #print selected opration
    print(f'Selected operation: {operations[op]}')
    
    
    #read the operators
    print('Type the first operator: ')
    a = float(input())
    
    #if 4 is selected read only a operator
    b = None
    if not op == 4:
        print('Type the second operator: ')
        b = float(input())
    
    
    #define string aux to print the result
    aux = '=======\nThe result is: {}\n======='
    
    result = calculator(op, a, b=b if not b is None else None)
    if result:
        print(aux.format(result))
    else:
        print('Operation can not be performed.')
    
    
    op = select_operation(operations)
    