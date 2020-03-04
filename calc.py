def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mult(x, y):
    return x*y


def div(x, y):
    return x/y


print("Select operation:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
choice = input("Enter the choice=")
x = int(input("Enter first number="))
y = int(input("Enter second number="))
if choice == '1':
    print("The addition of two number is =", add(x, y))
elif choice == '2':
    print("The subtraction of two numbers is=", sub(x, y))
elif choice == '3':
    print("The multiplication of two numbers is=", mult(x, y))
elif choice == '4':
    print("The Division of two numbers is=", div(x, y))
