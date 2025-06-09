# Print Hello World
# Add two numbers
# Check if number is even or odd
# Find maximum of three numbers
# Check if a number is prime


# Print Hello World
print("Hello world")

# Add two numbers
num1=25
num2=56
print(num1+num2)
print(5+10)

# Check if number is even or odd
# number=int(input("Enter Any number you want to check even or odd "))

# if (number%2==0):
#     print(f"number {number} is even")
# else:
#     print(f"Number {number} is odd")

# Find maximum of three numbers
# list=[25,63,45]
# print(max(list))

# a=int(input("Enter first number="))
# b=int(input("Enter first number="))
# c=int(input("Enter first number="))

# if(a>b and a>c):
#     print(f"{a} is max value")
# elif(b>a and b>c):
#     print(f"{b} is max value")
# else:
#     print(f"{c} is max value")


# Check if a number is prime
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")




