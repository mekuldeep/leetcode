def romanizer(numbers):
    values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    def converter(n):
        result = ''
        for val, symbol in values:
            while n >= val:
                result += symbol
                n -= val
        return result
    
    return [ converter(n) for n in numbers ]
    
    
    
result = romanizer([75,80,99,100, 875])
print(result)