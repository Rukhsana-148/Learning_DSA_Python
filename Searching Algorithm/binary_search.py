array = list(map(int,input("Take an array : ").split()))
sortedArray = sorted(array)
print("Sorted Array : ", sortedArray)
target = int(input("Guess a number : "))
low, high = 0, len(sortedArray)-1
found = False
while low<=high:
    mid = (low+high)//2
    if sortedArray[mid]==target:
        print("Found, Position : ", mid+1)
        found = True
        break
    elif sortedArray[mid]>target:
        high = mid-1
    elif sortedArray[mid]<target:
        low = mid+1
if found==False:
    print("Not Found")
    