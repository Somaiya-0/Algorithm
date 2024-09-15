a = []
n = int(input("Enter range: "))

user_input = input(f"Enter {n} numbers separated by spaces: ")
for num in user_input.split():
    a.append(int(num))

print("Before sorting: ", a)

# Bubble Sort Algoritm
for i in range(0, n - 1):
    for j in range(0, n - i - 1):
        # Swap 
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

print("Sorted: ", a)
