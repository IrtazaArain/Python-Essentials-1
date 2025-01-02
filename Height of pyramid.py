blocks = int(input("Enter the number of blocks: "))
height = 0	
for i in range(1,blocks + 1):
    if blocks >= i:
        blocks -= i
        height +=1
print("The height of the pyramid:", height)
