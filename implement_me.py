# Credits to ChatGPT

import math

def lcm(a, b):
    # Calculate the absolute value of the product of a and b
    abs_product = abs(a * b)
    # Calculate the GCD of a and b
    gcd = math.gcd(a, b)
    # Calculate the LCM using the formula
    lcm = abs_product // gcd
    return lcm

# Example usage:
num1 = 12
num2 = 18
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {result}")
