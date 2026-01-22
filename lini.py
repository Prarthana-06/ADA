n=int(input("enter number of elements:"))
arr=list(map(int,input("enter elements:").split()))
key=int(input("enter element to search:"))
found=False
for i in range(n):
    if arr[i]==key:
        print("elements found at postion",i+1)
        found=True
        break
if not found:
    print("element not found")    