num1 = float(input("Enter number a: "))
op = input("Enter operation: ")
num2 = float(input("Enter another number b: "))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*' or op == 'x':
    print(num1 * num2)
elif op == '/':
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("Math error!")
else:
    print("Wrong input")

