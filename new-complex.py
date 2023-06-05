import sympy as sp

def process(function, var1):
    return sp.diff(function, var1)


# those two processes don't play along so i separated them
def integrals_fun(function, var1, op):
    if var1 == 'x':
        if op == 2:
            return sp.integrate(function, (x, num2, num1))
        elif op == 3:
            return sp.integrate(function, x)
    if var1 == 'y':
        if op == 2:
            return sp.integrate(function, (y, num2, num1))
        elif op == 3:
            return sp.integrate(function, y)
    if var1 == 'z':
        if op == 2:
            return sp.integrate(function, (z, num2, num1))
        elif op == 3:
            return sp.integrate(function, z)


####

option = 0
run = True
while run:
    while True:
        try:
            option = int(input("""choose an option
               1.derivative
               2.definite integration
               3.indefinite integration (dont forget the + c in the end )
               """))

            if option <= 3:
                break
            else:
                print("invalid input")

        except ValueError:
            print(" invalid value please enter a number")

    times = int(input(" how many times do u want to process the function "))

    f = input(" please enter a formula ")
    x, y, z = sp.symbols(" x y z")
    variable_list = []
    for time in range(times):
        vari = str(input(" pick a variable "))
        variable_list.append(vari)
    steps = []
    steps.append(f)
    res = None
    results = []
    # works
    if option == 1:
        for time in range(times):
            res = process(steps[time], variable_list[time])
            steps.append(res)
    if option == 2 or option == 3:
        if option == 2:
            num1 = int(input("give me upper and upper limit"))
            num2 = int(input("give me upper and lower limit"))
        for time in range(times):
            res = integrals_fun(steps[time], variable_list[time], option)
            steps.append(res)
    print(steps)
    conti = input(" do you want to keep going ? y/n : ")
    if conti != 'y':
        break
