N = int(input("Please enter a positive integer number here: "))

numbers = []

for i in range(N):
    num = int(input("You will need to provide total  " + str(N) + f" numbers. Please Enter number {i + 1}: "))
    numbers.append(num)

X = int(input("Please enter test integer X: "))

if X in numbers:
    index = numbers.index(X) + 1
    print(f"The sequence index number of test integer X is {index}.")
else:
    print("-1")
