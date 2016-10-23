def binarySearch(alist, item):
    first=0
    last=len(alist)-1
    found = False

    while first<=last and not found:
        midpoint=(first+last)//2
        if alist[midpoint]==item:
            found =True
        else:
            if item<alist[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
    return found
print("Enter the number to search")
num=int(input())
alist=[0, 1, 2, 8, 13, 17, 19, 32, 42,]
z=(binarySearch(alist,num))
if z==True:
    print("Number is present in the list")
else:
    print("Number is not present in the list")
