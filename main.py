# Program 1: Even/odd checker

# a = int(input("Enter a number: "))
    
# if(a==0):
#     print(f"{a} is neither even nor odd..")

# elif(a%2==0):
#     print(f"{a} is even.")

# else:    
#     print(f"{a} is odd.")

# Program 2: Simple Calculator

# b = int(input("Enter 1st number: "))
# c = int(input("Enter 2nd number: "))

# print("---Operations---\n")

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
# print("\n")

# operation = input("Enter operation to be performed: ")
# print("\n")


# if(operation == '1'):
#     print(f"The addition of {b} and {c} is: {b+c}")
# elif(operation == '2'):
#     print(f"The subtraction of {b} and {c} is: {b-c}")
# elif(operation == '3'):
#     print(f"The multiplication of {b} and {c} is: {b*c}")
# elif(operation == '4'):
#     print(f"The division of {b} and {c} is: {b/c}")
# else:
#     print("Invalid Input. Enter (1-4)")

# Program 3: Multiplication Table 

# d = int(input("Enter the number whose multiplication table is to be printed: "))

# for i in range(1,11):
#     print(f"{d} X {i} = {d*i}")

# print("\n".join(f"{d} X {i} = {d*i}" for i in range(1,11)))

# Program 4: Prime Number 
n = int(input("Enter a number: "))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

is_prime(n)

print(f"{n} is prime: {is_prime(n)}")


