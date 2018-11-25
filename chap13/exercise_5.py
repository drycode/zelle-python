def baseConversion(num, base):
    digit = num % base
    print(num, digit)
    num = num // base
    
    if num == 0:
        return 1
    elif num < base:
        digit = num
        num = 0
        print(num, digit)
    else:
        baseConversion(num, base)
    
baseConversion(153, 10)

        

