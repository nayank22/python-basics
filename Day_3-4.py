# Program 3: Multiplication Table 

d = int(input("Enter the number whose multiplication table is to be printed: "))

for i in range(1,11):
    print(f"{d} X {i} = {d*i}")

print("\n".join(f"{d} X {i} = {d*i}" for i in range(1,11)))

# Program 4: Prime Number 
n = int(input("Enter a number: "))
def prime(n):
    if n<2:
        return False
    
    for i in range(2,int(n**0.5)+1):
        return False
    
    return True

prime(n)

print(f"{n} is prime: {prime(n)}")

