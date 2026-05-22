# Program 1: Even/odd checker

a = int(input("Enter a number: "))
    
if(a==0):
    print(f"{a} is neither even nor odd..")

elif(a%2==0):
    print(f"{a} is even.")

else:    
    print(f"{a} is odd.")

# Program 2: Simple Calculator

b = int(input("Enter 1st number: "))
c = int(input("Enter 2nd number: "))

print("---Operations---\n")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("\n")

operation = input("Enter operation to be performed: ")
print("\n")


if(operation == '1'):
    print(f"The addition of {b} and {c} is: {b+c}")
elif(operation == '2'):
    print(f"The subtraction of {b} and {c} is: {b-c}")
elif(operation == '3'):
    print(f"The multiplication of {b} and {c} is: {b*c}")
elif(operation == '4'):
    print(f"The division of {b} and {c} is: {b/c}")
else:
    print("Invalid Input. Enter (1-4)")
