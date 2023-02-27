def divition_decorator(func):
    def wrapper(x,y):
        if y>x:
            x,y = y,x
        return func(x,y)
    return wrapper

@divition_decorator
def division(x,y):
    result = x/y
    return result

d = division(2,10)
print(d)