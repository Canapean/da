def validate_pin(a):
    if (len(a) == 4 or len(a) == 6) and a.isdigit() == True:
        return True
    else:
        return False
print(validate_pin('1434'))