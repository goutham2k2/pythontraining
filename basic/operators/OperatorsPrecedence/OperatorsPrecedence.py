#Example 1: Basic Operator Precedence

result = 10 + 5 * 2
print("Result:", result)

#10 + (5 * 2) = 10 + 10 = 20


#Example 2: Using Parentheses to Override Precedence

result = (10 + 5) * 2
print("Result:", result) #Result: 30


#Example 3: Mixing Logical and Arithmetic Operators

value = 10
result = value > 5 and value < 20
print("Result:", result)

"""
Result: True
(10 > 5) and (10 < 20) → True and True → True


BODMAS


"""
