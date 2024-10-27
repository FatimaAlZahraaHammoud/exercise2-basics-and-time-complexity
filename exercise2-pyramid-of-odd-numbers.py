x = int(input("Enter a number: "))

while x <= 0:
    print("Please enter a valid positive integer!")
    x = int(input("Enter a number: "))

for i in range(x):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num + 2
    print()