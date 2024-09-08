a=[]
n=int(input("Enter range :" ,))
for j in range(0,n):
    b=int(input("",))
    a.append(b)
print("before sorting : ",a)

print("Processing : ")
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            print(a)
            print(i)
    print(a)   
print("Sorted : ",a)