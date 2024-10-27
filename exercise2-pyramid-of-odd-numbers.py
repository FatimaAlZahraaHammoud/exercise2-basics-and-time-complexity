x = int(input("Enter a number: "))

for i in range(x):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num + 2
    print()