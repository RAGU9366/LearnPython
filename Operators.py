# ---------- Operators in Python ---------- #

# An Operator is a symbol that will perform mathematical operations on variables or values...
# Operators operate on operands (values) and return a result...

# ---------- 7 Types of operators in Python ---------- #

# 1. Arithmetic Operators: { +  -  *  /  **  //  % }

num1 = 7
num2 = 4
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2)
print(num1 // num2)  # Quotient rounded to next smallest integer...
print(num1 % num2)  # Remainder...

# 2. Relational Operators / Comparison Operators: { <  >  <=  >=  ==  != }

print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2)
print(num1 != num2)

# 3. Assignment Operators: { =  +=  -=  *=  /=  %=  **=  //= }

num3 = 8  # Assign
print(num3)

num3 += 8  # Add and Assign
print(num3)

num3 -= 8  # Subtract and Assign
print(num3)

num3 *= 8  # Multiply and Assign
print(num3)

num3 /= 2  # Divide and Assign
print(num3)

num3 = 8
num3 %= 3  # Modulus and Assign
print(num3)

num3 **= 2  # Exponentiation and Assign
print(num3)

num3 //= 2  # Floor-Divide and Assign
print(num3)

# 4. Logical Operators: { and  or  not }

x = True and False
print(x)

x = True or False
print(x)

x = not False
print(x)

# 5. Membership Operators: { in  not in }

x = 2 in [1, 2, 3]
print(x)

x = 2 not in [1, 2, 3]
print(x)

# 6. Identity Operators: { is  not is }

a = 5
x = a is 5.0  # Similar to ==
print(x)

x = a is not 5.0  # Similar to !=
print(x)

# 7. Bitwise Operators: { &  |  ^  ~  <<  >> }

print(3 & 4)  # (Bitwise and) 3 & 4 is 011 & 100. This is 000 (0)...
print(3 | 4)  # (Bitwise or) 3 | 4 is 011 | 100. This is 111 (7)...
print(3 ^ 4)  # (Bitwise xor) 3 ^ 4 is 011 ^ 100. This is 111 (7)...
print(~3)  # (Bitwise 1's complement) !3 is 011. Negation of this is 100. The result is -4...
print(4 << 2)  # (Bitwise left-shift) 4 << 2. This is 10000 (16)...
print(4 >> 2)  # (Bitwise right-shift) 4 >> 2. This is 1 (1)...

# ---------- End of File ---------- #
