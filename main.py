def divide(a, b):
   if b == 0:
       raise ValueError('It is forbidden to divide by zero')
   return a/b

def modulus(a, b):
    if b == 0:
        raise ValueError('It is forbidden to divide by zero')
    return a % b


