import sympy as sp


def process(function, var1, op):
    if op == 1:
        return sp.diff(function, var1)

    elif op == 2:
        return sp.integrate(function, (var1, num2, num1))

    elif op == 3:
        return sp.integrate(function, var1)
    else:
        return None


option = 0
while True:
    try:
        option = int(input("""choose an option
           1.
           2.
           3.
           """))

        if option <= 3:
            break
        else:
            print("invalid input")

    except ValueError:
        print("invalid value please enter a number")

times = int(input("how many times do you want to process the function: "))

f = str(input("please enter a formula: "))
x, y, z = sp.symbols("x y z")
variable_list = []
for time in range(times):
    vari = sp.symbols("x{}".format(time + 1))
    variable_list.append(vari)
steps = [f]
res = None
results = []
if option == 2:
    num1 = int(input("give me upper limit: "))
    num2 = int(input("give me lower limit: "))

for time in range(times):
    temp_var = variable_list[time]
    temp_func = steps[time]
    res = process(temp_func, temp_var, option)
    steps.append(res)

print(steps)
