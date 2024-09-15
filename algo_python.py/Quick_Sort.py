#Quick Sort Algrorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # Create partitions
    pivot = arr[len(arr) // 2]
    left = []
    right = []
    middle = []
    
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)
    
    return quick_sort(left) + middle + quick_sort(right)
# Take numbers in a single line
n = int(input("How many numbers do you want to sort? "))
user_input = input(f"Enter {n} numbers separated by spaces: ")

# Convert the input string into a list of integers
arr = []
for num in user_input.split():
    arr.append(int(num))

sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
