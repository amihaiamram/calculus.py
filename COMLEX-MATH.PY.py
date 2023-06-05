import sympy as sp


def der(func, *arg):
    der_list = []
    for i in range(len(arg)):
        der_now = sp.diff(func, *arg[:i])
        der_list.append(der_now)
    return der_list


def intg(func, *arg, var, snum, fnum):
    print(f"""
        i will intagrate the func {func} {len(arg)} with the variable {var} 
        times , from {snum} to {fnum}""")
    return sp.integrate(func, *arg, (var, snum, fnum))


def sim_intger(func, *arg):
    return sp.integrate(func, *arg)


x, y, z = sp.symbols("x y z")
op = int(input(" do you want definitive or regular "))
f = x ** 3 + x * z
dervs = []
times = int(input(" how many times do you want to preform an integral "))
for time in range(times):
    var = input(" which variable would u like to integrate now ")
    dervs.append(var)

integration_vars = [sp.symbols(var) for var in dervs]
if op == 1 or op == 2:
    try:
        if op == 1:
            num1, num2 = float(input(" what is the range of the integral "), input())
            res = intg(f, *integration_vars[::-1], var, num1, num2)
            print(res)
        elif op == 2:
            result = sim_intger(f, *integration_vars[::-1])
            print(result)
    except ValueError:
        print("Invalid limits. Please enter valid numerical limits for integration.")
else:
    res = der(f, *integration_vars[::-1],[x,y,z])
    print(res)
