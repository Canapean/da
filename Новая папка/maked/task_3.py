def multiply(a:float | int, b:float | int) -> float | int:
    return a*b if type(a) == float or int and type(b) == float or int else "нужно число"
