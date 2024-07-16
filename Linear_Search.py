array = list(map(int, input("Enter numbers separated by spaces: ").split()))
target =int (input("Enter your target value : "))
position = 0
length = len(array)

while position<length:
    if array[position]==target:
        
       print("Position : ", position)
       break
    position+=1
    
if position==length:
        print("Not Found")
      
        
    
    
    
